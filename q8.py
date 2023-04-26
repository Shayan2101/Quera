k = int(input())
code = input()
ans = 0
n = 0
for _ in range(k):
    charkhane = input()
    for i in code[n]:
        # print("i =", i)
        cou = -1
        for j in charkhane:
            cou += 1
            if i == j:
                if cou < 5:
                    ans += cou
                    # print("cou =", cou)
                else:
                    ans += 9-cou
                    # print("cou =", cou)
    n += 1
print(ans)
