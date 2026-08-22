from tkinter import PhotoImage
from hitbox import Hitbox

class tank:
    count = 0
    SIZE = 100

    def __init__(self, canvas, x, y, model='ИС-2', ammo=30, speed=12,
                 file_up = './img/tank_up.png'
                  file_down = './img/tank_down.png',
                  file_left = './img/tank_left.png',
                  file_right = './img/tank_right.png'):
        tank.count += 1
        self.__hitbox = Hitbox(x,y,self.get_size)
        self.canvas = canvas
        self.model = model
        self.fuel = 1000 # Запас топлива
        self.hp = 100
        self.xp = 0
        self.ammo = ammo
        self.speed = speed

        self.__x = x
        self.__y = y

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

        self.skin_up = PhotoImage(file=file_up)
        self.skin_down = PhotoImage(file=file_down)
        self.skin_left = PhotoImage(file=file_left)
        self.skin_right = PhotoImage(file=file_right)

        self.__create()

    def __str__(self):
        return f'x={self.x} y={self.y} ammo={self.ammo}'

    def __create(self): # Метод отрисовки квадрата танка
        #self.id = self.canvas.create_rectangle(self.x, self.y, self.x + tank.SIZE, self.y + tank.SIZE)
        self.__id = self.canvas.create_image(self.__x,self.__y,image=self.__skin_up,ancor='nw')
    
    def __repaint(self): # Метод перерисовки танка
        self.canvas.moveto(self.id, x=self.x, y=self.y)

    def show_info(self):
        print(f'x={self.x},y={self.y},ammo={self.ammo}',)

    def fire(self):
        if self.ammo > 0:
            self.ammo -= 1
            print('выстрел!!!')

    def forward(self):
        if self.fuel > 0:
            self.y -= self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.__canvas.itemconfig(self.__id,image=self.skin_up)
            self.__repaint()

    def backward(self):
        if self.fuel > 0:
            self.y += self.speed
            self.fuel -= 1
            self.__canvas.itemconfig(self.__id,image=self.skin_down)
            self.__repaint()

    def left(self):
        if self.fuel > 0:
            self.x -= self.speed
            self.fuel -= 1
            self.__canvas.itemconfig(self.__id,image=self.skin_left)
            self.__repaint()

    def right(self):
        if self.fuel > 0:
            self.x += self.speed
            self.fuel -= 1
            self.__canvas.itemconfig(self.__id,image=self.skin_right)
            self.__repaint()

    def __update_hitbox(self):
        self.__hitbox.moveto(self.x,self.y)

    def intersects(self,other_tank):
        return self.__hitbox.intersects(other_tank._hitbox)
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_model(self):
        return self.__model
    
    def get_fuel(self):
        return self.__fuel
    
    def get_hp(self):
        return self.__hp
    
    def get_xp(self):
        return self.__xp
    
    def get_ammo(self):
        return self.__ammo
    
    def get_speed(self):
        return self.__speed
    
    def get_size(self):
        return self.__skin_up.width()
    
    @staticmethod
    def get_quantity():
        return Tank.count
