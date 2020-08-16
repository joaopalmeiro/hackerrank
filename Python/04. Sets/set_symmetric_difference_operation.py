if __name__ == "__main__":
    n_english = int(input())
    english = set(map(int, input().split()))

    n_french = int(input())
    french = set(map(int, input().split()))

    # `symmetric_difference` returns the elements that are in each one but not in both
    print(len(english.symmetric_difference(french)))
