from math import factorial

i = list(map(float, "1.09 1".split()))

p = i[0] / sum(i)
# p = 0.5

x = 3
# x = 5

n = 6
# n = 10


def binomial_pmf(x, n, p):
    f = factorial(n) / (factorial(x) * factorial(n - x))
    b = f * p ** x * (1 - p) ** (n - x)

    return b


def at_least_cdf(x, n, p):
    b = [binomial_pmf(x_r, n, p) for x_r in range(x, n + 1)]

    return round(sum(b), 3)


print(at_least_cdf(x, n, p))
