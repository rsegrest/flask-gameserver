import random;

class UserModel():

    def __init__(self, user_name, user_id=None, user_email=None, user_last_name=None, user_first_name=None):
        self.user_name = user_name
        if (user_id is None):
            self.user_id = random.randint(1, 1000000000)
        self.user_email = user_email
        self.user_last_name = user_last_name
        self.user_first_name = user_first_name

    def __str__(self):
        output_string = "User Name: " + self.user_name + "\n\tUser ID: " + str(self.user_id)
        if (self.user_email is not None):
            output_string += "\n\tEmail: " + self.user_email
        if (self.user_last_name is not None):
            output_string += "\n\tLast Name: " + self.user_last_name
        if (self.user_first_name is not None):
            output_string += "\n\tFirst Name: " + self.user_first_name
        return output_string

if __name__ == "__main__":
    user = UserModel()
    pass