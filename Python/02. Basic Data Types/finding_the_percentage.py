from statistics import mean

if __name__ == "__main__":
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        student_marks[name] = list(map(float, line))

    query_name = input()

    print(f"{mean(student_marks[query_name]):.2f}")
