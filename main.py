
print("=" * 80)
print(f"{'Adventure Quest':^80}")
print("=" * 80)
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


print("=" * 80)
print(f"{'Adventure Quest':^80}")
print("=" * 80)
print("Create your Character!")
print("")


health = 100
strength = 10
level = 1
gold = 0
magic = 0

inventory = ["Food", "Water"]


name = input("Enter your character's name: ")
bonus = int(input("Choose a starting strength bonus (0-5): "))


strength = strength + bonus
attack_power = strength * 2 + level

print(f"Character created! Name: {name}, Health: {health}, Strength: {strength}")
print(f"Attack Power: {attack_power}")
print("")


# ----- Week 3: the game world as a 2-D list -----

world = [
    ["Uncharted Territory", "Haunted Forest", "Mystical City", "Haunted Forest", "Uncharted Territory"],
    ["Abandoned Village", "Uncharted Territory", "Magical Spring", "Uncharted Territory", "Forest Camp"],
    ["Mystical City", "Ancient Ruins", "Enchanted Castle", "Ancient Ruins", "Mystical City"],
    ["Forest Camp", "Uncharted Territory", "Magical Spring", "Uncharted Territory", "Abandoned Village"],
    ["Uncharted Territory", "Haunted Forest", "Mystical City", "Abandoned Village", "Uncharted Territory"],
]
row = 0
col = 0

location_count = len(world) * len(world[0])

print("Initializing game world...")
print("Row 0:", world[0])
print("Row 1:", world[1])
print("Row 2:", world[2])
print("Row 3:", world[3])
print("Row 4:", world[4])
print(f"Game world ready. {location_count} locations loaded.")
print("")


location = world[row][col]

location_line = f"Location: {location} ({row}, {col})"

stat_row = f"Name: {name}".ljust(22) + f"Health: {health}".ljust(24) + f"Strength: {strength}"
info_row = f"Level: {level}".ljust(22) + f"Gold: {gold}".ljust(22) + f"Inventory: {inventory[0]}, {inventory[1]}"

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


print(f"Welcome, {name}! You stand at the edge of the Uncharted Territory, where danger and opportunity lurk at every turn. Your journey to the Enchanted Castle begins here. To the east lies an Abandoned Village shrouded in mystery, and to the south, a Haunted Forest beckons with eerie silence.")
print("")

command = input("Enter your command: ")