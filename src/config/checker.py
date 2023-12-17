import os
import os.path
import typing


import src.config.constant
import src.config.environment


def check_directories():
    base_dir = "assets/guessing"
    directories = src.config.constant.CLASSES

    for directory in directories:
        dir_path = os.path.join(base_dir, directory.lower())
        if not os.path.isdir(dir_path):
            raise ValueError(f"Directory '{dir_path}' does not exist.")
        else:
            files = os.listdir(dir_path)
            if len(files) == 0:
                raise ValueError(f"Directory '{dir_path}' is empty.")


def check_word_list() -> typing.List[str]:
    if not os.path.exists(src.config.environment.APP_LIST_OF_WORDS_FILE_PATH):
        raise ValueError(f"File '{src.config.environment.APP_LIST_OF_WORDS_FILE_PATH}' does not exist.")

    if not os.path.isfile(src.config.environment.APP_LIST_OF_WORDS_FILE_PATH):
        raise ValueError(f"File '{src.config.environment.APP_LIST_OF_WORDS_FILE_PATH}' is not a file.")

    if not os.access(src.config.environment.APP_LIST_OF_WORDS_FILE_PATH, os.R_OK):
        raise ValueError(f"File '{src.config.environment.APP_LIST_OF_WORDS_FILE_PATH}' is not readable.")

    lines: typing.List[str] = []
    with open(src.config.environment.APP_LIST_OF_WORDS_FILE_PATH) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().replace(" ", "")
        if line == "":
            raise ValueError(f"File '{src.config.environment.APP_LIST_OF_WORDS_FILE_PATH}' contains empty line.")

        if all((char in src.config.constant.CLASSES) for char in line) == False:
            raise ValueError(f"File '{src.config.environment.APP_LIST_OF_WORDS_FILE_PATH}' contains invalid word '{line}'.")

    if len(lines) == 0:
        raise ValueError(f"File '{src.config.environment.APP_LIST_OF_WORDS_FILE_PATH}' is empty.")
