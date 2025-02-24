def menu():
    print("=======好友管理系统=======")
    print("请输入您的选项")
    print("1. 添加好友")
    print("2. 删除好友")
    print("3. 备注好友")
    print("4. 展示好友")
    print("5. 退出")


def add_friend(friends:list):
    print("请输入要添加的好友：")
    name = input()
    original_len = len(friends)
    friends.append(name)
    now_len = len(friends)
    if now_len == original_len + 1:
        print("好友添加成功")
    else:
        print("添加失败")


def del_friend(friends:list):
    name = input("请输入删除好友姓名：")
    original_len = len(friends)
    friends.remove(name)
    now_len = len(friends)
    if now_len == original_len - 1:
        print("好友删除成功")
    else:
        print("添加失败")


def rename_friend(friends:list):
    # 显示当前好友列表
    print("当前好友列表:")
    for friend in friends:
        print(friend, end="  ")
    print()

    # 获取用户输入
    old_name = input("请输入要修改的好友姓名：")
    new_name = input("请输入修改后的好友姓名：")

    # 尝试修改好友姓名
    if old_name in friends:
        # 找到旧名字的位置
        index = friends.index(old_name)
        # 修改为新名字
        friends[index] = new_name
        print("备注成功")
    else:
        print(f"未找到名为'{old_name}'的好友")

    # 显示更新后的好友列表
    print("\n更新后的好友列表:")
    for friend in friends:
        print(friend, end="  ")

    print()


def show_friends(friends:list):
    if len(friends) == 0:
        print("好友列表为空")
    else:
        for friend in friends:
            print(friend, end=" ")

    print()


if __name__ == "__main__":
    friends = []
    while True:
        menu()
        choice = int(input())
        if choice == 1:
            add_friend(friends)
        elif choice == 2:
            del_friend(friends)
        elif choice == 3:
            rename_friend(friends)
        elif choice == 4:
            show_friends(friends)
        elif choice == 5:
            break
        else:
            print("输入非法，请重新输入")
