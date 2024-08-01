from pathlib import Path
from word_count import count_words

def count(word, filename):
    count = 0
    for i in filename:
        if i == word:
            count += 1
    return count

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
    print(count('Neck Snap'), path)
