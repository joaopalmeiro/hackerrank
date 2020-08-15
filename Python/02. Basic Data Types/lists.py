import re
import traceback
from typing import List

METHOD_LIST = [
    func
    for func in dir(list)
    if callable(getattr(list, func)) and not func.startswith("__")
]


def get_expression(obj: List[int], command: str, values: List[str]) -> str:
    stack = traceback.extract_stack()
    _, _, _, code = stack[-2]

    arr_name = re.findall(r"[\w]+(?=[,\)])", code)[0]

    expression = f"{arr_name}.{command}({', '.join(values)})"

    return expression


if __name__ == "__main__":
    N = int(input())
    result_arr: List[int] = []

    for _ in range(N):
        command, *values = input().split()

        if command in METHOD_LIST:
            expression = get_expression(result_arr, command, values)
            eval(expression)
        elif command == "print":
            # print(result_arr)
            exec(f"print({result_arr})")
        else:
            raise Exception(f"{repr(command)} is an invalid command.")
