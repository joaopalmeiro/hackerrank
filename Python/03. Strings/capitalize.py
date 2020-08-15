def solve(s: str) -> str:
    # Explicitly define `sep` with a whitespace character to ensure that
    # only a single whitespace character is used to break the string.
    name = " ".join(map(str.capitalize, s.split(sep=" ")))
    return name


if __name__ == "__main__":
    s = input()

    result = solve(s)

    print(result)
