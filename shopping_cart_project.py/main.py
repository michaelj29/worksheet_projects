from customer import Customer

def customers_info(name):
  customers_details = Customer(name)
  customers_name = customers_details.name

  print(f'{customers_name}')
  print("-------------------")
  print(customers_details.cart.add_to_cart())
  print("-------------------")
  print(customers_details.cart.add_to_cart())
  print("-------------------")
  print(f'Hi {customers_name} here are your items {customers_details.cart.current_items}')
  print("-------------------")
  print(f'Your total is ${customers_details.cart.cart_total()}')
  print("-------------------")
# customers_details.cart.empty_cart()
  print(customers_details.cart.current_items)
  print("-------------------")
  return customers_details


jimme = customers_info("Jimme")
henry = customers_info("Henry")
alfred = customers_info("Alfred")

