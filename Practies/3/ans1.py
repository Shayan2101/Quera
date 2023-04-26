import re


def validate_email(email):
    if re.search("\.*\w+@\w[^_]+\.[a-zA-Z]{3}$", email):
        return True
    else:
        return False


def validate_phone(number):
    if re.search("^09", number) and re.search("\d", number) and len(number) == 11:
        return True
    elif re.search("^\+989", number) and re.search("\+\d", number) and len(number) == 13:
        return True
    elif re.search("^00989", number) and re.search("\d", number) and len(number) == 14:
        return True
    else:
        return False
