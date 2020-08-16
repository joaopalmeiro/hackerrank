import re
import traceback
from typing import Set

METHOD_LIST = [
    func
    for func in dir(set)
    if callable(getattr(set, func)) and func.endswith("update")
]


def get_expression(obj: Set[int], command: str, values: Set[int]) -> str:
    stack = traceback.extract_stack()
    _, _, _, code = stack[-2]

    st_name = re.findall(r"[\w]+(?=[,\)])", code)[0]

    expression = f"{st_name}.{command}({values})"

    return expression


if __name__ == "__main__":
    n_A = int(input())
    A = set(map(int, input().split()))

    n_sets = int(input())

    for _ in range(n_sets):
        command, n_set = input().split()

        if command in METHOD_LIST:
            expression = get_expression(A, command, set(map(int, input().split())))
            eval(expression)
        else:
            raise Exception(f"{repr(command)} is an invalid command.")

    print(sum(A))
