from pathlib import Path

def count_words(path):
    #Count the approximate number of words in a file.
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Number of words in {path} is: {num_words} words.")


"""
filenames = ['alice.txt', 'moby_dick.txt', 'little_woman.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
    """