import re
import traceback
from typing import List, Set

METHOD_LIST = ["discard", "pop", "remove"]


def get_expression(obj: Set[int], command: str, values: List[str]) -> str:
    stack = traceback.extract_stack()
    _, _, _, code = stack[-2]

    st_name = re.findall(r"[\w]+(?=[,\)])", code)[0]

    expression = f"{st_name}.{command}({', '.join(values)})"

    return expression


if __name__ == "__main__":
    N = input()

    st = set(map(int, input().split()))
    n_commands = int(input())

    for _ in range(n_commands):
        command, *value = input().split()

        if command in METHOD_LIST:
            expression = get_expression(st, command, value)
            eval(expression)
        else:
            raise Exception(f"{repr(command)} is an invalid command.")

    print(sum(st))
