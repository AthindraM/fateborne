# Base Entity Class
class Entity:
    def __init__(self, hp, level=1):
        self.hp = hp
        self.max_hp = hp
        self.level = level
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
    
    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

# Player Class
class Fated(Entity):
    def __init__(self):
        super().__init__(hp=10, level=1)
        self.inventory = []
        self.experience = 0
        self.max_experience = 100 * self.level
        self.unlocked_bullets = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_stats(self):
        print("\n--- Stats ---")
        print(f"Level: {self.level}\tEXP: {self.experience}/{self.max_experience}")
        print(f"HP: {self.hp}/{self.max_hp}")

    def show_inventory(self):
        print("\n--- Inventory ---")
        print(self.inventory)

# Base Enemy Class
class Enemy(Entity):
    def __init__(self, level, hp):
        super().__init__(hp=hp, level=level)
        self.boss = False
        self.experience = 10 * self.level
        self.drops = []

    def attack(self):  # NOTE: prototype 
        return 1

class Slime(Enemy):
    def __init__(self, level):
        super().__init__(level, hp=10)
        
