
class Student:
    student_number = 0

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if not isinstance(grade, Grade):
            return "please input the type of Grade"
        else:
            self.grades.append(grade)

    def get_average(self):
        total_scores = sum(grade.score for grade in self.grades)
        return total_scores / len(self.grades) if len(self.grades)  else 0

    def has_failing_grade(self):
        return any(not grade.is_passing() for grade in self.grades)

class Grade:
    passing = 60

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        if self.score > Grade.passing:
            return "passing"
        else:
            return "not passing"


if __name__ == "__main__":
    jerry = Student("Jerry", 5)
    grades = [Grade(100), Grade(90), Grade(85), Grade(88), Grade(70)]
    for i in grades:
        jerry.add_grade(i)
    has_failing_grade = jerry.has_failing_grade()
    average_grade = jerry.get_average()
    print(f"Jerry是否有不及格成绩: {has_failing_grade}")
    print(f"Jerry的平均成绩: {average_grade}")




