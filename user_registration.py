import re
from user_registration_exception import UserRegistrationException
from user_registration_interface import IMyInterface

first_name = "^[A-Z][a-z]{2,}$"
last_name = "^[A-Z][a-z]{2,}$"
email = "^[a-zA-z]{3}[0-9a-zA-Z\\.\\_\\-\\+]*@[a-z]*\\.(co|com.au|in|net|in|com.com|com|)$"
phone = "^91[\\s][6-9][0-9]{9}$"
password = "^(?=.*[0-9])" + "(?=.*[a-z])(?=.*[A-Z])" + "(?=.*[@#$%^&+=]).{8,20}"


class UserRegistration(IMyInterface):

    def __init__(self):
        pass

    def first_name_validation(self, first_name_input):
        if re.match(first_name, first_name_input):
            print("Valid first name")
            return True
        else:
            print("Invalid first name ")
            return False
            #raise UserRegistrationException("Wrong value input, please try again !")

    def last_name_validation(self, last_name_input):
        if re.match(last_name, last_name_input):
            print("Valid Last name")
            return True
        else:
            print("Invalid Last Name ")
            return False

    def email_validation(self, email_input):
        if re.match(email, email_input):
            print("Valid Email")
            return True
        else:
            print("Invalid Email ")
            return False

    def phone_number_validation(self, phone_number_input):
        if re.match(phone, phone_number_input):
            print("Valid Phone")
            return True
        else:
            print("Invalid Phone ")
            return False

    def password_validation(self, password_input):
        if re.match(password, password_input):
            print("Valid Password")
            return True
        else:
            print("Invalid Password ")
            return False
