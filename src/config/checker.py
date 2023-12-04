import os
import src.config.constant


def check_directories():
    base_dir = "assets/guessing"
    directories = src.config.constant.CLASSES

    for directory in directories:
        dir_path = os.path.join(base_dir, directory)
        if not os.path.isdir(dir_path):
            raise ValueError(f"Directory '{directory}' does not exist.")
        else:
            files = os.listdir(dir_path)
            if len(files) == 0:
                raise ValueError(f"Directory '{directory}' is empty.")
