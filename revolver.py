import random
from fated import Fated

barrel = [0, 0, 0, 0, 0, 0]

bullet_types = {
    0: "blank",
    1: "damage",
    2: "heal"
}

def generate_bullet(num):
    regen_num = random.randint(1,num)
    return regen_num

#TODO: write load()
def load_revolver(inventory):
    availible_bullets = 0
    availible_damage_bullets = 0
    availible_heal_bullets = 0

    for item in inventory:
        if item == "damage":
            availible_bullets += 1
            availible_damage_bullets += 1
        elif item == "heal":
            availible_bullets += 1
            availible_heal_bullets += 1

    print(f"You have {availible_bullets} bullets: {availible_damage_bullets} damage and {availible_heal_bullets} heal")
    for i in range(1, len(barrel)): #BUG: elif statement repeats instead of breaking
        while True:
            if i <= len(barrel) and i <= availible_bullets:
                bullet = input("What type of bullet would you like to load?").lower().strip
            elif i > len(barrel) or i > availible_bullets:
                print("You don't have any more bullets to load.")
                break
            else:
                print("Invalid input")
            break

def spin():
    rand_num = random.randint(1, len(barrel))

    for _ in range(rand_num):
        first = barrel.pop(0)
        barrel.append(first)

    num_unlocked_bullets = len(Fated().unlocked_bullets) 

    Fated().inventory.append(generate_bullet(num_unlocked_bullets))

def shoot():
    global barrel
    bullet = barrel.pop(0)
    barrel.append(0)

    bullet_type = bullet_types.get(bullet, "unknown")
    print(f"You fired a {bullet_type} bullet!")

    if bullet_type == "blank":
        print("Nothing happens...")
    elif bullet_type == "damage":
        print("You deal damage to your target!")
    elif bullet_type == "heal":
        print("You heal your target!")

    return bullet_type
