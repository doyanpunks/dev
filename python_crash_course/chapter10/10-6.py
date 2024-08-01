from pathlib import Path

def Sum(value1, value2):
    try:
        #value1 = input("Enter value1: ")
        #value2 = input("Enter value2: ")
        int(value1)
        int(value2)
    except ValueError:
        print("Value is not a number!")
    else:
        return int(value1) + int(value2)

value1 = input("Enter value 1: ")
value2 = input("Enter value 2: ")
print(Sum(value1, value2))