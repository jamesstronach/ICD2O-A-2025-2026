import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("First Pygame Test")

FPS = 120
RED = (255,0,0)
BLUE = (0,0,255)

dog = pygame.image.load("dog.png")
dog_rect = dog.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

running = True
background = RED
i = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False

    # i += 1
    # if i % 10000 == 0:
    #     if background == RED:
    #         background = BLUE
    #     else:
    #        background = RED
    #     screen.fill(RED)
    
    screen.fill(background)
    screen.blit(dog,dog_rect)

    pygame.display.flip() 