class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return f"Student(name='{self.name}', score={self.score})"

def main():
    # add stu
    stu_list = [
        Student('Lucy', 99),
        Student('liuhao', 100),
        Student('Mike', 90),
        Student('Trump', 99),
        Student('Kamala', 80)
    ]

    stu_list_sort = sorted(stu_list, key=lambda student: student.score)
    highest_score = stu_list_sort[-1]
    lowest_score = stu_list_sort[0]

    stu_list_sort.remove(highest_score)
    stu_list_sort.remove(lowest_score)

    stu_list_copy = stu_list_sort.copy()
    stu_list_copy.reverse()

    print("翻转后的学生列表:")
    for student in stu_list_copy:
        print(student)


if __name__ == "__main__":
    main()



