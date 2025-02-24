
class OutOfStack(Exception):
    def __init__(self, color):
        super(OutOfStack, self).__init__(f'蜡烛{color}已经没有库存啦')


class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock.get(color, 0) <= 0:
            raise OutOfStack(color)
        else:
            self.stock[color] = self.stock[color] - 1
            print(f'{color} 颜色的蜡烛购买成功')


if __name__ == "__main__":
    candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0, 'gray': 0})
    candle_shop.buy('blue')
    candle_shop.buy('gray')




