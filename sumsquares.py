from functools import reduce
ag = [1, 2, 3, -4]


def summa(a, b):
    if b > 0:
        return a + b**2
    else:
        return a + 0


sum_a = reduce(summa, ag)
print(sum_a)
