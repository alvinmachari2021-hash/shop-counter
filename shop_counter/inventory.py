from shop_counter.data import products

def show_products():
    print("\nAvailable Products:")
    for item, details in products.items():
        print(f"{item} - Price: {details['price']} | Stock: {details['stock']}")

def update_stock(item, quantity):
    if item in products and products[item]["stock"] >= quantity:
        products[item]["stock"] -= quantity
        return True
    return False