class Student:
    student_number = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_number += 1

    @classmethod
    def get_students_number(cls):
        return cls.student_number


if __name__ == "__main__":
    student1 = Student("Alice", 20)
    student2 = Student("Bob", 22)
    student3 = Student("Tom", 23)

    print(Student.get_students_number())
