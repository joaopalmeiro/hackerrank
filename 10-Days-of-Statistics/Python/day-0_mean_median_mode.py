# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

X = list(map(int, input().split()))


def mean(N, X):
    mean_value = sum(X) / N

    return(round(mean_value, 1))


def median(N, X):
    X.sort()

    if(N % 2 == 0):
        numerator = X[int(N/2)] + X[int(N/2 - 1)]
        median_value = numerator / 2
    else:
        median_value = X[int(N/2)]

    return(round(median_value, 1))


def mode(X):
    count = dict()

    for i in X:
        count[i] = count.get(i, 0) + 1

    mode = max(count, key=count.get)

    return(round(mode, 1))


print(mean(N, X))
print(median(N, X))
print(mode(X))
