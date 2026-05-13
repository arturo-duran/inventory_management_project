class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = {}

    # 1 add item
    def add_item(self, name, quantity):
        item = Item(name, quantity)
        self.items[name] = item

    # 2 remove item
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print("Item removed")
        else:
            print("Item not found in inventory")

    # 3 show item
    def show_items(self):
        for item in self.items.values():
            print(f"\n{item.name}, quantity:{item.quantity}")

    # 4 edit item
    def edit_item(self, name, quantity):
        if name in self.items:
            self.items[name] = Item(name, quantity)
            print("\nItem edited")
        else:
            print("\nItem not found in inventory")

    # 5 search item
    def search_item(self, name):
        if name in self.items:
            item = self.items[name]
            print(f"\n {item.name}, quantity:{item.quantity}")
            return self.items[name]
        else:
            print("Item not found in inventory")

    def sort_item(self):
        print("\nSorting Options:")
        print("1. Alphabetical")
        print("2. Quantity")

        choice = input("Enter your sorting method: ")

        if choice == "1":
            sorted_items = sorted(self.items.values(), key=lambda item: item.name)
        elif choice == "2":
            sorted_items = sorted(self.items.values(), key=lambda item: item.quantity)
        else:
            print("Invalid Choice")
            return
        for item in sorted_items:
            print(f"\n {item.name}, quantity:{item.quantity}")


def main():
    inventory = Inventory()

    while True:
        print("\n****Inventory Menu****")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Edit Items")
        print("4. Sort Item")
        print("5. Search")
        print("6. Show Items")
        print("Type q to quit")

        choice = input("Enter your choice: ")

        # 1 add item
        if choice == "1":
            name = input("Enter Item Name: ")
            quantity = int(input("Enter Item Quantity: "))
            inventory.add_item(name, quantity)

        # 2 remove item
        elif choice == "2":
            name = input("Enter Item Name to Remove: ")
            inventory.remove_item(name)

        # 3 edit items
        elif choice == "3":
            name = input("Enter Item to Edit: ")
            quantity = int(input("Enter Item Quantity: "))
            inventory.edit_item(name, quantity)

        # 4 sort
        elif choice == "4":
            inventory.sort_item()

        # 5 search items
        elif choice == "5":
            name = input("Enter Item Name: ")
            inventory.search_item(name)

         # 6 show items
        elif choice == "6":
            inventory.show_items()

        # q exit
        elif choice == "q":
            print("\nExiting the menu")
            break

        # any other input
        else:
            print("\nInvalid Choice")

if __name__ == "__main__":
    main()