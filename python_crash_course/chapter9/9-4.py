class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing variables"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"Name of the restaurant is {self.restaurant_name}")
        print(f"Cuisine is {self.cuisine_type}")
        
    def open_restaurant(self):
        print("Restaurant is open")

    def set_number_served(self, served_number):
        self.number_served = served_number 
    
    def increment_number_served(self, served_number):
        self.number_served += served_number
        
shaurma = Restaurant("Shaurma", "Fast Food")
shaurma.describe_restaurant()
print(f"guests served: {shaurma.number_served}")
shaurma.set_number_served(34)
print(f"guests served: {shaurma.number_served}")
shaurma.increment_number_served(7)
print(f"guests served: {shaurma.number_served}")
shaurma.open_restaurant()