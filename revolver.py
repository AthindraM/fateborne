import random

barrel = [0, 0, 0, 0, 0, 0]

bullet_types = {
    0: "blank",
    1: "damage",
    2: "heal"
}

def spin():
    rand_num = random.randint(1, len(barrel))

    for _ in range(rand_num):
        first = barrel.pop(0)
        barrel.append(first)

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
