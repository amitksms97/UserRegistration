import pytest

from user_registration import UserRegistration

user = UserRegistration()


@pytest.mark.parametrize("actual,expected",
                         [("Amit", True), ("AMT", False), ("amit", False), ("aMIT", False), ("AMIT", False)])
def test_first_name_when_proper_should_return_true(actual, expected, print_test_statement):
    assert user.first_name_validation(actual) == expected


@pytest.mark.parametrize("actual,expected",
                         [("Kumar", True), ("KUM", False), ("kumar", False), ("Kum", True), ("KUMAR", False)])
def test_last_name_when_proper_should_return_true(actual, expected, print_test_statement):
    assert user.first_name_validation(actual) == expected


@pytest.mark.parametrize("actual,expected",
                         [("amitksms@gmail.com", True), ("AMITKSMS@gmail.xo", False), ("amitksms.gmail.com", False),
                          ("amitksms97@yahoo.com", True), ("amit123ksms@google.in", True)])
def test_email_when_proper_should_return_true(actual, expected, print_test_statement):
    assert user.email_validation(actual) == expected


@pytest.mark.parametrize("actual,expected", [("91 9422484996", True), ("919422484996", False), ("9422484996", False),
                                             ("91 7020665302", True), ("91 9421359551", True)])
def test_phone_number_when_proper_should_return_true(actual, expected, print_test_statement):
    assert user.phone_number_validation(actual) == expected


@pytest.mark.parametrize("actual,expected", [("Amit@123", True), ("amitKum%123", True), ("9422amitD&1", True)])
def test_password_when_proper_should_return_true(actual, expected, print_test_statement):
    assert user.password_validation(actual) == expected
