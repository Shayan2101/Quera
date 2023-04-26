import re


def validate_email(email):
    # p = re.split("@", email)
    # print(re.search("\.l*\w+@\d*\w+\.[a-z]", p[0]))
    if re.search("^[\.\w]+@\w[^_]+\.[a-zA-Z]{3}$", email):
        # print(True)
        return True
    else:
        # print(False)
        return False
    # print("p[1] = {}".format(p[1]))
    # print(re.search("\w[^_]+\.[a-zA-Z]{3}$", p[1]).group())


def validate_phone(number):
    if re.search("^09\d{9}$", number):
        # print("1.", True)
        return True
    elif re.search("^\+989\d{9}$", number):
        # print("2.", True)
        return True
    elif re.search("^00989\d{9}$", number):
        # print("3.", True)
        return True
    else:
        # print(False)
        return False


# validate_email(input())
# validate_phone(input())
