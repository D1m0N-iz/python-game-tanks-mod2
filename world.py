def set_camera_xy(x,y):
    global _change_x,_camera_y
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x + SCREEN_WIDTH > WIDTH:
        x = WIDTH - SCREEN_WIDTH
    if y + SCREEN_HEIGHT > HEIGHT:
        y = HEIGHT - SCREEN_HEIGHT
    _change_x = x
    _camera_y = y

    def move_camera(delta_x,delta_y):
        set_camera_xy(_change_x + delta_x,_camera_y + delta_y)

    def get_screen_x(world_x):
        return world_x - _change_x

    def get_screen(world_y):
        return world_y - _camera_y

_change_x = _camera_y = 0
SCREEN_WIDTH, SCREEN_HEIGHT = 800,600

WIDTH = SCREEN_WIDTH * 6
HEIGHT = SCREEN_HEIGHT * 4