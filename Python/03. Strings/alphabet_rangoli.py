from string import ascii_lowercase as LOWERCASE

PADDING = "-"


def print_rangoli(size: int) -> None:
    width = size + 3 * (size - 1)

    half = [
        PADDING.join(LOWERCASE[i:size][::-1][:-1] + LOWERCASE[i:size]).center(
            width, PADDING
        )
        for i in range(size - 1, -1, -1)
    ]

    print(*half + half[:-1][::-1], sep="\n")


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
