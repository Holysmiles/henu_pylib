def total_salary(hourly_rate, regular_hours, overtime_hours):
    # 验证输入值
    if hourly_rate < 15:
        return "错误：正常工作时薪不能小于15元。"
    if regular_hours < 0 or regular_hours > 40:
        return "错误：每周常规工作时间应在0到40小时之间。"
    if overtime_hours < 0:
        return "错误：加班工作时间不能为负数。"

        # 计算总薪水
    regular_salary = hourly_rate * regular_hours
    overtime_salary = hourly_rate * 1.5 * overtime_hours
    total_salary = regular_salary + overtime_salary

    return f"总周薪为：{total_salary}元"


# 示例输入
hourly_rate = float(input("请输入每小时的薪水："))
regular_hours = float(input("请输入每周的常规工作时间（小时）："))
overtime_hours = float(input("请输入每周的加班工作时间（小时）："))

# 调用函数并显示结果
result = total_salary(hourly_rate, regular_hours, overtime_hours)
print(result)