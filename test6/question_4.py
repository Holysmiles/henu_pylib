class Goods:
    def __init__(self, name, price):
        self.price = price
        self.name = name

    def __str__(self) -> str:
        return f'Goods(name: {self.name}, price: {self.price})'


def test4(low: float, top: float):
    goods_list = [
        Goods("小米2", 568),
        Goods("罗技M750", 239),
        Goods("雷神K104机械键盘", 368),
        Goods("康普瑞", 435),
        Goods("小米充电宝", 121),
        Goods("华为电容笔", 219),
        Goods("Iphone电容笔", 834),
        Goods("华为nave11se", 1263),
        Goods("绿联扩展坞", 26)
    ]
    select_goods = []
    for goods in goods_list:
        if low <= float(goods.price) <= top:
            select_goods.append(goods)

    if len(select_goods) > 0:
        # 从小到大排序
        price_asc = sorted(select_goods, key=lambda goods: goods.price)
        # 从大到小排序
        price_des = sorted(select_goods, key=lambda goods: goods.price, reverse=True)
        # 计算平均价格
        average_price = sum(goods.price for goods in select_goods) / len(select_goods)

        print("从大到小：")
        for goods in price_des:
            print(goods)  # 这里会调用 __str__ 方法，打印出商品信息

        print("从小到大：")
        for goods in price_asc:
            print(goods)  # 同上，调用 __str__ 方法

        print("平均价格")
        print(average_price)
    else:
        print("没有这个价格范围内的商品")

if __name__ == "__main__":
    test4(20, 300)
