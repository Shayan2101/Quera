n = int(input())
ans = 0
for _ in range(n):
    s = input()
    t = ''
    for ch in s:
        if ch not in t:
            t += ch
    ans = max(ans, len(t))
print(ans)
