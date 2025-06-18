import os

def get_data():
    file_path = os.path.join(os.path.dirname(__file__), 'names.txt')
    with open(file_path) as f:
        names = f.read().splitlines()
    return names
