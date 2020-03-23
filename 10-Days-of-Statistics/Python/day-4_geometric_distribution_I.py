# Enter your code here. Read input from STDIN. Print output to STDOUT

i = "1 3"

i = list(map(int, i.split()))

n = 5

p = i[0] / i[1]


def geometric_pmf(n, p):
    q = 1 - p
    g = q ** (n - 1) * p

    return(round(g, 3))


print(geometric_pmf(n, p))
