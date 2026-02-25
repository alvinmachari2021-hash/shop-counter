import os
from shop_counter.sales import buy_item
from shop_counter.data import products


def reset_state():
    products["apple"]["stock"] = 50
    products["banana"]["stock"] = 100
    products["milk"]["stock"] = 20
    if os.path.exists("sales_history.json"):
        os.remove("sales_history.json")

def test_buy_item_success():
    reset_state()
    buy_item("apple", 5)
    assert products["apple"]["stock"] == 45
    
    with open("sales_history.json", "r") as f:
        content = f.read()
    assert '"item": "apple"' in content
    assert '"quantity": 5' in content

def test_buy_item_insufficient_stock():
    reset_state()
    buy_item("milk", 50)
    assert products["milk"]["stock"] == 20
    assert not os.path.exists("sales_history.json")  

def test_buy_item_invalid_product():
    reset_state()
    buy_item("orange", 1)
    assert not os.path.exists("sales_history.json")