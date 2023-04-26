p, d = input().split()
p = int(p)
d = int(d)

i = 1
while True:
    sm = d * i
    i += 1
    if ((sm % p) >= 0) and ((sm % p) <= (p/2)):
        break
print(sm)
