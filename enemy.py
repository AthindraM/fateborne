class Enemy:
    def __init__(self, level):
        self.hp = 50
        self.maxhp = 50
        self.level = level
        self.experience = 10 * self.level
        self.drops = []
