from pathlib import Path
import json

def get_stored_number(path):
    if path.exists():
        contents = path.read_text()
        fav_number = json.loads(contents)
        return fav_number
    else:
        return None

def get_new_number(path):
    fav_number = input("Enter your favorite number: ")
    contents = json.dumps(fav_number)
    path.write_text(contents)
    return fav_number

def print_number():
    path = Path('favorite_number.txt')
    fav_number = get_stored_number(path)
    if fav_number:
        print("Your favorite number is: {fav_number}!")
    else:
        get_new_number(path)
        fav_number = get_stored_number(path)
        print("Your new favorite number is: {fav_number}!")

print_number()