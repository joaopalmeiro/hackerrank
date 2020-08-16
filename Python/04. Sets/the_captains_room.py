if __name__ == "__main__":
    group_size = int(input())
    rooms = list(map(int, input().split()))

    # From the first part, you get `(group_size - 1) * number`:
    number = (sum(set(rooms)) * group_size - sum(rooms)) // (group_size - 1)

    print(number)
