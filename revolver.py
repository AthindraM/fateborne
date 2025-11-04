import random

barrel = [0, 0, 0, 0, 0, 0]

bullet_types = {
    0: "blank",
    1: "damage",
    2: "heal"
}

def load_revolver(fated):
    available_bullets = 0
    available_damage_bullets = 0
    available_heal_bullets = 0

    for item in fated.inventory:
        if item == "damage":
            available_bullets += 1
            available_damage_bullets += 1
        elif item == "heal":
            available_bullets += 1
            available_heal_bullets += 1

    print(f"You have {available_bullets} bullets: {available_damage_bullets} damage and {available_heal_bullets} heal")
    
    empty_chambers = barrel.count(0)
    if empty_chambers == 0:
        print("You can't load any more bullets.")
        return
    elif available_bullets == 0:
        print("You don't have any bullets to load.")
        return

    while empty_chambers > 0 and available_bullets > 0:
        bullet = input("What type of bullet would you like to load?\n\t[1] Damage\n\t[2] Heal\n\t[D]one").lower().strip()

        if bullet == "done" or bullet == "d":
            break
        elif bullet == "1" or bullet == "damage":
            if available_damage_bullets > 0:
                for i in range(len(barrel)):
                    if barrel[i] == 0:
                        barrel[i] = 1
                        break
                fated.inventory.remove("damage")
                available_bullets -= 1
                available_damage_bullets -= 1
                empty_chambers -= 1
                print("Loaded damage bullet!")
            else:
                print("You don't have any damage bullets!")
        elif bullet == "2" or bullet == "heal":
            if available_heal_bullets > 0:
                for i in range(len(barrel)):
                    if barrel[i] == 0:
                        barrel[i] = 2
                        break
                fated.inventory.remove("heal")
                available_bullets -= 1
                available_heal_bullets -= 1
                empty_chambers -= 1
                print("Loaded heal bullet!")
            else:
                print("You don't have any heal bullets!")
        else:
            print("Invalid input.")

        if available_bullets == 0:
            print("Revolver fully loaded!")
            break

def spin(fated):
    rand_num = random.randint(1, len(barrel))

    for _ in range(rand_num):
        first = barrel.pop(0)
        barrel.append(first)

    num_unlocked_bullets = len(fated.unlocked_bullets)
    fated.inventory.append(random.randint(1,num_unlocked_bullets)) #generates a bullet and adds it to the inventory  

def shoot(fated, enemy):
    global barrel

    while True:
        target = int(input("Who would you like to target?\n\t[1] Yourself\n\t[2] Enemy\n").strip())
        if target in [1,2]:
            break
        print("Invalid choice!")

    bullet = barrel.pop(0)
    barrel.append(0)

    bullet_type = bullet_types.get(bullet, "unknown")
    print(f"You fired a {bullet_type} bullet!")

    if bullet_type == "blank":
        print("Nothing happens...")
    elif bullet_type == "damage":
        damage_amount = 2
        if target == 1:
            fated.take_damage(damage_amount)
            print(f"You shoot yourself for {damage_amount} damage! (HP: {fated.hp}/{fated.max_hp})")
        else:
            enemy.take_damage(damage_amount)
            print(f"You deal {damage_amount} damage to {enemy.name}! (HP: {enemy.hp}/{enemy.max_hp})")
    elif bullet_type == "heal":
        heal_amount = 2
        if target == 1:
            fated.heal(heal_amount)
            print(f"You heal yourself for {heal_amount} HP! (HP: {fated.hp}/{fated.max_hp})")
        else:  # target == "2", heal enemy
            enemy.heal(heal_amount)
            print(f"You heal {enemy.name} for {heal_amount} HP! (HP: {enemy.hp}/{enemy.max_hp})")

    return bullet_type
