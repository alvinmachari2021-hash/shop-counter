from shop_counter.inventory import update_stock
from shop_counter.data import products

def test_update_stock():
    assert update_stock("apple", 2) == True