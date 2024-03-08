class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name, str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price*self.item_quantity))


def get_item(item, count):
    print("Item", count)
    while True:
        item_name = input("Enter the item name: ")
        if item_name.strip():
            item.item_name = item_name
            break
        else:
            print("Item name can't be blank. Please try again.")

    while True:
        try:
            item_price = float(input("Enter the item price: "))
            if item_price >= 0:
                item.item_price = item_price
                break
            else:
                print("Item price can't be negative. Please re-enter.")
        except ValueError:
            print("Please enter a valid price as an integer.")

    while True:
        try:
            item_quantity = int(input("Enter the item quantity: "))
            if item_quantity >= 0:
                item.item_quantity = item_quantity
                break
            else:
                print("Item quantity can't be negative. Please re-enter.")
        except ValueError:
            print("Please enter a valid quantity as an integer.")


item1 = ItemToPurchase()
item2 = ItemToPurchase()

get_item(item1,1)
get_item(item2,2)

item1.print_item_cost()
item2.print_item_cost()
