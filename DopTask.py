# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.

class Store():
    def __init__(self, name, address, items={}):
        self.name = name
        self.address = address
        self.items = items


    def add_item(self, item, price):
        if item not in self.items:
            self.items[item] = price
            print(f'{item} was added, price: {price}')
        else:
            print(f'Item "{item}" already exists')


    def delete_item(self, item):
        deleted = self.items.pop(item, None)
        if deleted is None:
            print(f'Item "{item}" is not in list')
        else:
            print(f'{item} was removed from list')


    def price_of_item(self, item):
        return self.items.get(item) # get returns None if key not in dict


    def update_price(self, item, price):
        if item in self.items:
            self.items[item] = price
            print(f'The price of {item} was updated to {price}')
        else:
            print(f'{item} not in the list')


store_one = Store('Num One', 'New York', {'Milk': 30, 'Bread': 25, 'Eggs': 78})
store_two = Store('Num Two', 'Moscow')

londons_list = {
    'Phone': 1500,
    'Laptop': 2000,
    'Cofee Machine': 1300,
    'TV': 900,
    'Sound System': 850
}
store_three = Store('Num Three', 'London', londons_list)


#---------Testing-----------

store_one.add_item('Chips', 140)
store_one.add_item('Lemonade', 100)
store_one.add_item('Chips', 150) # Добавление существующего товара

store_two.add_item('T-shirt', 3000)
store_two.add_item('Dress', 5600)
store_two.add_item('Shoes', 11000)

store_three.delete_item('TV')
store_three.delete_item('Video Player') # Попытка удалить несуществующий товар

print(store_one.price_of_item('Eggs'))
print(store_two.price_of_item('Dress'))
print(store_two.price_of_item('Skirt')) # Попытка узнать цену несуществующего товара
print(store_three.price_of_item('Laptop'))

store_one.update_price('Milk', 40)
store_two.update_price('T-shirt', 3100)
store_three.update_price('TV', 1000) # Попытка изменить цену после удаления товара

