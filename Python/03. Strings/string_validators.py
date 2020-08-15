def first_solution(s: str) -> None:
    print(any([char.isalnum() for char in s]))  # (a-z, A-Z, 0-9)
    print(any([char.isalpha() for char in s]))  # (a-z, A-Z)
    print(any([char.isdigit() for char in s]))  # (0-9)
    print(any([char.islower() for char in s]))  # (a-z)
    print(any([char.isupper() for char in s]))  # (A-Z)


def second_solution(s: str) -> None:
    validation_by_char = [
        (char.isalnum(), char.isalpha(), char.isdigit(), char.islower(), char.isupper())
        for char in s
    ]

    final_validation = list(
        map(any, zip(*validation_by_char))
    )  # "Transpose" and apply the `any` function

    print(*final_validation, sep="\n")


if __name__ == "__main__":
    s = input()

    second_solution(s)
