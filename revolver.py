import random
from entities import *

barrel = [0, 0, 0, 0, 0, 0]

bullet_types = {
    0: "blank",
    1: "damage",
    2: "heal"
}

def load_revolver(fated):
    availible_bullets = 0
    availible_damage_bullets = 0
    availible_heal_bullets = 0

    for item in fated.inventory:
        if item == "damage":
            availible_bullets += 1
            availible_damage_bullets += 1
        elif item == "heal":
            availible_bullets += 1
            availible_heal_bullets += 1

    print(f"You have {availible_bullets} bullets: {availible_damage_bullets} damage and {availible_heal_bullets} heal")
    
    empty_chambers = barrel.count(0)
    if empty_chambers == 0:
        print("You can't load any more bullets.")
        return
    elif availible_bullets == 0:
        print("You don't have any bullets to load.")
        return

    while empty_chambers > 0 and availible_bullets > 0:
        bullet = input("What type of bullet would you like to load?\n\t[1] Damage\n\t[2] Heal\n\t[D]one").lower().strip()

        if bullet == "done" or bullet == "d":
            break
        elif bullet == "1" or bullet == "damage":
            if availible_damage_bullets > 0:
                for i in range(len(barrel)):
                    if barrel[i] == 0:
                        barrel[i] = 1
                        break
                fated.inventory.remove("damage")
                availible_bullets -= 1
                availible_damage_bullets -= 1
                empty_chambers -= 1
                print("Loaded damage bullet!")
            else:
                print("You don't have any damage bullets!")
        elif bullet == "2" or bullet == "heal":
            if availible_heal_bullets > 0:
                for i in range(len(barrel)):
                    if barrel[i] == 0:
                        barrel[i] = 2
                        break
                fated.inventory.remove("heal")
                availible_bullets -= 1
                availible_heal_bullets -= 1
                empty_chambers -= 1
                print("Loaded heal bullet!")
            else:
                print("You don't have any heal bullets!")
        else:
            print("Invalid input.")

        if availible_bullets == 0:
            print("Revolver fully loaded!")
            break

def spin(fated):
    rand_num = random.randint(1, len(barrel))

    for _ in range(rand_num):
        first = barrel.pop(0)
        barrel.append(first)

    num_unlocked_bullets = len(Fated().unlocked_bullets) 
    fated.inventory.append(random.randint(1,num_unlocked_bullets)) #generates a bullet and adds it to the inventory  

def shoot():
    global barrel
    bullet = barrel.pop(0)
    barrel.append(0)

    #TODO: give player choice of who to target

    bullet_type = bullet_types.get(bullet, "unknown")
    print(f"You fired a {bullet_type} bullet!")

    if bullet_type == "blank":
        print("Nothing happens...")
    elif bullet_type == "damage":
        print("You deal damage to your target!")
    elif bullet_type == "heal":
        print("You heal your target!")

    return bullet_type
