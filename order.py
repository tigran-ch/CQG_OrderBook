class Order():
    def __init__(self, type, price, volume):
        self.__type = type
        self.__price = price
        self.__volume = volume

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_volume(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def get_type(self):
        return self.__type