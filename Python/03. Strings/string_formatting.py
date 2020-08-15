def print_formatted(number):
    width = len(f"{number:b}")

    for num in range(1, number + 1):
        print(
            "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(
                num, width=width
            )
        )


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
