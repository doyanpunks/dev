class Privileges:
    def __init__(self):
        self.priveleges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for i in range(len(self.privileges)):
            print(self.privileges[i])


a = Privileges()
