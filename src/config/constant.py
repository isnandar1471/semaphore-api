import typing
import os

CLASSES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(f"CLASSES {type(CLASSES)} {CLASSES}")

GUESSING_DIRPATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "guessing"))
print(f"GUESSING_DIRPATH {type(GUESSING_DIRPATH)} {GUESSING_DIRPATH}")
