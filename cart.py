class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        print(self.item_name, str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price*self.item_quantity))

    def quick_item(self):
        while True:
            item_name = input("Enter the item name: ")
            if item_name.strip():
                self.item_name = item_name
                self.item_description = "None"
                self.item_quantity = 0
                self.item_price = 0
                break
            else:
                print("Item name can't be blank. Please try again.")
        

    def get_item(self):
        while True:
            item_name = input("Enter the item name: ")
            if item_name.strip():
                self.item_name = item_name
                break
            else:
                print("Item name can't be blank. Please try again.")

        while True:
            item_description = input("Enter the item description: ")
            if item_description.strip():
                self.item_description = item_description
                break
            else:
                print("Item description can't be blank. Please try again.")
        while True:
            try:
                item_price = float(input("Enter the item price: "))
                if item_price >= 0:
                    self.item_price = item_price
                    break
                else:
                    print("Item price can't be negative. Please re-enter.")
            except ValueError:
                print("Please enter a valid price as an float.")

        while True:
            try:
                item_quantity = int(input("Enter the item quantity: "))
                if item_quantity >= 0:
                    self.item_quantity = item_quantity
                    break
                else:
                    print("Item quantity can't be negative. Please re-enter.")
            except ValueError:
                print("Please enter a valid quantity as an integer.")

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
            for i in range(0,len(self.cart_items)):
                if self.cart_items[i].item_name == ItemToRemove:
                    self.cart_items.pop(i)
                    count += 1
                    break
            if count == 0:
                print("Item not Found")
        except ValueError:
            print("Item not found.")

    def modify_item(self, ItemToModify):
        count = 0
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == ItemToModify:
                    count += 1
                    print("Item current details:")
                    print("Description ", self.cart_items[i].item_description)
                    print("Price ", self.cart_items[i].item_price)
                    print("Quantity ", self.cart_items[i].item_quantity)
                    if self.cart_items[i].item_description == "None" and self.cart_items[i].item_price == 0 and self.cart_items[i].item_quantity == 0:
                        self.cart_items[i].item_description = str(input("Enter description: "))
                        self.cart_items[i].item_price =float(input("Enter price: "))
                        self.cart_items[i].item_quantity =int(input("Enter quantity: "))
                        break
                    else:
                        print("Modify Menu:")
                        print("To modify description, enter d: ")
                        print("To modify price, enter p: ")
                        print("To modify quantity, enter q: ")
                        print("To exit without modifying, enter n: ")
                        ans = input("Enter choice: ")
                        if ans == "d":
                            self.cart_items[i].item_description = str(input("Enter description: "))
                        if ans == "p":
                            self.cart_items[i].item_price =float(input("Enter price: "))
                        if ans == "q":
                            print("CHANGE ITEM QUANTITY")
                            self.cart_items[i].item_quantity =int(input("Enter quantity: "))
                        if ans == "n":
                            print("item not modified")
                            break
                        if ans != "d" or ans != "p" or ans !="q" or ans != "n":
                            print("invalid choice, item not modified, returning to main menu")
                            break
                        break
            else:
                if count== 0:
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
        if len(self.cart_items)==0:
            print("SHOPPING CART IS EMPTY")
        else:
            cost = 0
            print(self.customer_name + "'s Shopping Cart - ", self.current_date)
            self.get_num_items_in_cart()
            for i in range(len(self.cart_items)):
                print(self.cart_items[i].item_name, self.cart_items[i].item_quantity, "@ $", self.cart_items[i].item_price, "=", round(self.cart_items[i].item_quantity * self.cart_items[i].item_price,2) )
                cost += self.cart_items[i].item_quantity * self.cart_items[i].item_price
            print("Total price of items is $", round(cost,2))

    def print_descriptions(self):
        if len(self.cart_items) > 0:
            print(self.customer_name, "-", self.current_date)
            print("Item Descriptions")
            for i in range(len(self.cart_items)):
                print(self.cart_items[i].item_name + ": ", self.cart_items[i].item_description)


def print_menu():
    choice = ""
    while choice != "q":
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Modify item")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = str(input("choose an option: "))
        if choice == "a":
            new_item = ItemToPurchase()
            new_item.quick_item()
            print("ADD ITEM TO CART")
            my_cart.add_item(new_item)
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            item_name = str(input("Name of item to remove: "))
            my_cart.remove_item(item_name)
        elif choice == "c":
            item_name = str(input("Name of item to modify: "))
            my_cart.modify_item(item_name)
        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            my_cart.print_descriptions()
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            my_cart.print_total()
        elif choice == "q":
            print("Quitting the menu.")
        else:
            print("Invalid choice. Please choose a valid option.")

ans = input("do part 1?: ")
if ans == "y":
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    item1.get_item()
    item2.get_item()

    item1.print_item_cost()
    item2.print_item_cost()
    print("Total: $" + str(round(item1.item_quantity*item1.item_price+item2.item_quantity*item2.item_price, 2)))


customer_name = input("Enter customer's name: ")
todays_date = input("Enter today's date: ")

my_cart = ShoppingCart(customer_name, todays_date)

print_menu()
