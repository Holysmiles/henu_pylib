# 假设的正确用户名和密码
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"


def login_required(func):
    def wrapper(*args, **kwargs):
        attempts = 0
        while attempts < 3:
            username = input("请输入用户名: ")
            password = input("请输入密码: ")
            if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
                print("登录成功！")
                return func(*args, **kwargs)  # 执行目标函数
            else:
                attempts += 1
                print(f"用户名或密码错误，你还有 {3 - attempts} 次机会。")

                # 如果三次都失败，抛出异常或采取其他措施
        print("三次登录尝试均失败，访问被拒绝。")
        return None  # 或者其他你认为合适的返回值

    return wrapper


@login_required
def say_hello(name):
    return f"Hello, {name}!"


say_hello("liuhao")