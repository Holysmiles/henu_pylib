money = input("请输入金额：")
length = len(money)
money = int(money)
arr = [0,0,0,0,0]
for i in range(length):
    arr[i] = money % 10
    money = int(money / 10)

print(f'{arr[4]} 萬 {arr[3]} 仟 {arr[2]} 佰 {arr[1]} 什 {arr[0]} 元')
