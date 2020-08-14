def is_leap(year):
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return leap


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))
