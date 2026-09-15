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
    def __init__(self, available_items, shopping_cart:[]):
        self.__available_items = available_items
        self.__shopping_cart = shopping_cart

    def get_available_items(self):
            return self.__available_items

    def get_shopping_cart(self):
            return self.__shopping_cart

    def display_available_items(self):
            for item in self.__available_items:
                print(f"{item.get_description():30s} ${item.get_price():.2f}")

    def display_shopping_cart(self):
        total = 0
        for item in self.__shopping_cart:
            subtotal = item.get_price() * item.get_quantity()
            total += subtotal
            print(f"{item.get_description():30s} ${item.get_price():.2f}\
                    x {item.get_quantity}")
        print(f"Cart Total: ${total:.2f}")

    # Define a function to find item by upc, to see if its available to add into cart
    def find_item_by_upc(self, upc):
        for item in self.__available_items:
            if item.get_upc() == upc:
                return item
        return None

    # Add a item to the cart
    def add_item(self, upc):
            pass

    def checkout(self):
            if len(self.__shopping_cart) > 0:
                self.display_shopping_cart()
                # Ask user to confirm checkout
                # Update quantity in the available items
                for item in self.__shopping_cart:
                    # available_item = self.find_item_by_upc(item.get_upc())
                    location = self.__available_items.index(item)
                    self.__available_items[location].set_quantity(
                        self.__available_items[location].get_quantity() - item.get_quantity()
                    )

                # Empty the shopping cart
                self.__shopping_cart = []

def main():
    stock = [RetailItem(), RetailItem(), RetailItem()]
    cashier = CashRegister(...)

if __name__ == "__main__":
    main()