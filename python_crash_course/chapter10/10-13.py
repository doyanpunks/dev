from pathlib import Path
import json

# Dictionary {}
def get_info_from_file(path):
    if path.exists():
        contents = path.read_text()
        info = json.loads(contents)
        return info

def get_new_info(path):
    info = {}
    n = 3
    while n != 0:
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        info[key] = value
        contetns = json.dumps(info)
        path.write_text(contetns)
        n = n -1

def display_info():
    path = Path('user_info.json')
    info = get_info_from_file(path)
    if path.exists():
        print(f"Your info is: {info}")
    else:
         info = get_new_info(path)


display_info()