"""
cash_register.py: functions as a cash register that maintains 2 list of RetailItem,
            one for available items and one for shopping cart.
            The CashRegister class contains methods to display both lists,
            and add checkout (update available items quantity at same time)
            get_item_by_upc
By: Dillon S.
9/15/26
"""

from csc121.assignments.mod3 import retail_item as rt

class CashRegister:
    def __init__(self, available_items, shopping_cart=None):
        self.__available_items = available_items

        if shopping_cart is None:
            shopping_cart = []

        self.__shopping_cart = shopping_cart

    def get_available_items(self):
        return self.__available_items

    def get_shopping_cart(self):
        return self.__shopping_cart

    def display_available_items(self):
        print("\nAvailable Items:")
        print("-" * 50)

        for item in self.__available_items:
            # Fixed: Properly formatted string fields (:s) vs integer fields (:d)
            print(
                f"UPC: {item.get_upc():10s} "
                f"Description: {item.get_description():20s} "
                f"Price: ${item.get_price():.2f} "
                f"Qty: {item.get_quantity():<5d}"
            )

    def display_shopping_cart(self):
        total = 0
        for item in self.__shopping_cart:
            subtotal = item.get_price() * item.get_quantity()
            total += subtotal
            # Fixed: Added () to execute item.get_quantity()
            print(f"{item.get_description():30s} ${item.get_price():.2f} x {item.get_quantity()}")
        print(f"Cart Total: ${total:.2f}")

    def find_item_by_upc(self, upc):
        for item in self.__available_items:
            if str(item.get_upc()) == str(upc):
                return item

        return None

    def add_item(self, upc):
        item_to_add = self.find_item_by_upc(upc)

        # Safety check for invalid UPCs
        if item_to_add is None:
            print(f"Item with UPC {upc} not found.")
            return

        if item_to_add.get_quantity() <= 0:
            print(f"{item_to_add.get_description()} is out of stock.")
            return

        cart_item = None

        for item in self.__shopping_cart:
            if str(item.get_upc()) == str(upc):
                cart_item = item
                break

        if cart_item:
            cart_item.set_quantity(cart_item.get_quantity() + 1)
        else:
            cart_item = rt.RetailItem(
                item_to_add.get_upc(),
                item_to_add.get_description(),
                item_to_add.get_price(),
                1
            )

            self.__shopping_cart.append(cart_item)

        print(f"{item_to_add.get_description()} added to cart.")

    def remove_item(self, upc):
        cart_item = None

        for item in self.__shopping_cart:
            if str(item.get_upc()) == str(upc):
                # Fixed: Changed == to = for assignment
                cart_item = item
                break

        if cart_item is None:
            print(f"Item {upc} is not in the shopping cart.")
            return

        self.__shopping_cart.remove(cart_item)
        print(f"{cart_item.get_description()} removed from cart.")

    def checkout(self):
        if len(self.__shopping_cart) == 0:
            print("Shopping cart is empty.")
            return

        self.display_shopping_cart()

        confirmation = input("Would you like to checkout? (y/n): ")

        if confirmation.lower() != "y":
            print("Checkout cancelled.")
            return

        for cart_item in self.__shopping_cart:
            available_item = self.find_item_by_upc(cart_item.get_upc())

            if available_item:
                new_quantity = (
                    available_item.get_quantity() - cart_item.get_quantity()
                )

                available_item.set_quantity(new_quantity)

        print("Checkout complete!")
        self.empty_shopping_cart()

    def empty_shopping_cart(self):
        self.__shopping_cart.clear()
        print("Shopping cart emptied.")

def main():
    stock = [
        rt.RetailItem("upc1", "Frozen Pizza", 4.99, 10),
        rt.RetailItem("upc2", "Frozen Spaghetti", 4.39, 5),
        rt.RetailItem("upc3", "Frozen Steak", 4.39, 3),
        rt.RetailItem("upc4", "Crackers", 3.99, 2)
    ]

    cashier = CashRegister(stock)

    while True:
        print("\n===== CASH REGISTER =====")
        print("1. Display available items")
        print("2. Display shopping cart")
        print("3. Add item")
        print("4. Remove item")
        print("5. Checkout")
        print("6. Empty shopping cart")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cashier.display_available_items()

        elif choice == "2":
            cashier.display_shopping_cart()

        elif choice == "3":
            upc = input("Enter UPC to add: ")
            cashier.add_item(upc)

        elif choice == "4":
            upc = input("Enter UPC to remove: ")
            cashier.remove_item(upc)

        elif choice == "5":
            cashier.checkout()

        elif choice == "6":
            cashier.empty_shopping_cart()

        elif choice == "7":
            print("Thanks for using shopping cart!")
            break

if __name__ == "__main__":
    main()