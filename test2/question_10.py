def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi):

    if bmi < 18.5:
        return "过轻"
    elif 18.5 <= bmi < 24:
        return "正常"
    elif 24 <= bmi < 27:
        return "过重"
    elif 27 <= bmi < 32:
        return "肥胖"
    else:
        return "非常肥胖"

    # 示例：


weight = float(input("请输入您的体重（kg）："))
height = float(input("请输入您的身高（m）："))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"您的BMI指数为：{bmi:.2f}")
print(f"您的体质分类为：{category}")