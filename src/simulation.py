""" 
    File: simulation.py
    Project: Foundation-CompApps
    Purpose: Write the pygame window code here, this will be called in main.py
"""

import os
import sys
import math
import pygame

sys.path.insert(0, os.path.dirname(__file__))
from physics import PhysicsBody, PIXELS_PER_METER

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

        #on every mouse event while dragging
        self._prev_mouse_pos  = (float(x), float(y)) #save the position
        self._prev_mouse_time = pygame.time.get_ticks() / 1000.0 #save the time

        

    def update(self, dt):
        if self.dragging:
            return  # physics is paused while being held

        self.physics.update(dt)  # run SUVAT for this frame

        # --- Floor collision ---
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

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.dragging:
                self.dragging = False
                now = pygame.time.get_ticks() / 1000.0
                elapsed = now - self._prev_mouse_time


                if elapsed > 0:
                    # Work out how fast the mouse was moving in pixels/second
                    vx_px = (event.pos[0] - self._prev_mouse_pos[0]) / elapsed
                    vy_px = (event.pos[1] - self._prev_mouse_pos[1]) / elapsed
                else:
                    vx_px, vy_px = 0.0, 0.0

                # Divide by PIXELS_PER_METER to convert px/s → m/s, then launch
                self.physics.release(
                    vx_ms=vx_px / PIXELS_PER_METER,
                    vy_ms=vy_px / PIXELS_PER_METER,
                )

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.rect.x = event.pos[0] + self.offset_x
                self.rect.y = event.pos[1] + self.offset_y
                # Keep physics position synced while dragging
                self.physics.x = float(self.rect.x)
                self.physics.y = float(self.rect.y)
                # Update snapshot for velocity estimation
                self._prev_mouse_pos  = event.pos
                self._prev_mouse_time = pygame.time.get_ticks() / 1000.0

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    #load the bean can


def draw_arrow(surface, colour, start, end, width = 2, head = 10):
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

    pygame.draw.polygon(surface, colour, [end, p1, p2])

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


#MAIN LOOP
def run_simulation():
    pygame.init()

    info = pygame.display.Info()
    SCREEN_WIDTH  = info.current_w
    SCREEN_HEIGHT = info.current_h - 50

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("gravity sim")

    WHITE = (255, 255, 255)
    clock = pygame.time.Clock()

    # Pass screen size into BeanCan so it knows where the floor/walls are
    bean = BeanCan(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                   SCREEN_WIDTH, SCREEN_HEIGHT)

    # Start it falling immediately (u=0 means dropped from rest)
    bean.physics.release(vx_ms=0.0, vy_ms=0.0)

    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # seconds since last frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            bean.handle_event(event)

        bean.update(dt)   

        screen.fill(WHITE)
        bean.draw(screen)
        draw_velocity_vector(screen, bean)
        pygame.display.flip()

    pygame.quit()
    sys.exit()




