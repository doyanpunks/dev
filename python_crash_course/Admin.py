from User import User
from Privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, uid, passwd):
        super().__init__(first_name, last_name, uid, passwd)
        self.privileges = Privileges()
        self.privileges = []

    def show_privileges(self):
        self.privileges.show_privileges()

