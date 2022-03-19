from product import Product

class Shopping_cart:
    def __init__(self):
        self.current_items = []
        self.current_items_price = []
        self.total = 0

    def add_to_cart(self):
        new_item = Product(input(f'input item name: '), int(input(f'input item price: ') or 0), input(f'input item category: '))
        self.current_items.append(f'{new_item.name} : {new_item.price}')
        self.current_items_price.append(new_item.price)

    def cart_total(self):
      for item in self.current_items_price:
          self.total += item
      return self.total

    def empty_cart(self):
        self.current_items = []
        self.current_items_price = []
    