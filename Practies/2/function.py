from datetime import datetime


def day_calculator(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    sajjad_date = datetime.strptime('14-01-1999', '%d-%m-%Y')
    if (date - sajjad_date).days >= 0:
        return (date - sajjad_date).days
    else:
        return "Not yet born"
    # print((date - sajjad_date).days)


# day_calculator('2005-01-06')
