if __name__ == "__main__":
    total = int(input())

    total_distinct = len(set(input() for _ in range(total)))

    print(total_distinct)
