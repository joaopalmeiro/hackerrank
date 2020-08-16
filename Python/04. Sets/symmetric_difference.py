if __name__ == "__main__":
    M = int(input())
    M_elements = set(map(int, input().split()))

    N = int(input())
    N_elements = set(map(int, input().split()))

    # `symmetric_difference` returns the elements that are in each one but not in both
    print(*sorted(M_elements.symmetric_difference(N_elements)), sep="\n")
