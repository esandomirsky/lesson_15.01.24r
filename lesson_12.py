class Item:
    def __init__(self, name, price, colour, dimensions):
        self.price = price
        self.colour = colour
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name} - ${self.price}"

class User:

     def __init__(self, name, surname, number_phone):
            self.name = name
            self.surname = surname
            self.number_phone = number_phone

     def __str__(self):
         return f"{self.name} {self.surname} - {self.number_phone}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
         self.products[item] = cnt

    def __str__(self):
        items_str = '\n'.join([f"{item} - {cnt} pcs." for item, cnt in self.products.items()])
        total_str = f"Total order is: {self.get_total()}$"
        return f"User: {self.user}\nItems:\n{items_str}\n{total_str}"
    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

#products
laptop_1 = Item('Asus', 500, "grey", "17 inch", )
laptop_2 = Item('Apple', 2000, "grey", "15 inch", )
mobile_phone_1 = Item('Samsung', 400, "white", "5.6 inch", )
mobile_phone_2 = Item('Nokia', 200, "black", "4.9 inch", )

#buyers
buyer_1 = User("Ivan", "Ivanov", "02628162")
buyer_2 = User("Petr", "Petrov", "05628199")

#oder
cart = Purchase(buyer_1)
cart.add_item(laptop_2, 1)
cart.add_item(mobile_phone_1, 2)
print(cart)
print()

"""
User: Ivan Ivanov
Items:
laptop_2: 1 pcs.
mobile_phone_1: 2 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 2800, "Всього 2800"
assert cart.get_total() == 2800, 'Повинно залишатися 2800!'


cart = Purchase(buyer_2)
cart.add_item(mobile_phone_2, 5)

"""
User: Petr Petrov
Items:
mobile_phone_2: 5 pcs.
"""

assert cart.get_total() == 1000

print('Ok')



