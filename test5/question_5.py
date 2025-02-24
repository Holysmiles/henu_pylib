# class Animal:
#     count = 0
#
#     # 构造器
#     def __init__(self):
#         Animal.count += 1
#
#     # 实例方法
#     def call(self):
#         pass
#
#     # 实例方法
#     def run(self):
#         pass
#
#     # 类方法
#     @classmethod
#     def class_method_1(cls):
#         pass
#
#     # 类方法
#     @classmethod
#     def class_method_2(cls):
#         pass
#     # 类方法
#
#     @classmethod
#     def class_method_3(cls):
#         pass
#
#     # 类方法
#     @classmethod
#     def class_method_4(cls):
#         pass
#
#     # 静态方法
#     @staticmethod
#     def static_func_1(self):
#         pass
#
#     # 静态方法
#     @staticmethod
#     def static_func_2(self):
#         pass
#
#     # 静态方法
#     @staticmethod
#     def static_func_3(self):
#         pass
#
#
# # 定义统计函数
# def func(*args):
#     function_count = 0 # 函数
#     method_count = 0 # 方法
#     animal_count = Animal.count # 对象
#
#     for arg in args:
#         if isinstance(arg, Animal):
#             # 如果是Animal对象，则不增加方法或函数的计数
#             continue
#         elif callable(arg):
#             # 如果是可调用的（方法或函数），则判断是否是类方法或静态方法
#             if isinstance(arg, classmethod) or isinstance(arg, staticmethod):
#                 method_count += 1
#             else:
#                 function_count += 1
#
#     return f"方法个数：{method_count}, 函数个数：{function_count}, Animal对象个数：{animal_count}"
#
#
# # 创建Animal对象
# a1 = Animal()
# a2 = Animal()
#
# # 调用统计函数
# result = func(a1, a1, a2, a2, a2, a1.call(), a1.run(), Animal.class_method_1(), Animal.class_method_2(),)
# result_1 = func(a1, Animal.class_method_3(), Animal.class_method_4(), Animal.static_func_1(a1), Animal.static_func_2(a1), Animal.static_func_3(a1))
# print(result)
# print(result_1)
class Animal:
    # 类变量，用于统计Animal对象的数量
    instance_count = 0

    def __init__(self):
        # 每创建一个实例，计数器增加
        Animal.instance_count += 1

    # 实例方法
    def func1(self):
        pass

    def func2(self):
        pass

    # 类方法
    @classmethod
    def func3(cls):
        pass

    @classmethod
    def func4(cls):
        pass

    # 静态方法
    @staticmethod
    def func5():
        pass

    @staticmethod
    def func6():
        pass

# 定义统计函数
def func(*args):
    method_count = 0
    function_count = 0
    animal_count = Animal.instance_count

    for arg in args:
        if isinstance(arg, Animal):
            # 如果是Animal对象，则不增加方法或函数的计数
            continue
        elif callable(arg):
            # 如果是可调用的（方法或函数），则判断是否是类方法或静态方法
            if isinstance(arg, classmethod) or isinstance(arg, staticmethod):
                method_count += 1
            else:
                function_count += 1

    return f"方法个数：{method_count}, 函数个数：{function_count}, Animal对象个数：{animal_count}"

# 创建Animal对象
a1 = Animal()
a2 = Animal()

# 调用统计函数
result = func(a1, a1, a1, a2, a2, a2, a1.func1, a1.func2, Animal.func3, Animal.func4)
print(result)


