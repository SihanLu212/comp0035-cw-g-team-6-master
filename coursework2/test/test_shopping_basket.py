import pytest
from shopping_basket import *


def test_add_item_normal(add_item_normal):
    basket, item1 = add_item_normal
    basket.add_item(item1, 1)
    assert len(basket.items) == 1
    assert item1 in basket.items
    assert basket.items[item1] == 1


def test_add_item_negative(add_item_negative):
    basket, item1, quantity = add_item_negative
    basket.add_item(item1, quantity)
    assert len(basket.items) == 0


def test_remove_item_normal(remove_item_normal):
    basket, item1 = remove_item_normal
    basket.remove_item(item1)
    assert len(basket.items) == 0


def test_remove_item_negative(remove_item_negative):
    basket, item1, quantity = remove_item_negative
    basket.remove_item(item1, quantity)
    assert len(basket.items) == 0


def test_update_item_normal(update_item_normal):
    basket, item1, quantity = update_item_normal
    basket.update_item(item1, quantity)
    assert len(basket.items) == 1
    assert item1 in basket.items
    assert basket.items[item1] == 2


def test_update_item_negative(update_item_negative):
    basket, item1, quantity = update_item_negative
    basket.update_item(item1, quantity)
    assert len(basket.items) == 0

def test_view_normal(view_normal):
    basket, item1 = view_normal
    basket.view()
    assert len(basket.items) == 1
    assert item1 in basket.items
    assert basket.items[item1] == 1

if __name__ == '__main__':
    pytest.main()