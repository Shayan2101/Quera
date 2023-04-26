def comb(n, k):
    a = n
    b = k
    c = n-k
    i = 1
    while i < n:
        a *= i
        i += 1
    j = 1
    while j < k:
        b *= j
        j += 1
    if k < n and k != 0:
        d = 1
        while d < n-k:
            c *= d
            d += 1
            # print(f"d = {d}")
        # print(f"a = {a} , b = {b} , c = {c}")
        # print(a / (b * c))
        return a / (b * c)
    elif k > n:
        # print(0)
        return 0
    elif k == 0:
        # print(1)
        return 1
    elif n == k:
        # print(1)
        return 1


# comb(3, 0)
