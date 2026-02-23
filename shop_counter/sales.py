from shop_counter.inventory import update_stock
from shop_counter.data import products
import json

def save_sale(item, quantity, total):
    sale = {"item": item, "quantity": quantity, "total": total}
    with open("sales_history.json", "a") as f:
        f.write(json.dumps(sale) + "\n")

def buy_item(item, quantity):
    if update_stock(item, quantity):
        total = products[item]["price"] * quantity
        print(f"✅ You bought {quantity} {item}(s) for {total} KES.")
        save_sale(item, quantity, total)
    else:
        print("❌ Not enough stock or item not found.")