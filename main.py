import tkinter as tk
from tank import tank
from hitbox import Hitbox
import world

hb1 = Hitbox(x=0,y=0,width=100,height=100)
hb2 = Hitbox(x=50,y=50,width=100,height=100)
hb3 = Hitbox(170,50,50,50)

# print(hb1.intersects(hb2))
# print(hb1.intersects(hb3))
# print(hb2.intersects(hb3))

# Коды клавиш
KEY_W_1, KEY_A_1, KEY_S_1, KEY_D_1 = 87, 65, 83, 68 # Кодировка ASCII
KEY_W_2, KEY_A_2, KEY_S_2, KEY_D_2 = 25, 38, 39, 40 # Кодировка Linux
KEY_CTRL_L = 17

FPS = 60

def update():
    player.update()
    enemy.update()
    check_colision()

    w.after(1000//FPS,update)

def key_press(event):
    if event.keycode == KEY_W_1 or event.keycode == KEY_W_2:
        player.forward()
    elif event.keycode == KEY_A_1 or event.keycode == KEY_A_2:
        player.left()
    elif event.keycode == KEY_S_1 or event.keycode == KEY_S_2:
        player.backward()
    elif event.keycode == KEY_D_1 or event.keycode == KEY_D_2:
        player.right()
    elif event.keycode == KEY_CTRL_L:
        player.stop()

def check_colision():

    player.intersects(enemy)
    enemy.intersects(player)

    if player.intersects(enemy):
        #print('танки столкнулись')
        player.undo_move()
    if enemy.intersects(player):
        enemy.undo_move()

w = tk.Tk() # Создаем объект окна
w.title('Танки на минималках 2.0') # Заголовок окна
canvas = tk.Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg="#6A6A6A") # Создаем холст в окне
canvas.pack() # Располагаем холст в окне

player = tank(canvas=canvas, x=100, y=50,speed=1) # Танк игрока

enemy = tank(canvas=canvas, x=500, y=150,speed=1) # Танк врага
enemy.set_target(player)

enemy = tank(canvas=canvas, x=500, y=150) # Танк врага


w.bind('<KeyPress>', key_press)

update()

w.mainloop()