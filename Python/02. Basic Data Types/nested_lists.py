if __name__ == "__main__":
    n = int(input())

    students = [[input(), float(input())] for _ in range(n)]

    second_lowest_score = sorted(set(student[1] for student in students))[1]

    student_names = sorted(
        [str(student[0]) for student in students if student[1] == second_lowest_score],
        key=str.casefold,
    )

    print(*student_names, sep="\n")
