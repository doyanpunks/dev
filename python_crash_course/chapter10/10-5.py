from pathlib import Path

path = Path("guest_book.txt")
contents = path.read_text()
number_of_guests = int(input("Enter number of guests: \n"))

while (number_of_guests != 0):
    name = input("Enter the guest name: ")
    contents += name + ".\n"
    number_of_guests -= 1

print(contents)