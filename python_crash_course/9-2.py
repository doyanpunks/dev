"""
Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
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
        print(f"{self.restaurant_name} is open")
        
shaurma = Restaurant("Shaurma", "Fast Food")
shaurma.describe_restaurant()
shaurma.open_restaurant()

daredjani = Restaurant("Daredjani", "Georgian")
daredjani.describe_restaurant()
daredjani.open_restaurant()

sandyq = Restaurant("Sandyq", "Kazakh")
sandyq.describe_restaurant()
sandyq.open_restaurant()
