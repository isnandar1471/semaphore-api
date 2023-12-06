import typing
import os

CLASSES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(f"CLASSES {type(CLASSES)} {CLASSES}")

IMAGE_WIDTH = 128
print(f"IMAGE_WIDTH {type(IMAGE_WIDTH)} {IMAGE_WIDTH}")

IMAGE_HEIGHT = 256
print(f"IMAGE_HEIGHT {type(IMAGE_HEIGHT)} {IMAGE_HEIGHT}")

GUESSING_DIRPATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "guessing"))
print(f"GUESSING_DIRPATH {type(GUESSING_DIRPATH)} {GUESSING_DIRPATH}")
