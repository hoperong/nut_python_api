import os


def get_full_path(*path):
    return os.path.abspath(os.path.join(*path))
