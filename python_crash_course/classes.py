### Classes. Chapter 9
class Dog:

    def __init__(self, name, age):
        """initialize name and age atributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling overe in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
my_dog.roll_over()
my_dog.sit()