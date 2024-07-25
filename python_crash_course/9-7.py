class User:
    def __init__(self, first_name, last_name, uid, passwd):
        """Initialize variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.uid = uid
        self.passwd = passwd
        self.login_attempts = 0
   
    def describe_user(self):
        print(f"User {self.first_name} {self.last_name} with UID: {self.uid} has password: {self.passwd}")
        
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! Nice to meet you!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for i in self.privileges:
            print(i)

class Admin(User):
    def __init__(self, first_name, last_name, uid, passwd, privileges):
        super().__init__(first_name, last_name, uid, passwd)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()

privileges_list = ["can add post", "can delete post", "can ban user"]
admin = Admin("Tom", "Cruze", "6547", "747", privileges_list)
admin.show_privileges()