import texture

def initialize(canvas):
    global _canvas,_map
    _canvas = canvas

    create_map(20,20)

def create_map(row=20,cals=20):
    global map

    # _map.append = _Cell(canvas,BRICK,0,0)
    # _map.append = _Cell(canvas,WATER,0,BLOCK_SIZE * 1)
    # _map.append = _Cell(canvas,CONCRETE,0,BLOCK_SIZE * 2)

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

WIDTH = SCREEN_WIDTH * 2
HEIGHT = SCREEN_HEIGHT * 2

GROUND = 'g'
WATER = 'w'
CONCRETE = 'c'
BRICK = 'b'
BLOCK_SIZE = 64

_canvas = None
_map = []

class _Cell:
    def __init__(self,canvas,block,x,y):
        self.__canvas__ = canvas
        self.__block = block
        self.__x = x
        self.__y = y

        self.__create_element(block)

    def __del__(self):
        try:
            self.__canvas.delete(self.__id)
        except Exception:
            pass

    def __create_element(self, block):
        if block != GROUND:
            self.__id = self.__canvas.create_image(
                self.__x, self.__y,
                image=texture.get(block), anchor='nw')

    def get_block(self):
        return self.__block