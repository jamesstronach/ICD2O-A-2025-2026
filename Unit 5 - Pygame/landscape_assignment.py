import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Landscape Assignment")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (160,32,240)
CYAN = (0,255,255)
BROWN = (150, 75, 0)
CUSTOM = (40,170,255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False
    pygame.draw.line(screen, BLACK, (0, 300), (840, 300), 6)
    pygame.draw.rect(screen, GREEN, (0, 304, 800, 800)) # GROUND
    pygame.draw.rect(screen, CYAN, (0, 0, 900, 296)) # SKY
    triangle_points = [(380, 200), (200, 290,), (600, 290)]

    pygame.draw.circle(screen, YELLOW, (650, 130), 60) # SUN
    pygame.draw.line(screen, YELLOW, (700, 100), (800, 75), 6)
    pygame.draw.ellipse(screen, WHITE, (80, 50, 220, 120)) # Cloud 1
    pygame.draw.ellipse(screen, WHITE, (400, 50, 110, 120)) # Cloud 2
    pygame.draw.rect(screen, BROWN, (250, 270, 300, 200)) # House body
    pygame.draw.polygon(screen, BROWN, triangle_points) # House roof
    pygame.draw.rect(screen, WHITE, (300, 400, 50, 70)) # door
    pygame.draw.circle(screen, BROWN, (310, 440), 7) # doorknob
    pygame.draw.ellipse(screen, WHITE, (100, 90, 120, 120)) # Cloud 1
    pygame.draw.ellipse(screen, WHITE, (350, 30, 110, 120)) # Cloud 2
    pygame.draw.rect(screen, CYAN, (285, 300, 75, 75)) # Window 1
    pygame.draw.rect(screen, CYAN, (430, 300, 75, 75)) # Window 2
    pygame.draw.rect(screen, BLACK, (285, 300, 75, 75), 3) # Window 1 outline
    pygame.draw.rect(screen, BLACK, (430, 300, 75, 75), 3) # Window 2 outline
    pygame.draw.arc(screen, BLACK, (680, 260, 75, 60), 0, 3.14159, 6) #bird 1
    pygame.draw.arc(screen, BLACK, (610, 260, 75, 60), 0, 3.14159, 6) # bird 1
    pygame.draw.arc(screen, BLACK, (680, 40, 50, 30), 0, 3.14159, 6) #bird 2
    pygame.draw.arc(screen, BLACK, (630, 40, 50, 30), 0, 3.14159, 6) # bird 2
    pygame.draw.arc(screen, BLACK, (80, 260, 75, 60), 0, 3.14159, 6) #bird 1
    pygame.draw.arc(screen, BLACK, (10, 260, 75, 60), 0, 3.14159, 6) # bird 1

    pygame.display.flip()




