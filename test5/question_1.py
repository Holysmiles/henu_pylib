import math


class Circe:
    __radius = 0

    def __init__(self, r=0):
        self.__radius = r

    def __del__(self):
        print(f"圆的半径为{self.__radius}")
        print("计算的是圆的面积")

    def set_radius(self, r = 0):
        self.__radius = r

    def area(self):
        return math.pi * self.__radius * self.__radius

    def _str(self):
        return f"半径为{self.__radius}的圆的面积为{self.area()}"

    def __gt__(self, other):
        return self.area() > other.area()


# 创建两个实例
circle1 = Circe(5)
circle2 = Circe(3)

# 验证 SetRadius 方法
circle1.set_radius(10)
circle2.set_radius(7)

# 验证 Area 方法
print(circle1._str())  # 输出: The area of the circle with radius 10 is 314.1592653589793.
print(circle2._str())  # 输出: The area of the circle with radius 7 is 153.93804002589985.

# 验证 _gt_ 方法
print(circle1.__gt__(circle2))  # 输出: True
print(circle2.__gt__(circle1))  # 输出: False