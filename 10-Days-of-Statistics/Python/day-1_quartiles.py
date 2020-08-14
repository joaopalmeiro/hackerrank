n = int(input())

X = list(map(int, input().split()))

X.sort()


def median(n, X):
    if n % 2 == 0:
        numerator = X[int(n / 2)] + X[int(n / 2 - 1)]
        median_value = numerator / 2
    else:
        median_value = X[int(n / 2)]

    return int(median_value)


print(median(int(n / 2), X[: int(n / 2)]))
print(median(n, X))
if n % 2 == 0:
    print(median(int(n / 2), X[int(n / 2) :]))
else:
    print(median(int(n / 2), X[int(n / 2) + 1 :]))
