import pygame
import sys
import random

# --- INITIALIZATION ---
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 608
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cavern Quest")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

# --- TILES ---
grass   = pygame.image.load("grass_32.png").convert()
dirt1   = pygame.image.load("dirt-pixilart.png").convert()
dirt2   = pygame.image.load("dirt-2-pixilart.png").convert()
cobble1 = pygame.image.load("cobble1.png").convert()
cobble2 = pygame.image.load("cobble2-pixilart.png").convert()
coal    = pygame.image.load("coal.png").convert()

TILE_DICT  = {1: grass, 2: dirt1, 3: dirt2, 4: cobble1, 5: cobble2, 6: coal}
MINE_TIMES = {1: 60, 2: 120, 3: 180, 4: 300, 5: 360, 6: 400}
MINE_REACH = 80

# --- BLOCK SHEET ---
block_sheet  = pygame.image.load("block.png").convert()
BLOCK_CELL_W = block_sheet.get_width() // 4
BLOCK_CELL_H = block_sheet.get_height() // 4
BLOCK_BG_KEY = block_sheet.get_at((0, 0))
block_sheet.set_colorkey(BLOCK_BG_KEY)

# --- PLAYER SPRITE SETUP ---
turtle     = pygame.image.load("turtle.png").convert()
walk_sheet = pygame.image.load("turtle1.png").convert()
BG_KEY      = turtle.get_at((0, 0))
WALK_BG_KEY = walk_sheet.get_at((0, 0))
turtle.set_colorkey(BG_KEY)
walk_sheet.set_colorkey(WALK_BG_KEY)

IDLE_CELL_W = turtle.get_width() // 10
IDLE_CELL_H = turtle.get_height()
WALK_CELL_W = walk_sheet.get_width() // 12
WALK_CELL_H = walk_sheet.get_height()

PLAYER_W = 28
PLAYER_H = 20

# --- PICKAXE ---
pickaxe_img = pygame.image.load("pickaxe.png").convert()
PICK_BG_KEY = pickaxe_img.get_at((0, 0))
pickaxe_img.set_colorkey(PICK_BG_KEY)
pickaxe_img = pygame.transform.scale(pickaxe_img, (20, 20))

# --- SWORD ITEM (NEW) ---
sword_item_img = pygame.image.load("sword.png").convert()
SWORD_ITEM_BG = sword_item_img.get_at((0, 0))
sword_item_img.set_colorkey(SWORD_ITEM_BG)
sword_item_img = pygame.transform.scale(sword_item_img, (20, 20)) # Scaled to match pickaxe

# --- SWORD ANIMATION EFFECT SETUP ---
sword_sheet = pygame.image.load("swing_sheet.png").convert()
SWORD_BG_KEY = sword_sheet.get_at((0, 0))
sword_sheet.set_colorkey(SWORD_BG_KEY)
SWORD_FRAMES_COUNT = 5
SWORD_W = sword_sheet.get_width() // SWORD_FRAMES_COUNT
SWORD_H = sword_sheet.get_height()

sword_frames = []
for i in range(SWORD_FRAMES_COUNT):
    frame = sword_sheet.subsurface((i * SWORD_W, 0, SWORD_W, SWORD_H)).copy()
    frame.set_colorkey(SWORD_BG_KEY)
    sword_frames.append(pygame.transform.scale(frame, (40, 40)))

# --- GLOBALS ---
is_swinging     = False
swing_angle     = 45
swing_direction = 1
SWING_SPEED     = 8
SWING_MAX_ANGLE = 80
SWING_MIN_ANGLE = 10

is_slashing      = False
sword_anim_index = 0
sword_anim_timer = 0
SWORD_ANIM_SPEED = 2 

is_blocking       = False
block_frame_index = 0
block_timer       = 0
block_speed       = 4

inventory = {"coal": 0}
hotbar            = ["pickaxe", "sword"]
active_slot_index = 0

player_x          = 600
player_y          = 160
velocity_y        = 0
gravity           = 0.1
jump_force        = -3
player_walk_speed = 0.5
player_run_speed  = 2
on_ground         = False
facing_left       = False
was_moving        = False

IDLE_FEET_OFFSET   = 20
COLLISION_OFFSET_X = 2

frame_index     = 0
animation_timer = 0
animation_speed = 15

mining_target   = None
mining_progress = 0

game_state   = "PLAY"
jump_pressed = False

camera_x = 0
camera_y = 0

# --- HELPER FUNCTIONS ---
def crop_and_scale(frame, key, w, h):
    frame.set_colorkey(key)
    mask   = pygame.mask.from_surface(frame)
    bounds = mask.get_bounding_rects()
    if bounds:
        cropped = frame.subsurface(bounds[0]).copy()
        return pygame.transform.scale(cropped, (w, h))
    return pygame.transform.scale(frame, (w, h))

