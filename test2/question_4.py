def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

n = input("请输入最大数：")
n = int(n)
fibonacci(n)
