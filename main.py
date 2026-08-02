import tkinter as tk
from tank import tank

# Коды клавиш
KEY_W, KEY_A, KEY_S, KEY_D = 87, 65, 83, 68

def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_S:
            player.backward()
    elif event.keycode == KEY_D:
                player.right()

w = tk.Tk()
w.title('танчики 2.0')
canvas = tk.Canvas(w,width=800,height=600, bg='#6a6a6a')
canvas.pack()

player = tank(canvas=canvas,x=100,y=50)
anemy = tank(canvas=canvas,x=500,y=150)

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