def get_tile_at(px, py):
    col = int(px) // 32
    row = int(py) // 32
    if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
        return grid[row][col]
    return 0

def generate_world(cols, rows):
    new_grid = []
    
    # --- ARENA SETTINGS ---
    arena_width = 14
    arena_height = 7
    arena_y_level = 22 # How deep it spawns
    center_x = cols // 2 # Finds the exact middle of your map
    
    for r in range(rows):
        row_data = []
        for c in range(cols):
            # 1. BOSS ARENA CHECK
            if (center_x - arena_width // 2 <= c <= center_x + arena_width // 2) and (arena_y_level <= r < arena_y_level + arena_height):
                row_data.append(0)
            # 2. STANDARD WORLD
            elif r < 8:
                row_data.append(0)  # Sky
            elif r == 8:
                row_data.append(1)  # Grass
            elif r < 12:
                row_data.append(random.choice([2, 3]))  # Dirt layer
            elif r < 20:
                row_data.append(6 if random.random() < 0.05 else 4) # Stone / Coal
            else:
                row_data.append(6 if random.random() < 0.08 else 5) # Deepslate / Coal
                
        new_grid.append(row_data)
    return new_grid

# --- INITIAL LOAD ---
block_frames = []
for row in range(4):
    for col in range(4):
        frame = block_sheet.subsurface((col * BLOCK_CELL_W, row * BLOCK_CELL_H, BLOCK_CELL_W, BLOCK_CELL_H)).copy()
        frame.set_colorkey(BLOCK_BG_KEY)
        mask   = pygame.mask.from_surface(frame)
        bounds = mask.get_bounding_rects()
        if bounds:
            frame = frame.subsurface(bounds[0]).copy()
            frame.set_colorkey(BLOCK_BG_KEY)
        block_frames.append(pygame.transform.scale(frame, (PLAYER_W, PLAYER_H)))

idle_frames = [crop_and_scale(turtle.subsurface((i * IDLE_CELL_W, 0, IDLE_CELL_W, IDLE_CELL_H)), BG_KEY, PLAYER_W, PLAYER_H) for i in range(10)]
walk_frames = [crop_and_scale(walk_sheet.subsurface((i * WALK_CELL_W, 0, WALK_CELL_W, WALK_CELL_H)), WALK_BG_KEY, PLAYER_W, PLAYER_H) for i in range(12)]

grid = generate_world(100, 100) 

map_width  = len(grid[0]) * 32
map_height = len(grid)    * 32

# --- SYSTEM FUNCTIONS ---

def handle_events():
    global running, game_state, is_blocking, velocity_y, on_ground, jump_pressed, block_frame_index, block_timer, active_slot_index
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = "PLAY"
            if event.key == pygame.K_TAB:
                game_state = "CRAFTING" if game_state == "PLAY" else "PLAY"
            if event.key == pygame.K_f:
                is_blocking = True
            
            if event.key == pygame.K_1:
                active_slot_index = 0
            if event.key == pygame.K_2:
                active_slot_index = 1
                
            if game_state == "PLAY":
                if event.key == pygame.K_SPACE and on_ground:
                    velocity_y   = jump_force
                    on_ground    = False
                    jump_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jump_pressed = False
            if event.key == pygame.K_f:
                is_blocking       = False
                block_frame_index = 0
                block_timer       = 0

def physics_and_movement():
    global player_x, player_y, velocity_y, on_ground, facing_left, moving, camera_x, camera_y
    keys = pygame.key.get_pressed()
    speed = player_run_speed if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) else player_walk_speed
    moving = False

    if not is_blocking:
        if keys[pygame.K_LEFT]:
            player_x   -= speed
            moving      = True
            facing_left = True
        if keys[pygame.K_RIGHT]:
            player_x   += speed
            moving      = True
            facing_left = False

    if get_tile_at(player_x + COLLISION_OFFSET_X, player_y + PLAYER_H // 2) != 0 and keys[pygame.K_LEFT]: player_x += speed
    if get_tile_at(player_x + PLAYER_W - COLLISION_OFFSET_X, player_y + PLAYER_H // 2) != 0 and keys[pygame.K_RIGHT]: player_x -= speed
    player_x = max(0, min(player_x, map_width - PLAYER_W))

    velocity_y += gravity
    player_y   += velocity_y

    head = player_y + 4
    if (get_tile_at(player_x + COLLISION_OFFSET_X, head) != 0 or get_tile_at(player_x + PLAYER_W - COLLISION_OFFSET_X, head) != 0) and velocity_y < 0:
        player_y   = (int(head) // 32 + 1) * 32 - 4
        velocity_y = 0

    feet = player_y + IDLE_FEET_OFFSET
    if (get_tile_at(player_x + COLLISION_OFFSET_X, feet) != 0 or get_tile_at(player_x + PLAYER_W - COLLISION_OFFSET_X, feet) != 0) and velocity_y > 0:
        player_y   = (int(feet) // 32) * 32 - IDLE_FEET_OFFSET
        velocity_y = 0
        on_ground  = True
    else:
        on_ground = False

    if player_y + IDLE_FEET_OFFSET > map_height:
        player_y   = map_height - IDLE_FEET_OFFSET
        velocity_y = 0
        on_ground  = True

    camera_x = max(0, min(int(player_x - SCREEN_WIDTH // 2.3), map_width - SCREEN_WIDTH))
    camera_y = max(0, min(int(player_y - SCREEN_HEIGHT // 2), map_height - SCREEN_HEIGHT))

def actions():
    global mining_target, mining_progress, is_swinging, swing_angle, swing_direction, is_slashing, sword_anim_index, sword_anim_timer
    mouse_held = pygame.mouse.get_pressed()[0]
    mouse_x, mouse_y = pygame.mouse.get_pos()
    world_mouse_x, world_mouse_y = mouse_x + camera_x, mouse_y + camera_y
    tile_col, tile_row = int(world_mouse_x) // 32, int(world_mouse_y) // 32
    dist = ((world_mouse_x - (player_x + PLAYER_W // 2)) ** 2 + (world_mouse_y - (player_y + PLAYER_H // 2)) ** 2) ** 0.5

    current_item = hotbar[active_slot_index]

    if mouse_held and not is_blocking:
        if current_item == "pickaxe":
            if dist <= MINE_REACH:
                if 0 <= tile_row < len(grid) and 0 <= tile_col < len(grid[tile_row]):
                    tile_val = grid[tile_row][tile_col]
                    if tile_val != 0:
                        if mining_target == (tile_col, tile_row):
                            mining_progress += 1
                            if mining_progress >= MINE_TIMES.get(tile_val, 120):
                                grid[tile_row][tile_col] = 0
                                if tile_val == 6: inventory["coal"] += 1
                                mining_target, mining_progress = None, 0
                        else:
                            mining_target, mining_progress = (tile_col, tile_row), 0
            is_swinging = True
            
        elif current_item == "sword":
            is_slashing = True
            is_swinging = True  # Added so the physical sword item rotates too
    else:
        mining_target, mining_progress = None, 0

    if is_swinging:
        swing_angle += SWING_SPEED * swing_direction
        if swing_angle >= SWING_MAX_ANGLE: swing_direction = -1
        if swing_angle <= SWING_MIN_ANGLE: swing_direction = 1
        
        # Check if mouse released or item changed
        if not mouse_held or (current_item != "pickaxe" and current_item != "sword"):
            if swing_angle > 45: swing_angle -= SWING_SPEED
            elif swing_angle < 45: swing_angle += SWING_SPEED
            else: is_swinging, swing_angle = False, 45

    if is_slashing:
        sword_anim_timer += 1
        if sword_anim_timer >= SWORD_ANIM_SPEED:
            sword_anim_timer = 0
            sword_anim_index += 1
            if sword_anim_index >= len(sword_frames):
                sword_anim_index = 0
                if not mouse_held or current_item != "sword":
                    is_slashing = False
    else:
        sword_anim_index = 0

def animations():
    global block_timer, block_frame_index, frame_index, animation_timer, was_moving
    if is_blocking:
        block_timer += 1
        if block_timer >= block_speed:
            block_timer = 0
            if block_frame_index < len(block_frames) - 1: block_frame_index += 1

    if moving != was_moving:
        frame_index, animation_timer = 0, 0
    was_moving = moving

    animation_timer += 1
    if animation_timer >= animation_speed:
        animation_timer = 0
        if moving: frame_index = (frame_index + 1) % len(walk_frames)
        else: frame_index = (frame_index + 1) % len(idle_frames)

def draw_world():
    start_col = max(0, camera_x // 32)
    end_col   = min(len(grid[0]), (camera_x + SCREEN_WIDTH) // 32 + 1)
    start_row = max(0, camera_y // 32)
    end_row   = min(len(grid), (camera_y + SCREEN_HEIGHT) // 32 + 1)

    for ri in range(start_row, end_row):
        for ci in range(start_col, end_col):
            val = grid[ri][ci]
            if val in TILE_DICT:
                screen.blit(TILE_DICT[val], (ci * 32 - camera_x, ri * 32 - camera_y))

def draw_player():
    if is_blocking: player_frame = block_frames[block_frame_index]
    else: player_frame = walk_frames[frame_index] if moving else idle_frames[frame_index]
    
    if facing_left: player_frame = pygame.transform.flip(player_frame, True, False)
    screen.blit(player_frame, (player_x - camera_x, player_y - camera_y))

    current_item = hotbar[active_slot_index]

    if not is_blocking:
        # DRAW PICKAXE
        if current_item == "pickaxe":
            if not facing_left:
                angle = -swing_angle + 45
                rotated_pick = pygame.transform.rotate(pickaxe_img, angle)
                pick_offset_x = PLAYER_W
            else:
                flipped_pick = pygame.transform.flip(pickaxe_img, True, False)
                angle = swing_angle - 45
                rotated_pick = pygame.transform.rotate(flipped_pick, angle)
                pick_offset_x = -rotated_pick.get_width()
                
            pick_offset_y = PLAYER_H // 2 - rotated_pick.get_height() // 2
            screen.blit(rotated_pick, (player_x - camera_x + pick_offset_x, player_y - camera_y + pick_offset_y))

        # DRAW SWORD AND EFFECT
        elif current_item == "sword":
            # 1. Draw the physical rotating sword item
            if not facing_left:
                angle = -swing_angle + 45
                rotated_sword = pygame.transform.rotate(sword_item_img, angle)
                sword_offset_x = PLAYER_W
            else:
                flipped_sword = pygame.transform.flip(sword_item_img, True, False)
                angle = swing_angle - 45
                rotated_sword = pygame.transform.rotate(flipped_sword, angle)
                sword_offset_x = -rotated_sword.get_width()
                
            sword_offset_y = PLAYER_H // 2 - rotated_sword.get_height() // 2
            screen.blit(rotated_sword, (player_x - camera_x + sword_offset_x, player_y - camera_y + sword_offset_y))

            # 2. Draw the slash effect overlay if actively attacking
            if is_slashing:
                sword_effect_img = sword_frames[sword_anim_index]
                player_center_x = player_x - camera_x + (PLAYER_W // 2)
                player_center_y = player_y - camera_y + (PLAYER_H // 2)
                
                if facing_left:
                    sword_effect_img = pygame.transform.flip(sword_effect_img, True, False)
                    draw_x = player_center_x - sword_effect_img.get_width()
                else:
                    draw_x = player_center_x 
                
                draw_y = player_center_y - (sword_effect_img.get_height() // 2)
                screen.blit(sword_effect_img, (draw_x, draw_y))

def draw_ui():
    if mining_target and game_state == "PLAY" and hotbar[active_slot_index] == "pickaxe":
        tc, tr = mining_target
        if grid[tr][tc] != 0:
            mine_time = MINE_TIMES.get(grid[tr][tc], 120)
            bar_x, bar_y = player_x - camera_x, player_y - camera_y - 12
            bar_width = int((mining_progress / mine_time) * 32)
            pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, 32, 6))
            pygame.draw.rect(screen, (255, 200, 0), (bar_x, bar_y, bar_width, 6))

    pygame.draw.rect(screen, (40, 40, 40), (10, 10, 160, 36))
    screen.blit(font.render(f"Equipped: {hotbar[active_slot_index]}", True, (255, 255, 255)), (18, 18))
    
    # --- NEW: COORDINATE SYSTEM HUD ---
    tile_x, tile_y = int(player_x // 32), int(player_y // 32)
    coord_surface = font.render(f"Pos  X: {tile_x} | Y: {tile_y}", True, (255, 255, 255))
    coord_rect = coord_surface.get_rect(topright=(SCREEN_WIDTH - 15, 15))
    pygame.draw.rect(screen, (40, 40, 40), coord_rect.inflate(20, 10))
    screen.blit(coord_surface, coord_rect)
    
    inv_y = 55
    for item, count in inventory.items():
        screen.blit(font.render(f"{item.capitalize()}: {count}", True, (220, 220, 220)), (10, inv_y))
        inv_y += 22

    if game_state == "CRAFTING":
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        pygame.draw.rect(screen, (100, 100, 100), (200, 100, 400, 400), border_radius=10)
        screen.blit(font.render("Crafting Menu (TAB to close)", True, (255, 255, 255)), (220, 120))

# --- MAIN LOOP ---
running = True
while running:
    handle_events()
    screen.fill((135, 206, 235))

    if game_state == "PLAY":
        physics_and_movement()
        actions()
        animations()
    
    draw_world()
    
    # generate_world(100, 30) <--- REMOVED! This was causing your world to regenerate over itself every single frame!
    
    draw_player()
    draw_ui()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()