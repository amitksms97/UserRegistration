class UserRegistrationInput:

    def __init__(self, first_name_input = '', last_name_input ='', email_input = '', phone_number_input = '', password_input = ''):
        self.first_name_input = first_name_input
        self.last_name_input = last_name_input
        self.email_input = email_input
        self.phone_number_input = phone_number_input
        self.password_input = password_input

    def get_first_name_input(self):
        return self.first_name_input

    def set_first_name_input(self, first_name):
        self.first_name_input = first_name

    def get_last_name_input(self):
        return self.last_name_input

    def set_last_name_input(self, last_name):
        self.last_name_input = last_name

    def get_email_input(self):
        return self.email_input

    def set_email_input(self, email_input):
        self.email_input = email_input

    def get_phone_number_input(self):
        return self.phone_number_input

    def set_phone_number_input(self, phone_number_input):
        self.phone_number_input = phone_number_input

    def get_password_input(self):
        return self.password_input

    def set_password_input(self, password_input):
        self.password_input = password_input
