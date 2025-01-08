from django.test import TestCase

# Create your tests here.
from app.utils import validate_license_code, send_sms_with_error_handling

def test_validate_license_code():
    assert validate_license_code("123456") == True
    assert validate_license_code("12345") == False

def test_send_sms_with_error_handling():
    assert send_sms_with_error_handling("1234567890", "Test message") == True

