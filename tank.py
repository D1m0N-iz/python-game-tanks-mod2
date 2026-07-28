class tank:
    def __init__(self,x,y,fuel,hp,ammo = 30,model = 'ис 2'):
        self.model = self.model
        self.fuel = 100
        self.hp = 100
        self.xp = 0
        self.ammo = ammo

        self.x = x
        self.y = y

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0