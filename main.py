import locations
import character


XP_PER_MOVE = 50


def print_title():
    print("=" * 80)
    print(f"{'Adventure Quest':^80}")
    print("=" * 80)


def draw_hud(name, row, col, level, strength):
    location_line = f"Location: {locations.location_name(row, col)} ({row}, {col})"

    stat_row = f"Name: {name}".ljust(22) + f"Health: {health}".ljust(24) + f"Strength: {strength}"
    info_row = f"Level: {level}".ljust(22) + f"Gold: {gold}".ljust(22) + f"Inventory: {', '.join(inventory)}"

    print("=" * 80)
    print(f"{'Adventure Quest':^80}")
    print(f"{location_line:^80}")
    print("=" * 80)
    print(("| " + stat_row).ljust(80) + "|")
    print(("| " + info_row).ljust(80) + "|")
    print("=" * 80)
    print("| Available Commands:".ljust(80) + "|")
    print("| - Move: north (n), south (s), east (e), west (w)".ljust(80) + "|")
    print("| - Actions: pick up (p), drop (d), use (u), talk (t)".ljust(80) + "|")
    print("| - Inventory: view inventory (i)".ljust(80) + "|")
    print("| - Save Game (save), Load Game (load), Quit (q)".ljust(80) + "|")
    print("=" * 80)


def show_inventory(inventory):
    print("=" * 80)
    print("| Inventory:".ljust(80) + "|")
    for item in inventory:
        print(("| - " + item).ljust(80) + "|")
    print("=" * 80)


print_title()
print("Welcome to Adventure Quest!")
print("")
print("In this mystical land, you will embark on a thrilling journey to find the Enchanted")
print("Castle, rescue allies, and rebuild communities. Along the way, you will encounter")
print("various challenges, meet different characters, and collect valuable resources.")
print("Good luck on your adventure!")
print("")


print("=" * 80)
print("| Main Menu:".ljust(80) + "|")
print("| 1. Start New Game".ljust(80) + "|")
print("| 2. Load Game".ljust(80) + "|")
print("| 3. Quit".ljust(80) + "|")
print("=" * 80)

menu_choice = input("Please select an option: ")


# ----- Week 5: route the menu choice -----

if menu_choice == "1":

    print_title()
    print("Create your Character!")
    print("")


    health = 100
    strength = 10
    level = 1
    gold = 0
    magic = 0
    xp = 0

    inventory = ["Food", "Water"]


    name = input("Enter your character's name: ")
    bonus = int(input("Choose a starting strength bonus (0-5): "))


    strength = strength + bonus
    attack_power = strength * 2 + level

    print(f"Character created! Name: {name}, Health: {health}, Strength: {strength}")
    print(f"Attack Power: {attack_power}")
    print("")


    row = 0
    col = 0

    location_count = len(locations.world) * len(locations.world[0])

    print("Initializing game world...")
    print("Row 0:", locations.world[0])
    print("Row 1:", locations.world[1])
    print("Row 2:", locations.world[2])
    print("Row 3:", locations.world[3])
    print("Row 4:", locations.world[4])
    print(f"Game world ready. {location_count} locations loaded.")
    print("")


    # ----- Week 5: the game loop, controlled by the game_running flag -----

    game_running = True

    while game_running:

        draw_hud(name, row, col, level, strength)


        if row == 0 and col == 0:
            print(f"Welcome, {name}! You stand at the edge of the Uncharted Territory, where danger and opportunity lurk at every turn. Your journey to the Enchanted Castle begins here. To the east lies an Abandoned Village shrouded in mystery, and to the south, a Haunted Forest beckons with eerie silence.")
        else:
            print("Descriptions coming soon.")

        print("")

        command = input("Enter your command: ")


        # ----- Week 7: move through the module, then award XP -----

        if command == "q":
            game_running = False
            print("Thank you for playing Adventure Quest!")
        elif command == "i":
            show_inventory(inventory)
        elif command == "n" or command == "s" or command == "e" or command == "w":
            new_row, new_col = locations.try_move(command, row, col)
            if new_row != row or new_col != col:
                row = new_row
                col = new_col
                xp = xp + XP_PER_MOVE
                level, strength = character.check_level_up(xp, level, strength)
        else:
            print("Invalid command.")

elif menu_choice == "2":
    print("Feature Under Construction.")
elif menu_choice == "3":
    print("Thank you for playing Adventure Quest!")
else:
    print("Invalid menu option.")
