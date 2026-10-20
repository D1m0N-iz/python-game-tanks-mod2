from tkinter import PhotoImage
from hitbox import Hitbox

from random import randint

class tank:
    count = 0
    SIZE = 100

    def __init__(self,bot canvas, x, y, model='ИС-2', ammo=30, speed=1,
                 file_up = './img/tank_up.png',
                  file_down = './img/tank_down.png',
                  file_left = './img/tank_left.png',
                  file_right = './img/tank_right.png',
                  bot = True):
        tank.count += 1
        self.__bot = bot
        self.__target = None
        self.__canvas = canavas
        self.__model = model
        self.__fuel = 10000 # Запас топлива
        self.__hp = 100
        self.__xp = 0
        self.__mmo = ammo
        self.__speed = speed

        self.__vx = 0
        self.__vy = 0
        self.dx = 0
        self.dy = 0

        self.__x = x
        self.__y = y

        if tank.x < 0:
            tank.x = 0
        if tank.y < 0:
            tank.y = 0

        self.skin_up = PhotoImage(file=file_up)
        self.skin_down = PhotoImage(file=file_down)
        self.skin_left = PhotoImage(file=file_left)
        self.skin_right = PhotoImage(file=file_right)

        self.__hitbox = Hitbox(x,y,self.get_size(),self.get_size(),padding=8)

        self.__create()

    def __str__(self):
        return f'x={self.x} y={self.y} ammo={self.ammo}'

    def __create(self): # Метод отрисовки квадрата танка
        self.__id = self.canvas.create_image(self.__x,self.__y,image=self.__skin_up,ancor='nw')
    
    def show_info(self):
        print(f'x={self.x},y={self.y},ammo={self.ammo}',)

    def __repaint(self): # Метод перерисовки танка
        self.canvas.moveto(self.id,
                            x=world_get_screen_x(self._x),
                            y=world_get_screen_y(self._y)

    def AI(self):
        if randint(1,30) == 1:

            if self.__taerget is not None and randint(1,10) < 9:
                self._AI_goto_target()
            self.AI_change_orientation()

            self.AI_change_orientation

    def AI_change_orientation(self):
        rand = randint(0-3)
        match rand:
            case 0:self.left()
            case 1:self.farward()
            case 2:self.right()
            case 3:self.backward()

    def __AI_goto_target(self):
        if randint(1,2)==1:
            if self.__target.get_x() < self.get_x():
                self.left()
            else:
                self.right()
        else:
            if self.__target.get_y() < self.get_y():
                self.forward
            else:
                self.backward()

    def update(self):
        if self.__fuel >= self.__speed:
            if self.__bot:
                self.__AI()
            if self.vx == 0 and self.vy == 0:
                return
            self.__dx  = self.__vx + self.__speed
            self.__dy  = self.__vy + self.__speed
            self.__fuel -= self.__speed
            self.__x += self.__dx
            self.__y += self.__dy
            self.__update_hitbox()
            self.__check_out_of_world()
            self.__repaint()

    def __check_out_of_world(self):
        if self.__hitbox.left < 0 or \
                self.__hitbox.top < 0 or \
                self.__hitbox.right > world.WIDTH or \
                self.__hitbox.bottom >world.HEIGHT:
            self.__undo_move()
            if self.bot:
                self.AI_change_orientation() 

    def __undo_move(self):
        if self.__dx == 0 and self.__dy == 0 :
            return
        
        self.__x -=self.__dx
        self.__y -=self.__dy
        self.__fuel += self.__speed
        self.__update_hitbox()
        self.__repaint()

        self.__dx = self.dy = 2
   
    def fire(self):
        if self.ammo > 0:
            self.ammo -= 1
            print('выстрел!!!')

    def forward(self):
        self.__vx = 0
        self.__vy = -1
        self.canavas.itemconfig(self.__id,image = self.__skin_up)

        
    def backward(self):
        self.__vx = 0
        self.__vy = 1
        self.canavas.itemconfig(self.__id,image = self.__skin_down)

    def left(self):
        self.__vx = 0
        self.__vy = -1
        self.canavas.itemconfig(self.__id,image = self.__skin_left)

    def right(self):
        self.__vx = 0
        self.__vy = 1
        self.canavas.itemconfig(self.__id,image = self.__skin_right)

    def stop(self):
        self.__vx = self.__vy = 0

    def __update_hitbox(self):
        self.__hitbox.moveto(self.x,self.y)

    def intersects(self,other_tank):
        value = self.__hitbox.intersects(other_tank._hitbox)
        if value:
            self.__undo_move
            if self.__bot:
                self.AI_change_orientation()
        return value
    
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

    def set set_target(self,target):
        self.__target = target

