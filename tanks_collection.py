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