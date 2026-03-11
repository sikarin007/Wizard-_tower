
screen_width = 1280
screen_height = 720
FPS = 60

player_speed = 5
player_jump_speed = 10
player_gravity = 0.5
player_jump_gravity = 0.1
player_jump_height = 100
player_jump_time = 0.5
player_jump_time_gravity = 0.01
player_jump_time_height = 100
player_jump_time_time = 0.5

# tower
TOWER_FRAME_WIDTH = 64
TOWER_FRAME_HEIGHT = 128    # แต่ละเฟรมมีขนาด 64x128 พิกเซล
TOWER_INIT_FRAMES = 6
TOWER_IDLE_FRAMES = 8
TOWER_POS = (screen_width // 2, screen_height // 2)
TOWER_HEALTH = 100
TOWER_HEALTH_BAR_LENGTH = TOWER_FRAME_WIDTH
TOWER_HEALTH_RATIO = TOWER_HEALTH / TOWER_HEALTH_BAR_LENGTH
TOWER_FRAME_DELAY = 6  # frames ต่อ 1 sprite frame


# enemy
ENEMY_SPEED = 2
ENEMY_FRAME_WIDTH = 32
ENEMY_FRAME_HEIGHT = 32
ENEMY_INIT_FRAMES = 6
ENEMY_IDLE_FRAMES = 8
ENEMY_POS = (screen_width // 2, screen_height // 2)
