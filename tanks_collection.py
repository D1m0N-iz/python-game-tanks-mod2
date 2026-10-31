from random import randint
from tank import tank
import world

_tanks = []
_canvas = None

def initialize(canvas):
    global _canvas
    _canvas = canvas
    player = tank(canvas=canvas, x=100, y=50,speed=1) # Танк игрока
    enemy = tank(canvas=canvas, x=500, y=150,speed=1) # Танк врага
    enemy.set_target(player)
    _tanks.append(player)
    _tanks.append(enemy)

def get_player():
    return _tanks[0]

def update():
    for tank in _tanks:
        tank.update()
        check_collision(tank)

def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersects(other_tank):
            return    

def spawn_enemy():
    pos_x = randint(200,world.WIDTH - 200)
    pos_y = randint(200,world.HEIGHT - 200)
    t = tank(_canvas, pos_x,pos_y)
    t.set_target(get_player)
    _tanks.append(t)