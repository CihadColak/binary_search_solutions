def solve(self, n):
    primes = []
    for num in range(2, n):
        for j in range(2, num):
            if num % j == 0:
                break
        primes.append(num)
    return primes


print(solve(1, 5))
