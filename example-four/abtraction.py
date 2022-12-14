class Computer():
    def __init__(self):
        # self.max_price = max_price
        self._max_price = 90

    def get_price(self):
        print(self._max_price)

    def change_price(self, price):
        self._max_price = price


computer = Computer()
computer.get_price()

computer.change_price(30)
computer.get_price()
