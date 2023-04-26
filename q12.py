m, n = map(int, input().split())
ls = []
for x in range(m):
    ls.append([])
    for y in range(n):
        ls[x].append(0)
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    ls[r-1][c-1] = "*"
    for i in range(r-2, r+1):
        for j in range(c-2, c+1):
            if (i in range(m)) and (j in range(n)) and (ls[i][j] != "*"):
                # print("OK, {}{}".format(i, j))
                ls[i][j] += 1

# print(ls)
for o in range(m):
    for c in range(n):
        print(ls[o][c], end=' ')
    print()
