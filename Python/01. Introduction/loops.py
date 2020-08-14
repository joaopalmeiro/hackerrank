if __name__ == "__main__":
    n = int(input())

    squared = [num ** 2 for num in range(n)]

    print(*squared, sep="\n")
