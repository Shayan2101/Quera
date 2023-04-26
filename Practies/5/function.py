def calc(a):
    n = len(a)
    last_index = n - 1
    a.sort()
    a_sum = 0
    for i in a:
        a_sum += i
    avg = a_sum / n
    if n % 2 == 0:
        miane = (a[last_index//2] + a[(last_index//2)+1]) / 2
    else:
        miane = a[(last_index//2)]
    a_max = max(a)
    res = (avg, miane, a_max)
    # print(res)
    return res


# calc([2, 20, 30 , 29])
