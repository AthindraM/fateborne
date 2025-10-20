print('"O Hunter, heed my call. Rid this world of its evil."\n')

while True:
    userInput = input('"Do you heed?" (Y/n): ').lower().strip()
    if userInput == "y":
        break
    elif userInput == "n":
        print('"Then this world is doomed..."')
        break
    else:
        print('"Do you heed or not!"')

for i in range(5):
    print("...\n")

print("You awaken in a small damp room, lit by a single candle.")
print(
    "You can barely make out a body covered in clothes slumped on a chair. "
    "In front of you is a staircase leading up to a wooden door."
)

bodyChecked = False

while True:
    prompt = "Do you:\n"
    if not bodyChecked:
        prompt += "\t[1] Check out the body\n"
    prompt += "\t[2] Go up the stairs\n"

    userInput = int(input(prompt).strip())
    if userInput == 1 and not bodyChecked:
        print(
            "You get up and walk over to the body. "
            "As you reach over and barely touch the soft cloth, the body crumbles into ash, leaving a pile of clothes."
        )
        bodyChecked = True
        continue
    elif userInput == 2:
        print("You go up the stairs and open the door...")
        break
    else:
        print("Invalid input.\n")

print(
    "You come to the room of a house. "
    "There is a tiny fireplace and kitchen, and a table with one chair. "
    "On the table you see a revolver."
)
