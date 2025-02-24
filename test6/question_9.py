students = [
    {"name": "zs", "age": 18, "score": 87},
    {"name": "ls", "age": 19, "score": 92},
    {"name": "ww", "age": 18, "score": 93},
    {"name": "zl", "age": 18, "score": 87},
]
# 排序
sorted_students = sorted(students, key=lambda student: student["score"], reverse=True)
# 平均分
average_score = sum(student["score"] for student in students) / len(students)
# 输出排序后的学生信息
print("排序后的学生信息：")
for student in sorted_students:
    print(f"姓名: {student['name']}, 年龄: {student['age']}, 成绩: {student['score']}")

# 输出平均分
print(f"\n学生的平均分：{average_score:.2f}")