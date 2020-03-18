# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

X = list(map(int, input().split()))


def mean(N, X):
    mean_value = sum(X) / N

    return(mean_value)


def sd(N, X):
    mean_value = mean(N, X)

    squared_dist_value = [(x - mean_value) ** 2 for x in X]

    sd_value = (sum(squared_dist_value) / N) ** (1/2)

    return(round(sd_value, 1))


print(sd(N, X))
