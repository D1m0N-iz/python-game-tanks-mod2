class tank:
    count = 0
    SIZE = 100

    def __init__(self,canvas,x,y,ammo = 30,model = 'ис 2',speed=10):
        tank.count += 1
        self.canvas = canvas
        self.model = model
        self.fuel = 1000
        self.hp = 100
        self.xp = 0
        self.ammo = ammo
        self.speed = speed

        self.x = x
        self.y = y

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

        self.create()


    def __str__(self):
        return f'x={self.x},y={self.y},ammo={self.ammo}'

    def create(self):
        self.id = self.canvas.create_rectangle(self.x,self.y,self.x + tank.SIZE,self.y + tank.SIZE)

    def repaint(self):
        self.canvas.moveto(self.id, x=self.x, y=self.y)

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
            self.repaint()

    def backward(self):
        if self.fuel > 0:
            self.y += 1
            self.fuel -= 1
            self.repaint()

    def left(self):
        if self.fuel > 0:
           self.x -= 1
           self.fuel -=1
           self.repaint()
                
    def right(self):
        if self.fuel > 0:
            self.x += 1
            self.fuel -= 1
            self.repaint()