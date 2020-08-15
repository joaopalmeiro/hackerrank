import textwrap
from typing import List


def wrap(string: str, max_width: int) -> List[str]:
    return textwrap.wrap(string, width=max_width)


def fill(string: str, max_width: int) -> str:
    return textwrap.fill(string, width=max_width)


if __name__ == "__main__":
    string, max_width = input(), int(input())

    # result = wrap(string, max_width)
    # print(*result, sep="\n")

    result = fill(string, max_width)
    print(result)
