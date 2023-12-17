import typing
import os
import os.path
import src.config.environment

CLASSES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(f"CLASSES {type(CLASSES)} {CLASSES}")

IMAGE_WIDTH = 128
print(f"IMAGE_WIDTH {type(IMAGE_WIDTH)} {IMAGE_WIDTH}")

IMAGE_HEIGHT = 256
print(f"IMAGE_HEIGHT {type(IMAGE_HEIGHT)} {IMAGE_HEIGHT}")

GUESSING_DIRPATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "guessing"))
print(f"GUESSING_DIRPATH {type(GUESSING_DIRPATH)} {GUESSING_DIRPATH}")

LIST_OF_WORDS: typing.List[str] = []
with open(os.path.join(os.path.dirname(__file__), "..", "..", src.config.environment.APP_LIST_OF_WORDS_FILE_PATH)) as f:
    LIST_OF_WORDS = [line.strip().replace(" ", "") for line in f.readlines()]
print(f"LIST_OF_WORDS {type(LIST_OF_WORDS)} len: {len(LIST_OF_WORDS)}")

print("")
