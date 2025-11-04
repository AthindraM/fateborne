# Base Entity Class
class Entity:
    def __init__(self, name, hp, level=1):
        self.name = name
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

    @staticmethod
    def show_battle_comparison(player, enemy):
        """Show player and enemy stats side by side"""

        def draw_health_bar(current_hp, max_hp, bar_length=10):
            filled = int((current_hp / max_hp) * bar_length)
            empty = bar_length - filled
            return "[" + "█" * filled + "░" * empty + "]"

        print("\n╔" + "═" * 28 + "╦" + "═" * 28 + "╗")
        print("║" + f"  {player.name} (YOU)".ljust(28) + "║" + f"  {enemy.name}".ljust(28) + "║")
        print("╠" + "═" * 28 + "╬" + "═" * 28 + "╣")

        # HP text
        player_hp_text = f"  HP: {player.hp}/{player.max_hp}"
        enemy_hp_text = f"  HP: {enemy.hp}/{enemy.max_hp}"
        print("║" + player_hp_text.ljust(28) + "║" + enemy_hp_text.ljust(28) + "║")

        # Health bars with brackets included in draw function
        player_bar = draw_health_bar(player.hp, player.max_hp)
        enemy_bar = draw_health_bar(enemy.hp, enemy.max_hp)

        # Manual spacing calculation (brackets are part of bar now)
        player_bar_line = "  " + player_bar + " " * (26 - len(player_bar))
        enemy_bar_line = "  " + enemy_bar + " " * (26 - len(enemy_bar))
        print("║" + player_bar_line + "║" + enemy_bar_line + "║")

        # Level
        print("║" + f"  Level: {player.level}".ljust(28) + "║" + f"  Level: {enemy.level}".ljust(28) + "║")
        print("╚" + "═" * 28 + "╩" + "═" * 28 + "╝\n")

# Player Class
class Fated(Entity):
    def __init__(self):
        super().__init__(name="Fated", hp=10, level=1)
        self.inventory = []
        self.experience = 0
        self.max_experience = 100 * self.level
        self.unlocked_bullets = []
        self.in_combat = False

    def add_item(self, item):
        self.inventory.append(item)

    def show_adventure_stats(self):
        print("\n--- Stats ---")
        print(f"Level: {self.level}\tEXP: {self.experience}/{self.max_experience}")
        print(f"HP: {self.hp}/{self.max_hp}")

    def show_inventory(self):
        print("\n--- Inventory ---")
        print(self.inventory)

# Base Enemy Class
class Enemy(Entity):
    def __init__(self, name, level, hp):
        super().__init__(name=name, hp=hp, level=level)
        self.boss = False
        self.experience = 10 * self.level
        self.drops = []

    def attack(self):  # NOTE: prototype 
        return 1

class Slime(Enemy):
    def __init__(self, name, level):
        super().__init__(name=name, level=level, hp=10)
        
