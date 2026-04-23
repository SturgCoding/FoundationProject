""" 
    File: simulation.py
    Project: Foundation-CompApps
    Purpose: Write the pygame window code here, this will be called in main.py
"""

import os
import sys
import math
import pygame

sys.path.insert(0, os.path.dirname(__file__))  # lets Python find physics.py inside src/
from physics import PhysicsBody, PIXELS_PER_METER


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class BeanCan:
    def __init__(self, x, y, screen_width, screen_height):
        self.original_image = pygame.image.load("assets/bean_can.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (60, 100))
        self.rect  = self.image.get_rect()
        self.rect.x = int(x)
        self.rect.y = int(y)

        self.screen_width  = screen_width
        self.screen_height = screen_height

        # Create a PhysicsBody(rectangle) at the same position as the sprite
         
        self.physics = PhysicsBody(x, y, mass=0.4)

        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

        self._pos_history = []  
        

    def update(self, dt):
        if self.dragging:
            return  # physics is paused while being held

        self.physics.update(dt)  # run SUVAT for this frame

        # --- Floor collision ---
        global ground_y
        ground_y = self.screen_height - self.rect.height
        if self.physics.y >= ground_y and self.physics.in_flight:
            self.physics.bounce(ground_y)

        # --- Keep settled can on the floor ---
        if self.physics.grounded:
            self.physics.y = float(ground_y)

        # Copy physics pixel position into the sprite rectangle
        self.rect.x = int(self.physics.x)
        self.rect.y = int(self.physics.y)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                if self.rect.collidepoint(event.pos):
                    self.dragging = True
                    self.offset_x = self.rect.x - event.pos[0]
                    self.offset_y = self.rect.y - event.pos[1]
                    self._prev_mouse_pos  = event.pos
                    self._prev_mouse_time = pygame.time.get_ticks() / 1000.0
                    self.physics.in_flight = False  # pause physics while held
                    self.physics.grounded  = False
                    self._pos_history.clear()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.dragging:
                self.dragging = False
                now = pygame.time.get_ticks() / 1000.0
                start = now

                vx_px, vy_px = 0.0, 0.0
                # Walk backwards to find a sample >= 50ms old.
                # Using just the last frame gives elapsed~=0 (same tick) → no velocity.
                """I tried fixing michael jakson issue. It didn't work out yet, but code still works."""
                if self.physics.grounded != True:
                    for pos, t in reversed(self._pos_history):
                        elapsed = now - t
                        if elapsed >= 0.05:
                            vx_px = (event.pos[0] - pos[0]) / elapsed
                            vy_px = (event.pos[1] - pos[1]) / elapsed
                            break
                    else:
                        if self._pos_history:
                            pos, t = self._pos_history[0]
                            elapsed = now - t
                            if elapsed > 0.001:
                                vx_px = (event.pos[0] - pos[0]) / elapsed
                                vy_px = (event.pos[1] - pos[1]) / elapsed
                    self.physics.release(
                    vx_ms=vx_px / PIXELS_PER_METER,
                    vy_ms=vy_px / PIXELS_PER_METER,
                    )
                    if self.physics.y == ground_y and self.physics.vy == 0:
                        time_used = pygame.time.get_ticks()/1000 - start
                        print(time_used)
                
        elif event.type == pygame.MOUSEMOTION:
            if self.physics.grounded != True:
                if self.dragging:
                    self.rect.x = event.pos[0] + self.offset_x
                    self.rect.y = event.pos[1] + self.offset_y
                    self.physics.x = float(self.rect.x)
                    self.physics.y = float(self.rect.y)
                    # Record position snapshot for throw velocity estimation
                    self._pos_history.append((event.pos, pygame.time.get_ticks() / 1000.0))
                    if len(self._pos_history) > 15:
                        self._pos_history.pop(0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    #load the bean can


def draw_arrow(surface, colour, start, end, width = 2, head = 10):
    if width <= 0: return
    pygame.draw.line(surface, colour, start, end, width)

    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.hypot(dx, dy)
    if length < 0.5:
        return  # too short(and eliminating division by 0)

    # unit vector pointing in the direction of the arrow
    ux = dx / length
    uy = dy / length

    # Two points that make the arrowhead triangle (perpendicular to the line)
    p1 = (end[0] - head * ux + head * 0.4 * uy,
          end[1] - head * uy - head * 0.4 * ux)
    p2 = (end[0] - head * ux - head * 0.4 * uy,
          end[1] - head * uy + head * 0.4 * ux)

    # Use anti-aliased polygon for smoother arrow tips
    pygame.draw.polygon(surface, colour, [end, p1, p2])
    pygame.draw.aalines(surface, colour, True, [end, p1, p2])

def draw_velocity_vector(surface, bean_can):
    """
    Draw the three SUVAT velocity vectors on screen:
      - Blue  = horizontal component (vx)
      - Red   = vertical component   (vy)
      - Yellow = resultant speed      (v)
    """
    if not bean_can.physics.in_flight:
        return  # only draw when in the air
    
    cx = bean_can.rect.centerx
    cy = bean_can.rect.centery
    SCALE = 8  # how many pixels per m/s for the velocity vectors(bigger/smaller arrows)
    
    vx = bean_can.physics.vx#m/s positive = right negative = left
    vy = bean_can.physics.vy#m/s positive = DOWN(PYGAME STUFF)

#horizontal arrow(velocity)
    if abs(vx) > 0.1:
        draw_arrow(surface, (80, 120, 255),
                     (cx, cy),
                     (cx + vx * SCALE, cy),
                     width=3, head=12)
#vertical arrow(velocity)
    if abs(vy) > 0.1:
        draw_arrow(surface, (255,80, 80),
                     (cx, cy),
                     (cx, int(cy + vy * SCALE)))
        
    if math.hypot(vx, vy) > 0.1:
        draw_arrow(surface, (255, 220, 60),
                     (cx, cy),
                     (int(cx + vx * SCALE), int(cy + vy * SCALE)))


def draw_suvat_overlay(surface, font, physics):
    """
    Draw real-time SUVAT values as a text overlay inside a professional semi-transparent panel.
    """
    lines = [
        "--- SUVAT ---",
        f"Time (t): {physics.t:.2f} s",
        f"Disp (s): x={physics.sx:.2f}m, y={physics.sy:.2f}m",
        f"Init Vel (u): x={physics.ux:.2f}m/s, y={physics.uy:.2f}m/s",
        f"Final Vel (v): x={physics.vx:.2f}m/s, y={physics.vy:.2f}m/s",
        f"Accel (a): x={physics.ax:.2f}m/s², y={physics.ay:.2f}m/s²",
    ]
    
    # Measure text block size
    max_w = 0
    total_h = 0
    text_surfs = []
    
    for line in lines:
        text_surf = font.render(line, True, (240, 240, 245))
        text_surfs.append(text_surf)
        max_w = max(max_w, text_surf.get_width())
        total_h += 25
        
    pad = 15
    rect = pygame.Rect(10, 10, max_w + pad*2, total_h + pad)
    
    # Draw semi-transparent panel
    overlay = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (30, 35, 45, 200), overlay.get_rect(), border_radius=8)
    surface.blit(overlay, (rect.x, rect.y))
    
    y = rect.y + pad
    for text_surf in text_surfs:
        surface.blit(text_surf, (rect.x + pad, y))
        y += 25

def draw_background(surface, width, height):
    """Draw a smooth gradient and a professional grid."""
    # Gradient background
    for y in range(height):
        # Top color to bottom color interpolation (sky-like logic if you want but simple slate here)
        r = int(245 - (y / height) * 20)
        g = int(247 - (y / height) * 20)
        b = int(250 - (y / height) * 15)
        pygame.draw.line(surface, (r, g, b), (0, y), (width, y))

    # Grid Lines (1 meter intervals)
    
    grid_color = (200, 210, 220)
    # Vertical lines
    for x in range(0, width, PIXELS_PER_METER):
        pygame.draw.line(surface, grid_color, (x, 0), (x, height))
    # Horizontal lines
    for y in range(height, 0, -PIXELS_PER_METER):
        pygame.draw.line(surface, grid_color, (0, y), (width, y))

#MAIN LOOP
def run_simulation(queue=None):
    # queue receives gravity/mass updates from the tkinter window
    pygame.init()

    SCREEN_WIDTH  = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("gravity sim")
    icon = pygame.image.load("assets/bean_can.png").convert_alpha()
    pygame.display.set_icon(icon)

    WHITE = (255, 255, 255)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 14)

    # Pass screen size into BeanCan so it knows where the floor/walls are
    global bean
    bean = BeanCan(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                   SCREEN_WIDTH, SCREEN_HEIGHT)
    # Start it falling immediately (u=0 means dropped from rest)
    bean.physics.release(vx_ms=0.0, vy_ms=0.0)
    #defining properties of reseted bean can
    def reset_bean():
        # Move it back to screen center
        bean.rect.centerx = SCREEN_WIDTH // 2
        bean.rect.centery = SCREEN_HEIGHT // 2

        bean.physics.x = float(bean.rect.x)
        bean.physics.y = float(bean.rect.y)

        # Stop movement of bean can and putting it on the ground
        bean.physics.vx = 0
        bean.physics.vy = 0
        bean.physics.in_flight = False
        bean.physics.grounded = True
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # seconds since last frame
         # Check if tkinter sent new values via the queue
        if queue:
            try:
                settings = queue.get_nowait()
                #Checking for reset message
                if settings.get('reset'):
                    reset_bean()
                new_gravity = settings.get('gravity', bean.physics.ay)
                if new_gravity != bean.physics.ay:
                    bean.physics.ay = new_gravity
                    # Rebaseline SUVAT so new gravity applies from NOW, not retroactively
                    if bean.physics.in_flight:
                        bean.physics.release(bean.physics.vx, bean.physics.vy)
                bean.physics.mass = settings.get('mass', bean.physics.mass)
            except Exception:
                pass  # queue empty this frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            bean.handle_event(event)

        bean.update(dt)   

        screen.fill(WHITE)
        draw_background(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Draw a solid ground floor slightly more prominent
        floor_rect = pygame.Rect(0, SCREEN_HEIGHT - 2, SCREEN_WIDTH, 2)
        pygame.draw.rect(screen, (100, 150, 200), floor_rect)

        bean.draw(screen)
        draw_velocity_vector(screen, bean)
        draw_suvat_overlay(screen, font, bean.physics)
        pygame.display.flip()

    pygame.quit()
    sys.exit()




