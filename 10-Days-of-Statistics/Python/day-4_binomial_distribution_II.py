# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial

i = "12 10"

i = list(map(int, i.split()))

p = i[0] / 100

x = 2

n = i[1]


def binomial_pmf(x, n, p):
    f = factorial(n) / (factorial(x) * factorial(n - x))
    b = f * p ** x * (1-p) ** (n-x)

    return(b)


def cdf(a, b, n, p):
    p = [binomial_pmf(x_r, n, p) for x_r in range(a, b+1)]

    return(round(sum(p), 3))


print(cdf(0, x, n, p))
print(cdf(x, n, n, p))
