import pytest
from shopping_basket import *

@pytest.fixture
def add_item_normal():
    basket = Basket()
    item1 = Item("Apple", "iPhone", "Latest version of the iPhone", Decimal("1000.00"))
    return basket, item1

@pytest.fixture
def add_item_negative():
    basket = Basket()
    item1 = Item("Apple", "iPhone", "Latest version of the iPhone", Decimal("1000.00"))
    return basket, item1, -1

@pytest.fixture
def remove_item_normal():
    basket = Basket()
    item1 = Item("Apple", "iPhone", "Latest version of the iPhone", Decimal("1000.00"))
    basket.add_item(item1, 1)
    return basket, item1

@pytest.fixture
def remove_item_negative():
    basket = Basket()
    item1 = Item("Apple", "iPhone", "Latest version of the iPhone", Decimal("1000.00"))
    basket.add_item(item1, 1)
    return basket, item1, -1

@pytest.fixture
def update_item_normal():
    basket = Basket()
    item1 = Item("Apple", "iPhone", "Latest version of the iPhone", Decimal("1000.00"))
    basket.add_item(item1, 1)
    return basket, item1, 2

@pytest.fixture
def update_item_negative():
    basket = Basket()
    item1 = Item("Apple", "iPhone", "Latest version of the iPhone", Decimal("1000.00"))
    basket.add_item(item1, 1)
    return basket, item1, -1

@pytest.fixture
def view_normal():
    basket = Basket()
    item1 = Item("Apple", "iPhone", "Latest version of the iPhone", Decimal("1000.00"))
    basket.add_item(item1, 1)
    return basket, item1