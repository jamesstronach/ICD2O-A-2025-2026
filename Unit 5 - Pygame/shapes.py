import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pygame: Colours + Shapes")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (160,32,240)
CYAN = (0,255,255)
CUSTOM = (40,170,255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False

    screen.fill((WHITE))
    pygame.draw.rect(screen, BLUE, (80, 80, 160, 100)) # filled 
    # pygame.draw.rect(screen, BLACK, (80, 80, 160, 100), 3) # outline 
    # pygame.draw.circle(screen, RED, (450, 130), 60) # filled
    # pygame.draw.circle(screen, BLACK, (450, 130), 60, 3) # outline
    # pygame.draw.line(screen, GREEN, (60, 520), (840, 520), 6)
    triangle_points = [(650, 250), (800, 400,), (500, 400)]
    pygame.draw.polygon(screen, PURPLE, triangle_points)
    pygame.draw.polygon(screen, BLACK, triangle_points, 3)
    pygame.draw.ellipse(screen, CUSTOM, (80, 260, 220, 120)) # filled
    pygame.draw.ellipse(screen, BLACK, (80, 260, 220, 120), 3) # outline
    pygame.draw.arc(screen, CYAN, (360, 260, 180, 120), 0, 3.14159, 6)
    pygame.draw.rect(screen, YELLOW, (720, 60, 50, 50))
    pygame.draw.rect(screen, CYAN, (780, 60, 50, 50))
    pygame.draw.rect(screen, PURPLE, (840, 60, 50, 50))


    pygame.display.flip()

pygame.quit()


