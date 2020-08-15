def count_substring(string, sub_string):
    count = start = 0
    while True:
        # `str.find()` returns `-1` if `sub_string` is not found.
        start = string.find(sub_string, start) + 1
        if start > 0:
            count += 1
        else:
            return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
