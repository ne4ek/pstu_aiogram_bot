import os
from pathlib import Path


def get_all_image_stoimost():
    cwd = os.getcwd()
    directory = '/static/img/menu_pages/stoimost/'
    full_path = cwd + directory
    all_files = [file.name for file in Path(full_path).iterdir() if file.is_file()]
    return all_files