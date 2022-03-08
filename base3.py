def solve(n):
    # 11 / 3 == 3 r 2
    #  3 / 3 == 1 r 0
    #  1 / 3 == 0 r 1
    div = 1
    res = ""
    c = n
    while c > 0:
        res += str(c % 3)
        c = c // 3

    return int(res)


print(solve(11))
