"""Roll one or more dice and display their faces as a text diagram."""

import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DICE_HEIGHT = len(DICE_ART[1])
DICE_WIDTH = len(DICE_ART[1][0])
DICE_FACE_SEPARATOR = " "


def parse_input(input_string):
    """Return the requested number of dice, or exit for invalid input."""
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number between 1 - 6")
        raise SystemExit(1)


def roll_dice(num_dice):
    """Return ``num_dice`` random results, with each result from 1 to 6."""
    roll_result = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_result.append(roll)
    return roll_result


def generate_dice_faces_diagram(dice_values):
    """Return a formatted text diagram for the dice values provided."""
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


def _get_dice_faces(dice_values):
    """Return the text-art face for each value in ``dice_values``."""
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces


def _generate_dice_faces_rows(dice_faces):
    """Combine each row of the dice faces into rows for the final diagram."""
    dice_faces_rows = []
    for row_idx in range(DICE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DICE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows


def main():
    """Read the user's choice, roll the dice, and display the results."""
    num_dice_input = input("how many dices do you want to roll? [1-6] ")
    num_dice = parse_input(num_dice_input)
    roll_results = roll_dice(num_dice)
    dice_faces_art = generate_dice_faces_diagram(roll_results)
    print(f"\n{dice_faces_art}")


if __name__ == "__main__":
    main()