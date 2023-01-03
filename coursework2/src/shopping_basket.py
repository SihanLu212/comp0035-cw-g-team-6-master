# Write unit tests that test aspects of this class. You may modify the code or extend it by adding additional
# attributes and methods. The code has not been tested and may contain bugs.
"""
编写测试该类各方面的单元测试。您可以修改代码或通过添加额外的内容来扩展它。
属性和方法。代码没有经过测试，可能包含错误。
"""
import decimal
from decimal import Decimal
from reprlib import recursive_repr


class Item(object):
    """A simple item that may be purchased in the shop.

        Attributes:
            brand_name (str): The name of the brand or manufacturer of the item
            product_name (str): The name of the item
            description (str): A short description of the item
            price (Decimal): Price per unit of the item
    """

    def __init__(self, brand_name: str, product_name: str, description: str, price: Decimal):
        """ Constructor """
        self.brand_name = brand_name
        self.product_name = product_name
        self.description = description
        self.price = price

    def __repr__(self):
        """ String representation of an item object """
        return f" {self.brand_name}, {self.product_name}, {self.description}, {str(self.price)}"


class Basket:
    """A basket to hold shopping items.

        Attributes:
            items (dict): A dictionary of all the items in the shopping basket: {item:quantity}
            checkout (bool): A flag to show whether the basket is in checkout or not, default set to False
        Methods:
            add_item: Adds an item to the basket
            remove_item: Removes an item from the basket or reduces its quantity by 1
            update_item: Updates (increase or decrease) the quantity of an item from the basket
            view: Prints the contents of the basket
            get_total_cost: Calculates the total cost of the basket
            reset: Empties the contents of the basket.
            is_empty: Returns whether the basket is empty or not.

        """

    def __init__(self):
        """ Constructor creates an empty basket that has a checkout status of False """
        self.items = {}
        self.checkout = False

    @recursive_repr()
    def __repr__(self):
        """
        String representation of a basket object. Iterates the list of items and their quantity in the basket.
        """
        return str(self.checkout) + '\n' + '<' + '\n'.join(map(repr, self.items)) + '>'

    def add_item(self, item: Item, quantity: int = 1):
        """ Add an item to the basket

        Args:
            item (Item): item to be added
            quantity (int): the quantity of the item to be added, default is 1

        Returns:
            None

        Raises:
            ValueError: if quantity is an integer less than 0
        """
        try:
            if quantity > 0:
                # Check if the item is already in the shopping basket
                if item in self.items:
                    self.items[item] += quantity
                else:
                    self.items[item] = quantity
            else:
                raise ValueError
        except ValueError:
            print("Invalid operation - Quantity must be a positive number!")

    def remove_item(self, item, quantity=0):
        """ Remove an item from the shopping basket (or reduces its quantity if there is more than one)

        Args:
            item (Item): item to be removed
            quantity (int): the quantity of the item to be added, may be negative, default is 0 (i.e. neither add
            nor remove)

        Returns:
            None
        """
        if quantity <= 0:
            # Remove the item
            self.items.pop(item, None)
        else:
            if item in self.items:
                if quantity < self.items[item]:
                    # Reduce the required quantity for this item
                    self.items[item] -= quantity
                else:
                    # Remove the item
                    self.items.pop(item, None)

    def update_item(self, item, quantity):
        """ Updates the quantity of an item in the shopping basket.

            Args:
                item (Item): item to be removed
                quantity (int): the quantity of the item to be added, may be negative (removes) or positive (increases)

            Returns:
                None
        """
        if quantity > 0:
            self.items[item] = quantity
        else:
            self.remove_item(item)

    def view(self):
        """ Prints the contents of the basket.

        Includes quantity, price and total cost.

        Returns:
            None
        """
        total_cost = 0
        print("---------------------")
        for item in self.items:
            quantity = self.items[item]
            cost = quantity * item.price
            print(" + " + item.brand_name + ' ' + item.product_name + " - " + str(quantity) + " x £" + '{0:.2f}'.format(
                item.price) + " = £" + '{0:.2f}'.format(cost))
            total_cost += cost
        print("---------------------")
        print("Basket total = £" + '{0:.2f}'.format(total_cost))
        print("---------------------")

    def get_total_cost(self):
        """ Calculates the total cost of the basket.

        Multiplies the price by the quantity for each item in the basket.

        Returns:
            total_cost (Decimal) : the total cost of all items in the basket
        """
        total_cost = 0
        for item in self.items:
            quantity = self.items[item]
            cost = quantity * item.price
            total_cost += cost
        return total_cost

    def reset(self):
        """  Empties the contents of the basket. """
        self.items = {}

    def is_empty(self):
        """ Returns whether the basket is empty or not.

            Returns:
                bool : Boolean value, True if empty other False
        """
        return len(self.items) == 0


if __name__ == '__main__':
    # This is to illustrate how to create instances of the objects, you can delete the 'main' function before testing
    # your class
    i1 = Item("Warburtons", "Toastie", "800g white sliced loaf", decimal.Decimal('1.52'))
    i2 = Item("Flora", "Buttery", "Buttery spread", decimal.Decimal('0.89'))
    b = Basket()
    b.add_item(i1, -1)
    b.add_item(i1, 1)
    b.add_item(i2, 2)
    print(b)
    print("----view")
    b.view()
    print("----end")
    print(b.is_empty())
    print(b.get_total_cost())
    b.add_item(i1, 3)
    b.remove_item(i1, 1)
    b.view()  # Expect 3 of item 1
    b.reset()
    print(b.is_empty())  # Expect True
