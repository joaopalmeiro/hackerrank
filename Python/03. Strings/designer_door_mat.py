# Shape: (N, M) -> N is an odd natural number, M is 3 times N

MESSAGE = "WELCOME"
PATTERN = ".|."
PADDING = "-"

if __name__ == "__main__":
    N, M = map(int, input().split())  # Height, Width

    half = [(PATTERN * (row * 2 + 1)).center(M, PADDING) for row in range(N // 2)]

    print(*half, sep="\n")
    print(MESSAGE.center(M, PADDING))
    print(*half[::-1], sep="\n")
