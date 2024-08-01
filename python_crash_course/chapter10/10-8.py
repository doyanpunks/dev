from pathlib import Path
from word_count import count_words

def read_the_zoo(path):
    try:
         contents = path.read_text()
    except FileNotFoundError:
         print(f"File {path} is not found!")
    else:
         print(contents)

files = ['dogs.txt', 'cats.txt']
for file in files:
     path = Path(file)
     read_the_zoo(path)