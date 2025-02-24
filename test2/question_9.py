def narcissistic_number(num):
    t = 0
    for i in range(100, 1000):
        i1 = i % 10
        t = int(i / 10)
        i2 = t % 10
        i3 = int(t / 10)
        if i1**3 + i2**3 + i3**3 == i:
            num.append(i)


num = []
narcissistic_number(num)
print(num)