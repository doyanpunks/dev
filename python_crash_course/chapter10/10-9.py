from pathlib import Path

def read_the_zoo(path):
    try:
         contents = path.read_text()
    except FileNotFoundError:
         pass
    else:
         print(contents)

files = ['dogs.txt', 'cats.txt']
for file in files:
     path = Path(file)
     read_the_zoo(path)