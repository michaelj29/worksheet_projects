from shopping_cart import Shopping_cart


class Customer:
    def __init__(self, name):
      self.name = name
      self.cart = Shopping_cart()