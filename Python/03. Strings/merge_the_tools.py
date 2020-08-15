import sys
import textwrap
from collections import OrderedDict


def remove_duplicates(string: str, keep_order: bool = True) -> str:
    return (
        "".join((dict if sys.version_info >= (3, 6) else OrderedDict).fromkeys(string))
        if keep_order
        else "".join(set(string))
    )


def merge_the_tools(string: str, k: int) -> None:
    segments = map(remove_duplicates, textwrap.wrap(string, k))

    print(*segments, sep="\n")


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
