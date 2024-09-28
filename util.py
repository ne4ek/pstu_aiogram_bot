import os
from pathlib import Path

def get_all_menu_items():
    ordering = ['napravlenia', 'stoimost', 'obshejitie',
                'contacti', 'anketi', 'eksameni',
                'postuplenie' ,'ligoti', 'o_vuse',
                ]
    return ordering

def get_all_social_for_menu():
    ordering = {'vk': 'https://vk.ru', 'wikipedia': 'https://wikipedia.com', 'telegram': 'https://t.me'}
    return ordering



def get_all_image_for(directory):
    cwd = os.getcwd()
    full_path = cwd + directory
    all_files = [file.name for file in Path(full_path).iterdir() if file.is_file()]
    return all_files
    
    
def get_all_image_stoimost():
    directory = '/static/img/menu_pages/stoimost/'
    return get_all_image_for(directory=directory)


def get_all_image_obshejitie():
    directory = '/static/img/menu_pages/obshejitie/'
    return get_all_image_for(directory=directory)