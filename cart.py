class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name, str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price*self.item_quantity))

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, ItemToRemove):
        count = 0
        try:
            for i in range(0,len(self.items)):
                if self.cart_items[i].item_name == ItemToRemove:
                    self.cart_items.pop(i)
                    count += 1
                    break
            if count == 0:
                print("Item not Found")
        except ValueError:
            print("Item not found.")

    def modify_item(self, ItemToModify):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == ItemToModify:
                    print("Item current details:")
                    print(self.cart_items[i].item_description)
                    print(self.cart_items[i].item_price)
                    print(self.cart_items[i].item_quantity)
                    ans = input("Update description y/n: ")
                    if ans == "y":
                        self.cart_items[i].item_description = str(input("Enter description: "))
                    ans = input("Update price y/n: ")
                    if ans == "y":
                        self.cart_items[i].item_price =float(input("Enter price: "))
                    ans = input("Update quantity y/n: ")
                    if ans == "y":
                        self.cart_items[i].item_quantity =int(input("Enter quantity: "))
                    break
            else:
                print("Item not found in cart.")
            
    def get_num_items_in_cart(self):
        count = 0
        for i in range(len(self.cart_items)):
            count += self.cart_items[i].item_quantity
        print("Total number of items is", count)

    def get_cost_of_cart(self):
        cost = 0
        for i in range(len(self.cart_items)):
            cost += self.cart_items[i].item_quantity * self.cart_items[i].item_price
        print("Total price of items is $", cost)
    
    def print_total(self):
        if len(self.items)==0:
            print("SHOPPING CART IS EMPTY")
        else:
            cost = 0
            print("John Doe's Shopping Cart - February 1, 2020")
            self.get_num_items_in_cart()
            for i in range(len(self.cart_items)):
                print(self.cart_items[i].item_name, self.cart_items[i].item_quantity, "@ $", self.cart_items[i].item_price, "=", round(self.cart_items[i].item_quantity * self.cart_items[i].item_price,2) )
                cost += self.cart_items[i].item_quantity * self.cart_items[i].item_price
            print("Total price of items is $", round(cost,2))

    def print_descriptions(self):
        if len(self.cart_items) > 0:
            print("John Doe's Shopping Cart - February 1, 2020")
            print("Item Descriptions")
            for i in range(len(self.cart_items)):
                print(self.cart_items[i].item_name + ": ", self.cart_items[i].item_description)


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

print("Total: $" + str(item1.item_quantity*item1.item_price+item2.item_quantity*item2.item_price))