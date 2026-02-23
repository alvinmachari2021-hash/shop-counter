from shop_counter.inventory import show_products
from shop_counter.sales import buy_item
import json

def load_sales():
    try:
        with open("sales_history.json", "r") as f:
            print("\n--- Past Sales ---")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No past sales found.")

def main():
    while True:
        print("\n--- Shop Counter ---")
        print("1. Show Products")
        print("2. Buy Item")
        print("3. View Sales History")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            item = input("Enter product name: ")
            qty = int(input("Enter quantity: "))
            buy_item(item, qty)
        elif choice == "3":
            load_sales()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()