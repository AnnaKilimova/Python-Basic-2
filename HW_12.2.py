class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f'{self.name}, price: {self.price}'

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'{self.name} {self.surname}'

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        items = ''
        for item, cnt in self.products.items():
            items += f'{str(item.name)}: {cnt} pcs. \n'
        return f'''User: {self.user}
Items:
{items}
'''
    def get_total(self):
        self.total = 0
        for key, cnt in self.products.items():
            self.total += key.price * cnt
        return self.total

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
assert cart.get_total() == 40
print('ok')



