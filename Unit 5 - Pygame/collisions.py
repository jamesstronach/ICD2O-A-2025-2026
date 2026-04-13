import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Collision Detection")
clock = pygame.time.Clock()

x = random.randint(0,SCREEN_WIDTH-20)
player1_rect = pygame.Rect(100,75,50,75)
player2_rect = pygame.Rect(500,75,50,75)
prize_rect = pygame.Rect(300,500,20,20)
dx = 1
dy = 1

score1 = 0
score2 = 0
font = pygame.font.SysFont(None, 40)


# main game loop runs until game is over
running = True
while running:
    # events (quit, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]: player1_rect.x += dx
    if key[pygame.K_LEFT]: player1_rect.x -= dx
    if key[pygame.K_UP]: player1_rect.y -= dy
    if key[pygame.K_DOWN]: player1_rect.y += dy

    player1_rect.x = max(0, player1_rect.x)
    player1_rect.y = max(0, player1_rect.y)
    player1_rect.y = min(SCREEN_HEIGHT-player1_rect.h, player1_rect.y)
    player1_rect.x = min(SCREEN_WIDTH-player1_rect.w, player1_rect.x)

    key = pygame.key.get_pressed()
    if key[pygame.K_d]: player2_rect.x += dx
    if key[pygame.K_a]: player2_rect.x -= dx
    if key[pygame.K_w]: player2_rect.y -= dy
    if key[pygame.K_s]: player2_rect.y += dy

    player2_rect.x = max(0, player2_rect.x)
    player2_rect.y = max(0, player2_rect.y)
    player2_rect.y = min(SCREEN_HEIGHT-player2_rect.h, player2_rect.y)
    player2_rect.x = min(SCREEN_WIDTH-player2_rect.w, player2_rect.x)
    # player1_rect.y += dx
    # dx += 0.15

    # SCREEN_WIDTH
    # SCREEN_HEIGHT

    screen.fill((50,50,0))
    pygame.draw.rect(screen,(255,0,0), player1_rect)
    pygame.draw.rect(screen,(0,255,0), player2_rect)
    pygame.draw.rect(screen,(0,255,255), prize_rect)

    msg = font.render(str(score1) + " - " + str(score2), True, (200, 200, 210))
    screen.blit(msg, (12, 10))

    pygame.display.flip() # redraw the screen

    
    clock.tick(300)

pygame.quit()
