def read_student_info(file_path):
    students = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            headers = file.readline().strip().split()
            for line in file:
                values = line.strip().split()
                student = dict(zip(headers, values))
                students.append(student)
        return students
    except Exception as e:
        print(f"发生错误: {e}")
        return []


if __name__ == "__main__":
    file_path = "StudentInfo.txt"
    student_list = list(read_student_info(file_path))

    print(student_list)
    for student in student_list:
        print(student)
