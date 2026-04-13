import pygame
import sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 608
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cavern Quest")
clock = pygame.time.Clock()

# Tiles
grass = pygame.image.load("grass_32.png").convert()
dirt1 = pygame.image.load("dirt-pixilart.png").convert()
dirt2 = pygame.image.load("dirt-2-pixilart.png").convert()
cobble1 = pygame.image.load("cobble1.png").convert()
cobble2 = pygame.image.load("cobble2-pixilart.png").convert()
coal = pygame.image.load("coal.png").convert()
# NEW TILES: Create these 32x32 images
cloud = pygame.Surface((32, 32)) # Placeholder
cloud.fill((200, 200, 255))
chest_img = pygame.Surface((32, 32)) # Placeholder
chest_img.fill((139, 69, 19))

# Player & Animations
turtle = pygame.image.load("turtle.png").convert()
walk_sheet = pygame.image.load("turtle1.png").convert()
BG_KEY = turtle.get_at((0, 0))
WALK_BG_KEY = walk_sheet.get_at((0, 0))
turtle.set_colorkey(BG_KEY)
walk_sheet.set_colorkey(WALK_BG_KEY)

# New Animations/Items (You need to make/load these)
# Assuming swing sheet is 1 row, 5 columns
try:
    swing_sheet = pygame.image.load("swing_sheet.png").convert_alpha()
    SWING_W = swing_sheet.get_width() // 5
    SWING_H = swing_sheet.get_height()
    swing_frames = [swing_sheet.subsurface(pygame.Rect(i*SWING_W, 0, SWING_W, SWING_H)) for i in range(5)]
except FileNotFoundError:
    print("Warning: swing_sheet.png missing. Using placeholders.")
    swing_frames = [pygame.Surface((32,32), pygame.SRCALPHA) for _ in range(5)] # Placeholders

# Tools (for UI and hand)
sword_img = pygame.Surface((20, 20)); sword_img.fill((200, 200, 200))
pickaxe_img = pygame.Surface((20, 20)); pickaxe_img.fill((100, 100, 100))

# --- PLAYER SETUP ---
PLAYER_W, PLAYER_H = 28, 20
IDLE_CELL_W, IDLE_CELL_H = turtle.get_width() // 10, turtle.get_height() // 1
WALK_CELL_W, WALK_CELL_H = walk_sheet.get_width() // 12, walk_sheet.get_height() // 1

def crop_and_scale(frame, key, w, h):
    frame.set_colorkey(key)
    mask = pygame.mask.from_surface(frame)
    bounds = mask.get_bounding_rects()
    if bounds:
        cropped = frame.subsurface(bounds[0]).copy()
        return pygame.transform.scale(cropped, (w, h))
    return pygame.transform.scale(frame, (w, h))

idle_frames = [crop_and_scale(turtle.subsurface((i*IDLE_CELL_W, 0, IDLE_CELL_W, IDLE_CELL_H)), BG_KEY, PLAYER_W, PLAYER_H) for i in range(10)]
walk_frames = [crop_and_scale(walk_sheet.subsurface((i*WALK_CELL_W, 0, WALK_CELL_W, WALK_CELL_H)), WALK_BG_KEY, PLAYER_W, PLAYER_H) for i in range(12)]

# --- MAP & DATA SETUP ---
grid = []
chest_data = {} # Stores inventory for specific chests: {(col, row): {"coal": 5}}

try:
    with open("tile1.tile") as f:
        for line in f:
            grid.append([int(ch) for ch in line.strip()])
except FileNotFoundError:
    grid = [[0]*40 for _ in range(30)] # Fallback empty grid

map_height = len(grid) * 32
map_width = len(grid[0]) * 32 if grid else 0

TILE_DICT = {1: grass, 2: dirt1, 3: dirt2, 4: cobble1, 5: cobble2, 6: coal, 7: cloud, 8: chest_img}
MINE_TIMES = {1: 60, 2: 120, 3: 180, 4: 300, 5: 360, 6: 400, 7: 30, 8: 10}
MINE_REACH = 80

def get_tile_at(px, py):
    col, row = int(px) // 32, int(py) // 32
    if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
        return grid[row][col]
    return 0

# --- SYSTEMS DATA ---
# Inventory System
inventory = {"dirt": 0, "cobble": 0, "coal": 0, "cloud": 0}
hotbar = ["sword", "pickaxe"]
active_slot_index = 0

# Game States
game_state = "PLAY" # Can be "PLAY", "CRAFTING", "CHEST"
active_chest_pos = None

