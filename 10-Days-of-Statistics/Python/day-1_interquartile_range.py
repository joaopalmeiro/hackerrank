n = int(input())

X = list(map(int, input().split()))

F = list(map(int, input().split()))

S = [x for i, x in enumerate(X) for f in range(F[i])]

S.sort()

n = len(S)

assert sum(F) == n, "The number of elements must equal the total frequency."


def median(n, X):
    if n % 2 == 0:
        numerator = float(X[int(n / 2)] + X[int(n / 2 - 1)])
        median_value = numerator / 2.0
    else:
        median_value = float(X[int(n / 2)])

    return median_value


def IQR(n, X):
    Q1 = median(int(n / 2), X[: int(n / 2)])

    if n % 2 == 0:
        Q3 = median(int(n / 2), X[int(n / 2) :])
    else:
        Q3 = median(int(n / 2), X[int(n / 2) + 1 :])

    return round(Q3 - Q1, 1)


print(IQR(n, S))
