""" 
    File: gui.py
    Project: Foundation-CompApps
    Purpose: Write the pygame window code here, this will be called in main.py
"""




import pygame
import pygame.surface
import pygame_gui
import sys
  
pygame.init()

info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 50))
pygame.display.set_caption("gravity sim")

#colours
WHITE = (255, 255, 255)
RED = (255, 50, 50)

#pygame clock
clock = pygame.time.Clock()

ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT - 50))

#slider for the mass
mass_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((50, 50), (200, 20)),
    start_value=1.0,
    value_range=(0.1, 10.0),
    manager=ui_manager
)

#label for the mass slider
mass_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((50, 20), (200, 20)),
    text="Mass:",
    manager=ui_manager
)


class BeanCan:
    def __init__(self,x ,y):
        self.original_image = pygame.image.load("bean_can.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (60, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.mass = 1.0
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                if self.rect.collidepoint(event.pos):
                    self.dragging = True
                    self.offset_x = self.rect.x - event.pos[0]
                    self.offset_y = self.rect.y - event.pos[1]
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
            
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.rect.x = event.pos[0] + self.offset_x
                self.rect.y = event.pos[1] + self.offset_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#load the bean can
bean = BeanCan(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


#MAIN LOOP
running = True
while running:
    time_delta = clock.tick(60) / 1000.0
   
   #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ui_manager.process_events(event)
        bean.handle_event(event)

     #checking if the slider moved
    ui_manager.update(time_delta)
    
    current_mass = mass_slider.get_current_value()
    bean.mass = current_mass

    mass_label.set_text(f"Mass: {current_mass:.1f} kg")

    screen.fill(WHITE)
    bean.draw(screen)
    ui_manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()



