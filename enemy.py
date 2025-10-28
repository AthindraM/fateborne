class Enemy:
    def __init__(self, level):
        self.hp = 50
        self.maxhp = 50
        self.level = level
        self.experience = 10 * self.level
        self.drops = []

    def attack(self): #NOTE: prototype 
        return 1;

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp
