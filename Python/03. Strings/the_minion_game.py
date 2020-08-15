from itertools import islice, tee


def nwise(iterable, n=2):
    iters = tee(
        iterable, n
    )  # `tee` returns `n` independent iterators from a single iterable
    for i, it in enumerate(iters):
        next(
            islice(it, i, i, 1), None
        )  # Advance each independent iterator `i`-steps ahead
    return zip(*iters)  # The `zip` function ensures groups of size `n` only


# Vowels are only defined as AEIOU.
# Here, Y is not considered a vowel.
def minion_game(string):
    for length in range(1, len(string)):
        print(list(nwise(string, length)))


if __name__ == "__main__":
    s = input()
    minion_game(s)
