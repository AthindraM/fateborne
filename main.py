import os
import sys
from entities import *
from revolver import *

# Game Functions
def clear_screen():
    os.system("cls" if  os.name == "nt" else "clear")

def game_over(reason = "You have perished..."):
    print(f"\n{reason}")
    sys.exit()

# Player Creation
player = Fated()

##### GAME START #####
clear_screen()
print('"O Hunter, heed my call. Rid this world of its evil."\n')

while True:
    user_input = input('"Do you heed?" (Y/n): ').lower().strip()
    if user_input == "y":
        clear_screen()
        break
    elif user_input == "n":
        clear_screen()
        print('"Then this world is doomed..."')
        game_over("You have refused the call and let evil run free. GAME OVER")
    else:
        print('"Do you heed or not!"')

print("You awaken in a small damp room, lit by a single candle.")
print(
    "You can barely make out a body covered in clothes slumped on a chair. "
    "In front of you is a staircase leading up to a wooden door."
)

body_checked = False

while True:
    prompt = "Do you:\n"
    if not body_checked:
        prompt += "\t[1] Check out the body\n"
    prompt += "\t[2] Go up the stairs\n"

    user_input = int(input(prompt).strip())
    if user_input == 1 and not body_checked:
        print(
            "You get up and walk over to the body. "
            "As you reach over and barely touch the soft cloth, the body crumbles into ash, leaving a pile of clothes."
        )
        body_checked = True
        continue
    elif user_input == 2:
        print("You go up the stairs and open the door...")
        break
    else:
        print("Invalid input.\n")

print(
    "You come to the room of a house. "
    "There is a tiny fireplace and kitchen, and a table with one chair. There is also another wooden door which seems to lead outside.\n"
    "On the table you see a revolver and holster."
)

gun_taken = False

while True:
    prompt = "Do you:\n"
    if not gun_taken:
        prompt += "\t[1] Take the revolver and holster\n"
    prompt += "\t[2] Go out the door\n\t[3] Go back\n"

    user_input = int(input(prompt).strip())
    if user_input == 1 and not gun_taken:
        print("As you touch the revolver, you feel and electrifying sensation, and two glowing bullets materialize; one red and one yellow")
        gun_taken = True
        player.unlocked_bullets.append("damage")
        player.unlocked_bullets.append("heal")
        player.add_item("damage")
        player.add_item("heal")
        continue
    elif user_input == 2:
        clear_screen()
        print("You open the door, the bright sun nearly blinding you and you step onto lush grass...")
        break
    elif user_input == 3:
        print("You try to open the door behind you but it doesn't budge.")
        continue
    else:
        print("Invalid input.\n")

print("You take a deep breath of fresh air, when suddenly you're confronted with a large gelatinous slime!")
slime = Slime("Slime", 1)
player.in_combat = True

if not gun_taken:
    print("You have no weapon to fight the slime.")
    game_over()

while player.in_combat:

    if player.hp == 0:
        game_over("You have perished.")
    elif slime.hp == 0:
        player.in_combat = False
        print("You defeated the slime!")
        player.experience += 10
        break

    Entity.show_battle_comparison(player, slime)
    choice = int(input("[1] Shoot [2] Load [3] Spin\n").strip())

    if choice == 1:
        shoot(player, slime)
    elif choice == 2:
        load_revolver(player)
    elif choice == 3:
        spin(player)
    else:
        print("Invalid input.\n")


