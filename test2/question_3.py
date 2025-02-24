
name = "qwe"
password = "123"
for i in range(10):
    if i <= 2:
        name_in = input("请输入您的用户名：")
        password_in = input("请输入您的密码：")
        if name == name_in and password == password_in:
            print(f'恭喜{name}')
            break
        else:
            print(f'你还有{2 - i}次机会')
    else:
        print("登陆超时，请明天登录")
        break

