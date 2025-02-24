import random
import string

def generate_verification_code(length=6):
    # 定义验证码字符集（大写字母、小写字母、数字）
    characters = string.ascii_letters + string.digits  # 包括大小写字母和数字
    # 随机生成一个指定长度的验证码
    verification_code = ''.join(random.choice(characters) for _ in range(length))
    return verification_code

# 生成并打印一个6位验证码
print(generate_verification_code())
