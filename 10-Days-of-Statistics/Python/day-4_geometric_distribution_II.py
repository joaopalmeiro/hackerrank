# Enter your code here. Read input from STDIN. Print output to STDOUT

i = "1 3"

i = list(map(int, i.split()))

n = 5

p = i[0] / i[1]


def geometric_cdf(n, p):
    g = 1 - (1 - p) ** n

    return(round(g, 3))


print(geometric_cdf(n, p))
