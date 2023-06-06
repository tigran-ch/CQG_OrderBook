"""Test intended to check add_orders function."""

from sources.order import Order
from sources.orderBook import OrderBook

import pytest

def setup_module(module):
    print("setup_module called ONES")

def teardown_module(module):
    print("teardown_module")

class TestAddOrder():

    #@classmethod
    def setup_class(self):
        print("setup_class called ONES")
        #self.orderBook = OrderBook()

    #@classmethod
    def teardown_class(self):
        print("teardown_class called ONES")

    #@pytest.fixture(scope='function', autouse=True)
    #def classSetup(self, create_object):
    #    print("classSetup")

    @pytest.fixture(autouse=True)
    def classTeardown(self, confTeardown):
        print("classTeardown")

    def test_add(self):
        print("Test_1")
        self.orderBook.add_orders([Order("Ask", 55, 5)])
        self.orderBook.print_table()

    def test_subtract(self):
        print("test_2")
        self.orderBook.add_orders([Order("Ask", 51, 1), Order("Bid", 57, 7), Order("Ask", 58, 8)])
        self.orderBook.print_table()
