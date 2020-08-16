if __name__ == "__main__":
    _ = input()
    arr = list(map(int, input().split()))
    like = set(map(int, input().split()))
    dislike = set(map(int, input().split()))

    print(sum((i in like) - (i in dislike) for i in arr))
