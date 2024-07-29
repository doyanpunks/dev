class User:
    def __init__(self, first_name, last_name, uid, passwd):
        """Initialize variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.uid = uid
        self.passwd = passwd
   
    def describe_user(self):
        print(f"User {self.first_name} {self.last_name} with UID: {self.uid} has password: {self.passwd}")
        
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! Nice to meet you!")
        
mikey = User("Casey", "Muratori", 9779, 12345678990)
mikey.greet_user()
mikey.describe_user()

jon = User("Jonathan", "Blow", 10001, 9876543210)
jon.greet_user()
jon.describe_user()