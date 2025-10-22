class Fated:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.inventory = []
        self.lvl = 1
        self.experience = 0
        self.max_exp = 100 * self.lvl

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
    
    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def add_item(self, item):
        self.inventory.append(item)

    def show_stats(self):
        print("\n--- Stats ---")
        print(f"Level: {self.lvl}\tEXP: {self.experience}/{self.max_exp}")
        print(f"HP: {self.hp}/{self.max_hp}")

    def show_inventory(self):
        print("\n--- Inventory ---")
        print(self.inventory)

