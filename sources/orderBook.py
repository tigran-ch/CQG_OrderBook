import json
from sources.order import Order

class OrderBook:

    def __init__(self):
        self.orderBook = dict()

    def __generate_id(self):
        id = 1
        if len(self.orderBook) > 0:
            id = max(list(self.orderBook.keys())) + 1
        return id

    def add_orders(self, orders):
        for order in orders:
            self.orderBook[self.__generate_id()] = order

    def remove_order(self, orderID):
        self.orderBook.pop(orderID)

    def get_order_info(self, orderID):
        print("{:<10} {:<10} {:<10} {:<10}".format("ID", 'Type', 'Price', 'Volume'))
        print("{:<10} {:<10} {:<10} {:<10}".format(orderID, self.orderBook[orderID].get_type(),
                    self.orderBook[orderID].get_price(), self.orderBook[orderID].get_volume()))
        print()

    def set_order_info(self, orderID, price=None, volume=None):
        if price is not None:
            self.orderBook[orderID].set_price(price)
        if volume is not None:
            self.orderBook[orderID].set_volume(volume)

    def dump_snapshot(self):
        snapshot = {"Asks": [], "Bids": []}
        print(self.orderBook)
        for orderID in self.orderBook.keys():
            if self.orderBook[orderID].get_type() == 'Ask':
                snapshot['Asks'].append({'price': self.orderBook[orderID].get_price(), 'volume': self.orderBook[orderID].get_volume()})
            if self.orderBook[orderID].get_type() == 'Bid':
                snapshot['Bids'].append({'price': self.orderBook[orderID].get_price(), 'volume': self.orderBook[orderID].get_volume()})

        snapshot['Asks'] = sorted(snapshot['Asks'], key=lambda x:x['price'])
        snapshot['Bids'] = sorted(snapshot['Bids'], key=lambda x:x['price'], reverse=True)
        print(json.dumps(snapshot, indent=4))

    def print_table(self):
        print("{:<10} {:<10} {:<10} {:<10}".format("ID", 'Type', 'Price', 'Volume'))
        for orderID in self.orderBook.keys():
            print("{:<10} {:<10} {:<10} {:<10}".format(orderID, self.orderBook[orderID].get_type(),
                                                   self.orderBook[orderID].get_price(), self.orderBook[orderID].get_volume()))
        print()


if __name__ == '__main__':
    orderBook = OrderBook()
    orderBook.add_orders([Order("Ask", 55, 5)])
    orderBook.add_orders([Order("Bid", 54, 4), Order("Bid", 53, 3), Order("Bid", 56, 6)])
    orderBook.print_table()
    orderBook.get_order_info(4)
    orderBook.remove_order(4)
    orderBook.print_table()
    orderBook.set_order_info(2, 200, 0)
    orderBook.print_table()
    orderBook.add_orders([Order("Ask", 51, 1), Order("Bid", 57, 7), Order("Ask", 58, 8)])
    orderBook.print_table()
    orderBook.dump_snapshot()

