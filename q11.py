s = input()

ls = []
c = 0
d = 0
for i in s:
    c += 1
    if i != "=":
        ls.append(i)
    else:
        d += 1
        if c != d:
            ls.pop()
for j in ls:
    print(j, end="")
