from pathlib import Path
path = Path("learning_python.txt")
content = path.read_text()
str = ''

for line in content.splitlines():
    str += line

print("printing the entire file: \n")
print(str)

print("\nprintting looping over each line: \n")
for line in content.splitlines():
    print(line)
      