# Player Variables
player_x, player_y = 600, 160
velocity_y = 0
gravity, jump_force = 0.5, -8
player_walk_speed, player_run_speed = 3, 6
on_ground, facing_left, was_moving = False, False, False
IDLE_FEET_OFFSET, COLLISION_OFFSET_X = 20, 2

# Animation Variables
frame_index, animation_timer, animation_speed = 0, 0, 6
mining_target, mining_progress = None, 0

# Action Variables
is_swinging = False
swing_timer = 0
current_swing_frame = 0
is_blocking = False

# Font for UI
font = pygame.font.SysFont("Arial", 18)

running = True
camera_x, camera_y = 0, 0

while running:
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            # UI Toggles
            if event.key == pygame.K_c:
                game_state = "CRAFTING" if game_state == "PLAY" else "PLAY"
            if event.key == pygame.K_ESCAPE:
                game_state = "PLAY"
                
            # Hotbar Selection (1 and 2 keys)
            if event.key == pygame.K_1: active_slot_index = 0
            if event.key == pygame.K_2: active_slot_index = 1
                
            # Movement/Actions (Only when playing)
            if game_state == "PLAY":
                if event.key == pygame.K_SPACE and on_ground and not is_blocking:
                    velocity_y = jump_force
                    on_ground = False
                if event.key == pygame.K_b: # Block key
                    is_blocking = True
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_b:
                is_blocking = False
                
        # Mouse Clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "PLAY" and event.button == 1: # Left click
                active_item = hotbar[active_slot_index]
                if active_item in ["sword", "pickaxe"] and not is_blocking:
                    is_swinging = True
                    swing_timer = 0
                    current_swing_frame = 0

    keys = pygame.key.get_pressed()
    screen.fill((135, 206, 235)) # Sky blue

    # --- LOGIC (ONLY UPDATE IF PLAYING) ---
    if game_state == "PLAY":
        speed = player_run_speed if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) else player_walk_speed

        # Movement (Disabled if blocking)
        moving = False
        if not is_blocking:
            if keys[pygame.K_LEFT]:
                player_x -= speed
                moving, facing_left = True, True
            if keys[pygame.K_RIGHT]:
                player_x += speed
                moving, facing_left = True, False

        # Horizontal collision
        left_tile = get_tile_at(player_x + COLLISION_OFFSET_X, player_y + PLAYER_H // 2)
        right_tile = get_tile_at(player_x + PLAYER_W - COLLISION_OFFSET_X, player_y + PLAYER_H // 2)
        if left_tile != 0 and keys[pygame.K_LEFT]: player_x += speed
        if right_tile != 0 and keys[pygame.K_RIGHT]: player_x -= speed

        # Map boundary
        player_x = max(0, min(player_x, map_width - PLAYER_W))

        # Gravity & Vertical Collision
        velocity_y += gravity
        player_y += velocity_y

        head = player_y + 4
        if (get_tile_at(player_x + COLLISION_OFFSET_X, head) != 0 or get_tile_at(player_x + PLAYER_W - COLLISION_OFFSET_X, head) != 0) and velocity_y < 0:
            player_y = (int(head) // 32 + 1) * 32 - 4
            velocity_y = 0

        feet = player_y + IDLE_FEET_OFFSET
        if (get_tile_at(player_x + COLLISION_OFFSET_X, feet) != 0 or get_tile_at(player_x + PLAYER_W - COLLISION_OFFSET_X, feet) != 0) and velocity_y > 0:
            player_y = (int(feet) // 32) * 32 - IDLE_FEET_OFFSET
            velocity_y = 0
            on_ground = True
        else:
            on_ground = False

        if player_y + IDLE_FEET_OFFSET > map_height:
            player_y = map_height - IDLE_FEET_OFFSET
            velocity_y, on_ground = 0, True

        # Camera
        camera_x = max(0, min(int(player_x - SCREEN_WIDTH // 2.3), map_width - SCREEN_WIDTH))
        camera_y = max(0, min(int(player_y - SCREEN_HEIGHT // 2), map_height - SCREEN_HEIGHT))

        # Mining Interaction
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        world_mouse_x, world_mouse_y = mouse_x + camera_x, mouse_y + camera_y
        tile_col, tile_row = int(world_mouse_x) // 32, int(world_mouse_y) // 32
        
        dist = ((world_mouse_x - (player_x + PLAYER_W//2))**2 + (world_mouse_y - (player_y + PLAYER_H//2))**2)**0.5

        if mouse_buttons[0] and dist <= MINE_REACH and hotbar[active_slot_index] == "pickaxe" and not is_blocking:
            if 0 <= tile_row < len(grid) and 0 <= tile_col < len(grid[tile_row]):
                tile_val = grid[tile_row][tile_col]
                if tile_val != 0:
                    # If it's a chest, open it instead of mining it (Right Click usually better, using left for now)
                    if tile_val == 8:
                        game_state = "CHEST"
                        active_chest_pos = (tile_col, tile_row)
                    else:
                        if mining_target == (tile_col, tile_row):
                            mining_progress += 1
                            if mining_progress >= MINE_TIMES.get(tile_val, 120):
                                grid[tile_row][tile_col] = 0 # Break block
                                # Add to inventory pseudo-logic
                                if tile_val == 6: inventory["coal"] += 1
                                elif tile_val == 7: inventory["cloud"] += 1
                                mining_target, mining_progress = None, 0
                        else:
                            mining_target, mining_progress = (tile_col, tile_row), 0
        else:
            mining_target, mining_progress = None, 0

        # Animation updates
        if moving != was_moving: frame_index, animation_timer = 0, 0
        was_moving = moving
        animation_timer += 1
        if animation_timer >= animation_speed:
            animation_timer = 0
            frame_index = (frame_index + 1) % (len(walk_frames) if moving else len(idle_frames))

        if is_swinging:
            swing_timer += 1
            if swing_timer > 3: # Speed of swing
                swing_timer = 0
                current_swing_frame += 1
                if current_swing_frame >= 5:
                    is_swinging = False

    # --- DRAWING ---
    # Draw Tiles (Optimized Culling)
    start_col = max(0, camera_x // 32)
    end_col = min(len(grid[0]), (camera_x + SCREEN_WIDTH) // 32 + 1) if grid else 0
    start_row = max(0, camera_y // 32)
    end_row = min(len(grid), (camera_y + SCREEN_HEIGHT) // 32 + 1)

    for ri in range(start_row, end_row):
        for ci in range(start_col, end_col):
            val = grid[ri][ci]
            if val in TILE_DICT:
                screen.blit(TILE_DICT[val], (ci * 32 - camera_x, ri * 32 - camera_y))

    # Draw Player
    if is_blocking:
        # TODO: Replace with your friend's block frame
        player_frame = idle_frames[0].copy()
        player_frame.fill((255,0,0, 128), special_flags=pygame.BLEND_RGBA_MULT) # Red tint to show block
    else:
        player_frame = walk_frames[frame_index] if moving else idle_frames[frame_index]
        
    if facing_left: player_frame = pygame.transform.flip(player_frame, True, False)
    
    screen.blit(player_frame, (player_x - camera_x, player_y - camera_y))

    # Draw Tool/Swing
    if is_swinging:
        swing_img = swing_frames[current_swing_frame]
        if facing_left:
            swing_img = pygame.transform.flip(swing_img, True, False)
            screen.blit(swing_img, (player_x - camera_x - 20, player_y - camera_y - 10))
        else:
            screen.blit(swing_img, (player_x - camera_x + 10, player_y - camera_y - 10))

    # Draw Mining Progress
    if mining_target is not None and game_state == "PLAY":
        tc, tr = mining_target
        if grid[tr][tc] != 0:
            bar_x, bar_y = player_x - camera_x, player_y - camera_y - 12
            pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, 32, 6))
            pygame.draw.rect(screen, (255, 200, 0), (bar_x, bar_y, int((mining_progress / MINE_TIMES.get(grid[tr][tc], 120)) * 32), 6))

    # --- UI DRAWING ---
    # Regular UI (Hotbar & Inventory)
    pygame.draw.rect(screen, (40, 40, 40), (10, 10, 200, 40))
    hotbar_text = font.render(f"Equipped: {hotbar[active_slot_index]}", True, (255, 255, 255))
    screen.blit(hotbar_text, (20, 20))

    inv_y = 60
    for item, count in inventory.items():
        inv_text = font.render(f"{item.capitalize()}: {count}", True, (200, 200, 200))
        screen.blit(inv_text, (10, inv_y))
        inv_y += 20

    # Crafting UI Overlay
    if game_state == "CRAFTING":
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        pygame.draw.rect(screen, (100, 100, 100), (200, 100, 400, 400), border_radius=10)
        title = font.render("Crafting Menu (Press 'C' to close)", True, (255, 255, 255))
        screen.blit(title, (220, 120))
        # Add your crafting recipe drawing logic here later!

    # Chest UI Overlay
    if game_state == "CHEST":
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        pygame.draw.rect(screen, (139, 69, 19), (200, 100, 400, 400), border_radius=10)
        title = font.render("Chest Contents (Press ESC to close)", True, (255, 255, 255))
        screen.blit(title, (220, 120))
        # Add logic to move items between inventory dictionary and chest_data here!

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()