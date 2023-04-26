import re


def solve(arr):
    p = re.split("[\+=\s]+", arr)
    # print(p)
    c = -1
    t1 = 0
    t2 = 0
    y = 0
    for x in p:
        c += 1
        if re.search("#+", x):
            t = re.split("#", x)
            t1 = t[0]
            t2 = t[1]
            if c == 0:
                # y = int(p[2]) - int(p[1])
                y = max(int(p[1]), int(p[2])) - min(int(p[1]), int(p[2]))
                if re.search(rf'^{t1}.*{t2}$', str(y)):
                    # print("y =", y)
                    # print("{} + {} = {}".format(y, p[1], p[2]))
                    return "{} + {} = {}".format(y, p[1], p[2])
                else:
                    return "-1"
            elif c == 1:
                # y = int(p[2]) - int(p[0])
                y = max(int(p[0]), int(p[2])) - min(int(p[0]), int(p[2]))
                if re.search(rf'^{t1}.*{t2}$', str(y)):
                    return "{} + {} = {}".format(p[0], y, p[2])
                else:
                    return "-1"
            else:
                # y = int(p[1]) + int(p[0])
                y = max(int(p[1]), int(p[0])) + min(int(p[1]), int(p[0]))
                if re.search(rf'^{t1}.*{t2}$', str(y)):
                    # print("y =", y)
                    # print("{} + {} = {}".format(p[0], p[1], y))
                    return "{} + {} = {}".format(p[0], p[1], y)
                else:
                    return "-1"


# solve(input())
