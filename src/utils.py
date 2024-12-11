import os

def create_dirs(dirs):
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
