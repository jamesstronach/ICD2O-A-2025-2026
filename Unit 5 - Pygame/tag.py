
import pygame
import random
pygame.init()
# prepare the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision Detection")
clock = pygame.time.Clock()
# --- sizes ---
PLAYER_SIZE = 20
PRIZE_SIZE = 20
player1_rect = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)
player2_rect = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)
prize_rect = pygame.Rect(0, 0, PRIZE_SIZE, PRIZE_SIZE)
dx = 3
dy = 3
def rectangles_overlap(r1, r2):
    global score1
    score1 = 0
    global score2
    score2 = 0
    global it_player
    it_player = 1

    r1_left   = r1.x
    r1_right  = r1.x + r1.w
    r1_top    = r1.y
    r1_bottom = r1.y + r1.h
    r2_left   = r2.x
    r2_right  = r2.x + r2.w
    r2_top    = r2.y
    r2_bottom = r2.y + r2.h
    overlap_x = (r1_left < r2_right) and (r1_right > r2_left)
    overlap_y = (r1_top  < r2_bottom) and (r1_bottom > r2_top)
    
    if overlap_x and overlap_y and it_player == 1:
        score1 += 1
        it_player += 1
    
    if overlap_x and overlap_y and it_player == 2:
        score2 += 1
        it_player -= 1

    return overlap_x and overlap_y and it_player


def keep_on_screen(r):
    r.x = max(0, min(SCREEN_WIDTH - r.w, r.x))
    r.y = max(0, min(SCREEN_HEIGHT - r.h, r.y))
def random_on_screen(r):
    r.x = random.randint(0, SCREEN_WIDTH - r.w)
    r.y = random.randint(0, SCREEN_HEIGHT - r.h)
# --- place players so they DON'T overlap at the start ---
random_on_screen(player1_rect)
while True:
    random_on_screen(player2_rect)
    if not rectangles_overlap(player1_rect, player2_rect):
        break
# --- place prize (starter) ---
random_on_screen(prize_rect)

font = pygame.font.SysFont(None, 40)
# IT player (1 or 2) - Player 1 starts as IT

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    # ---------------- Player 1 movement ----------------
    old1_x, old1_y = player1_rect.x, player1_rect.y
    if keys[pygame.K_RIGHT]: player1_rect.x += dx
    if keys[pygame.K_LEFT]:  player1_rect.x -= dx
    if keys[pygame.K_UP]:    player1_rect.y -= dy
    if keys[pygame.K_DOWN]:  player1_rect.y += dy
    keep_on_screen(player1_rect)
    # If player 1 moved into player 2, put player 1 back
    if rectangles_overlap(player1_rect, player2_rect):
        player1_rect.x, player1_rect.y = old1_x, old1_y
    # ---------------- Player 2 movement ----------------
    old2_x, old2_y = player2_rect.x, player2_rect.y
    if keys[pygame.K_d]: player2_rect.x += dx
    if keys[pygame.K_a]: player2_rect.x -= dx
    if keys[pygame.K_w]: player2_rect.y -= dy
    if keys[pygame.K_s]: player2_rect.y += dy
    keep_on_screen(player2_rect)
    # If player 2 moved into player 1, put player 2 back
    if rectangles_overlap(player2_rect, player1_rect):
        player2_rect.x, player2_rect.y = old2_x, old2_y
    # ---------------- draw ----------------
    screen.fill((128, 128, 128))
    pygame.draw.rect(screen, (150, 0, 0), player1_rect)
    pygame.draw.rect(screen, (0, 150, 0), player2_rect)
    pygame.draw.rect(screen, (0, 0, 150), prize_rect)
    msg = font.render(f"{score1} - {score2}", True, (200, 200, 210))
    screen.blit(msg, (12, 10))
    # stroke/outline on the IT player

    if it_player == 1:
        pygame.draw.rect(screen, (250, 250, 0), player1_rect, 2)
    else:
        pygame.draw.rect(screen, (250, 250, 0), player2_rect, 2)

    # -------------------------------------------------------------------------
    if rectangles_overlap(player1_rect, prize_rect):
        dx *= 1.5
        dy *= 1.5
        while True:
            random_on_screen(prize_rect)
            if not rectangles_overlap(player1_rect, prize_rect):
                break
            elif not rectangles_overlap(player2_rect, prize_rect):
                break
        
        if it_player == 2:
            dx /= 1.5
            dy /= 1.5
  
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

    rectangle = pygame.draw.rect, BLACK, (100,75,50,75)



    pygame.display.flip()
    clock.tick(60)


pygame.quit()
