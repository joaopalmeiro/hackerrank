N = int(input())

X = list(map(int, input().split()))

W = list(map(int, input().split()))


def weighted_mean(X, W):
    numerator = sum([a * b for a, b in zip(X, W)])

    denominator = sum(W)

    weighted_mean_value = numerator / denominator

    return round(weighted_mean_value, 1)


print(weighted_mean(X, W))
