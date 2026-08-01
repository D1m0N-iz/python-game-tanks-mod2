class tank:
    count = 0
    def __init__(self,x,y,ammo = 30,model = 'ис 2'):
        tank.count += 1
        self.model = model
        self.fuel = 1000
        self.hp = 100
        self.xp = 0
        self.ammo = ammo

        self.x = x
        self.y = y

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

    def __str__(self):
        return f'x={self.x},y={self.y},ammo={self.ammo}'

    def show_info(self):
        print(f'x={self.x},y={self.y},ammo={self.ammo}',)

    def fire(self):
        if self.ammo > 0:
            self.ammo -= 1
            print('выстрел!!!')
    def forward(self):
        if self.fuel > 0:
            self.y -= 1
            self.fuel -=1

    def backward(self):
        if self.fuel > 0:
            self.y += 1
            self.fuel -= 1

    def left(self):
        if self.fuel > 0:
         self.x -= 1
         self.fuel -=1
                
    def right(self):
        if self.fuel > 0:
            self.x += 1
            self.fuel -= 1