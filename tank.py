from hitbox import Hitbox

class tank:
    count = 0
    SIZE = 100

    def __init__(self, canvas, x, y, model='ИС-2', ammo=30, speed=12):
        tank.count += 1
        self.__hitbox = Hitbox(x,y,tank.SIZE,tank.SIZE)
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

        self.create()

    def __str__(self):
        return f'x={self.x} y={self.y} ammo={self.ammo}'

    def create(self): # Метод отрисовки квадрата танка
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + tank.SIZE, self.y + tank.SIZE)

    def repaint(self): # Метод перерисовки танка
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
            self.repaint()

    def backward(self):
        if self.fuel > 0:
            self.y += self.speed
            self.fuel -= 1
            self.repaint()

    def left(self):
        if self.fuel > 0:
            self.x -= self.speed
            self.fuel -= 1
            self.repaint()

    def right(self):
        if self.fuel > 0:
            self.x += self.speed
            self.fuel -= 1
            self.repaint()

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
    
    @staticmethod
    def get_quantity():
        return Tank.count
    
    @staticmethod
    def get_size():
        return Tank.SIZE