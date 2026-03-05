""" 
    File: gui.py
    Project: Foundation-CompApps
    Purpose: Write the pygame window code here, this will be called in main.py
"""




import pygame

import sys
  





class BeanCan:
    def __init__(self,x ,y):
        self.original_image = pygame.image.load("assets/bean_can.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (60, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.mass = 1.0
    def update(self, time_delta):
        if not self.dragging:
            self.vy += self.ay * time_delta # v = u + a * t
            self.rect.y += self.vy * time_delta # s = ut + 0.5 * a * t^2
            self.rect.x += self.vx * time_delta
             
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



#MAIN LOOP
def run_simulation():
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
    bean = BeanCan(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
    
    #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            bean.handle_event(event)
        screen.fill(WHITE)
        bean.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()




