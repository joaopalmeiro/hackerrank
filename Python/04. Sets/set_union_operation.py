if __name__ == "__main__":
    n_english = int(input())
    english = set(map(int, input().split()))

    n_french = int(input())
    french = set(map(int, input().split()))

    print(len(english.union(french)))
