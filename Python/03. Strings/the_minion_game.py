from collections import Counter
from itertools import islice, tee
from typing import Iterable, Iterator

VOWELS = "AEIOU"


def nwise(iterable: Iterable, n: int = 2) -> Iterator:
    iters = tee(
        iterable, n
    )  # `tee` returns `n` independent iterators from a single iterable
    for i, it in enumerate(iters):
        next(
            islice(it, i, i, 1), None
        )  # Advance each independent iterator `i`-steps ahead
    return zip(*iters)  # The `zip` function ensures groups of size `n` only


# It does not run within the time limit.
# It is not optimized large strings at all.
def minion_game_first_try(string: str) -> None:
    vowels_score = 1 if string.startswith(tuple(VOWELS)) else 0
    consonants_score = 1 if not string.startswith(tuple(VOWELS)) else 0

    for length in range(1, len(string)):
        cnt = Counter(nwise(string, length))
        vowels_cnt = sum(v for k, v in cnt.items() if k[0] in VOWELS)

        vowels_score += vowels_cnt
        consonants_score += sum(cnt.values()) - vowels_cnt

    if vowels_score == consonants_score:
        print("Draw")
    elif vowels_score > consonants_score:
        print(f"Kevin {vowels_score}")
    else:
        print(f"Stuart {consonants_score}")


def minion_game(string: str) -> None:
    vowels_score = 0
    consonants_score = 0

    length = len(string)

    # Each substring at position `i` starts with the same character.
    # With this in mind, it is enough to iterate over the string once.
    for i, l in enumerate(string):
        if l in VOWELS:
            vowels_score += length - i
        else:
            consonants_score += length - i

    if vowels_score == consonants_score:
        print("Draw")
    elif vowels_score > consonants_score:
        print(f"Kevin {vowels_score}")
    else:
        print(f"Stuart {consonants_score}")


if __name__ == "__main__":
    s = input()

    # minion_game_first_try(s)
    minion_game(s)
