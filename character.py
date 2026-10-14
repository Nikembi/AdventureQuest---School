import math


# ----- Week 7: the leveling system -----

def check_level_up(xp, level, strength):
    threshold = int(100 * math.pow(level, 1.5))

    if xp >= threshold:
        level = level + 1
        strength = strength + 5
        print(f"*** Level up! You are now level {level} (Strength {strength}). ***")

    return level, strength
