from typing import List


def average(array: List[int]) -> float:
    distinct_values = set(array)

    return sum(distinct_values) / len(distinct_values)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
