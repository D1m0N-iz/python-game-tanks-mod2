import tkinter as tk
from tank import tank
from hitbox import Hitbox

hb1 = Hitbox(10,10,100,100)
wid = hb1.get_widht
hb1.set_width(wid * 2)
print(hb1.get_widht())

# Коды клавиш
KEY_W_1, KEY_A_1, KEY_S_1, KEY_D_1 = 87, 65, 83, 68 # Кодировка ASCII
KEY_W_2, KEY_A_2, KEY_S_2, KEY_D_2 = 25, 38, 39, 40 # Кодировка Linux

def key_press(event):
    if event.keycode == KEY_W_1 or event.keycode == KEY_W_2:
        player.forward()
    elif event.keycode == KEY_A_1 or event.keycode == KEY_A_2:
        player.left()
    elif event.keycode == KEY_S_1 or event.keycode == KEY_S_2:
        player.backward()
    elif event.keycode == KEY_D_1 or event.keycode == KEY_D_2:
        player.right()
    print(player)

w = tk.Tk() # Создаем объект окна
w.title('Танки на минималках 2.0') # Заголовок окна
canvas = tk.Canvas(w, width=800, height=600, bg="#6A6A6A") # Создаем холст в окне
canvas.pack() # Располагаем холст в окне

player = tank(canvas=canvas, x=100, y=50) # Танк игрока
enemy = tank(canvas=canvas, x=500, y=150) # Танк врага

w.bind('<KeyPress>', key_press)

w.mainloop()

# t1 = tank(x=0,y=0)

# t2 = tank(x=100,y=200,model='tiger',ammo=25,)

# t2.forward()
# t2.forward()
# t2.right()
# t2.fire()


# print (t1.ammo)
# t1.fire()
# print (t1.ammo)

# print (tank.count)

# for t in[t1,t2]:
#     print(t.model)

