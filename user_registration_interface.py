import abc


class IMyInterface(abc.ABC):

    @abc.abstractmethod
    def first_name_validation(self, first_name_input):
        pass

    def last_name_validation(self, last_name_input):
        pass

    def email_validation(self, email_input):
        pass

    def phone_number_validation(self, phone_number_input):
        pass

    def password_validation(self, password_input):
        pass
