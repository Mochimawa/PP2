import pygame

pygame.init()

WIDTH, HEIGHT = 420, 500 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_SIZE = 50
STEP = 20 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

x = WIDTH // 2 - BALL_SIZE // 2
y = HEIGHT // 2 - BALL_SIZE // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
      
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x - STEP >= 0:         
                
                x -= STEP
        if keys[pygame.K_RIGHT] and x + STEP <= WIDTH - BALL_SIZE:
              
                    x += STEP
        if keys[pygame.K_UP] and y - STEP >=0:
                
                    y -= STEP
        if keys[pygame.K_DOWN] and y + STEP <= HEIGHT - BALL_SIZE:
               
                    y += STEP

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x + BALL_SIZE // 2, y + BALL_SIZE // 2), BALL_SIZE // 2)
    
    pygame.display.flip()

pygame.quit()