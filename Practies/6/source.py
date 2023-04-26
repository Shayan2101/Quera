import re


def check_registration_rules(**kwargs):
    ls = []
    # print(kwargs)
    for name, password in kwargs.items():
        # print("name = {} , password = {}".format(name, password))
        if (len(name) >= 4) and (len(password) >= 6):
            if (name != "quera") and (name != "codecup"):
                if not password.isdigit():
                    ls.append(name)
    # print(ls)
    return ls


# check_registration_rules(saeed='1234567', ab='afj$L12', username='password', sadegh='He3@lsa',
#                          quera='qwerty80', mmdreza='monday80', ali="aliali@", mammad="salam")
