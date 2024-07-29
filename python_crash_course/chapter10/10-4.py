from pathlib import Path

path = Path("guest.txt")
#content = path.read_text()
guest_name = input("Enter your name: ")
path.write_text(guest_name)

content = path.read_text()
print(content)