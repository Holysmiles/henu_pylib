# print("两全   美")
# print("    乐")
# print("    无")
# print("    穷")
str1 = '两全  美'
str2 = '乐\n\t无\n\t穷'
print(str1)
print('\t' + str2)
instr = input("请输入正确汉字，使上下成语成立：")
str_arr = str1.split(" ")
str1 = str_arr[0] + instr + str_arr[2]
print(str1)
print('\t' + str2)




