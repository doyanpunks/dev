"""
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing variables"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Name of the restaurant is {self.restaurant_name}")
        print(f"Cuisine is {self.cuisine_type}")
        
    def open_restaurant(self):
        print("Restaurant is open")
        
shaurma = Restaurant("Shaurma", "Fast Food")
shaurma.describe_restaurant()
shaurma.open_restaurant()