from shop_counter.data import products

def show_products():
    print("\nAvailable Products:")
    for item, details in products.items():
        print(
            f"{details['id']} | {item} ({details['brand']}) - "
            f"Category: {details['category']} | Price: {details['price']} KES | "
            f"Stock: {details['stock']} | Warranty: {details['warranty']}"
        )

def update_stock(item, quantity):
    if item in products and products[item]["stock"] >= quantity:
        products[item]["stock"] -= quantity
        return True
    return False