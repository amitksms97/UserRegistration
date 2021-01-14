from user_registration import UserRegistration
from user_registration_input import UserRegistrationInput

obj_user_input = UserRegistrationInput()
obj_user_check = UserRegistration()

if __name__ == '__main__':
        first_name = input("Enter your first name:")
        obj_user_input.set_first_name_input(first_name)
        first_name_input = obj_user_input.get_first_name_input()
        obj_user_check.first_name_validation(first_name_input)
        last_name = input("Enter Your Last Name:")
        obj_user_input.set_last_name_input(last_name)
        last_name_input = obj_user_input.get_last_name_input()
        obj_user_check.last_name_validation(last_name_input)
        email_input = input("Enter Your Email Address:")
        obj_user_input.set_email_input(email_input)
        email_input = obj_user_input.get_email_input()
        obj_user_check.email_validation(email_input)
        phone_number_input = input("Enter Your Phone Number:")
        obj_user_input.set_email_input(email_input)
        phone_number = obj_user_input.get_phone_number_input()
        obj_user_check.phone_number_validation(phone_number)
        password_input = input("Enter Your Password:")
        obj_user_input.set_password_input(password_input)
        password_input = obj_user_input.get_password_input()
        obj_user_check.password_validation(password_input)
