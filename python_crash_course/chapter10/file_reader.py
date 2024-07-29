from  pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birhday appear in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

print(f"{pi_string[:52]}")
print(len(pi_string))