import pytest

from user_registration import UserRegistration

obj = UserRegistration()

def test_first_name_when_proper_should_return_true():
    assert obj.first_name_validation("Amit") == True

def test_first_name_when_improper_should_return_false():
    assert obj.first_name_validation("Amt") == False

def test_last_name_when_proper_should_return_true():
    assert obj.last_name_validation("Kumar") == True

def test_last_name_when_improper_should_return_false():
    assert obj.last_name_validation("Kum") == False

def test_email_when_proper_should_return_true():
    assert obj.email_validation("kumaramitsinha97@gmail.com") == True

def test_email_when_improper_should_return_false():
    assert obj.email_validation("kumaramit$gmail.com") == False

def test_phone_number_when_proper_should_return_true():
    assert obj.phone_number_validation("91 9430354429") == True

def test_phone_number_improper_should_return_flase():
    assert obj.phone_number_validation("9430354429") == False

def test_password_rule4_when_proper_should_return_true():
    assert obj.password_validation("Kum500081TS##") == True

def test_password_rule4_improper_should_return_false():
    assert obj.password_validation("KUMam") == False