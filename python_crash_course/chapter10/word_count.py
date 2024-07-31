from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} is not found.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Number of words in {path} is: {num_words} words.")

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt']
for filname in filenames:
    path = Path(filenames)
count_words(path)