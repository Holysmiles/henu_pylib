print("请输入个人信息（姓名、性别、年龄、宿舍号、学院、专业、电话信息）：")
name = input("请输入姓名：")
gender = input("请输入性别：")
age = input("请输入年龄：")
dormitory_number = input("请输入宿舍号：")
college = input("请输入学院：")
major = input("请输入专业：")
tel = input("请输入电话信息：")
information = []
information.append(name)
information.append(gender)
information.append(age)
information.append(dormitory_number)
information.append(college)
information.append(major)
information.append(tel)
title = ["姓名", "性别", "年龄", "宿舍号", "学院", "专业", "电话信息"]
student = zip(title, information)
# print(type(student))  <class 'zip'>
student = dict(student) # 返回的是zip格式，需要强转
print()
for k, v in student.items():
    print(k +": " + v)