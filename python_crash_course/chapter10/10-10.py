from pathlib import Path
from word_count import count_words

def count(word, filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
         count_words = contents.lower().count(word)

         msg = f"'{word}' appears in {filename} about {count_words} times."
         print(msg)
    

filename = 'alice.txt'
count('the', filename)