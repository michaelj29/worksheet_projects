from customer import Customer
from product import Product

shopper1 = Customer("Michael")

print(shopper1.name)
print("-------------------")
print(shopper1.cart.add_to_cart())
print("-------------------")
print(shopper1.cart.add_to_cart())
print("-------------------")
print(shopper1.cart.current_items)
print("-------------------")
print(f'Your total is ${shopper1.cart.cart_total()}')
print("-------------------")
shopper1.cart.empty_cart()
print(shopper1.cart.current_items)
print("-------------------")
