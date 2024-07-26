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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["phistachio", "vanile", "banana"]

    def show_flavors(self):
        for i in range(len(self.flavors)):
            print(self.flavors[i])

"""
ice_cream_stand = IceCreamStand("Gelato", "Ice Cream")
ice_cream_stand.show_flavors()
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
"""