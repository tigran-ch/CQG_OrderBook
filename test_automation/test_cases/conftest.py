import sys
import pytest

# setting path
sys.path.append('../..')

from sources.orderBook import OrderBook
from sources.order import Order


print ("Reading conftest")
@pytest.fixture(scope='function', autouse=True)
def create_object(request):
    request.cls.orderBook = OrderBook()
    print ("creat_object called befor each function (TEST)")

@pytest.fixture()
def confTeardown(request):
    #request.cls.orderBook = OrderBook()
    print ("confTeardown")
