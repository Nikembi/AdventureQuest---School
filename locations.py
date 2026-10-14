# ----- Week 3: the game world as a 2-D list -----

world = [
    ["Uncharted Territory", "Haunted Forest", "Mystical City", "Haunted Forest", "Uncharted Territory"],
    ["Abandoned Village", "Uncharted Territory", "Magical Spring", "Uncharted Territory", "Forest Camp"],
    ["Mystical City", "Ancient Ruins", "Enchanted Castle", "Ancient Ruins", "Mystical City"],
    ["Forest Camp", "Uncharted Territory", "Magical Spring", "Uncharted Territory", "Abandoned Village"],
    ["Uncharted Territory", "Haunted Forest", "Mystical City", "Abandoned Village", "Uncharted Territory"],
]


def location_name(row, col):
    return world[row][col]


# ----- Week 4: one boundary-checked move -----

def try_move(direction, row, col):
    if direction == "n":
        if row > 0:
            row = row - 1
        else:
            print("You cannot move further north.")
    elif direction == "s":
        if row < 4:
            row = row + 1
        else:
            print("You cannot move further south.")
    elif direction == "e":
        if col < 4:
            col = col + 1
        else:
            print("You cannot move further east.")
    elif direction == "w":
        if col > 0:
            col = col - 1
        else:
            print("You cannot move further west.")
    return row, col
