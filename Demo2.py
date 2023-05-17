class Item:

  def __init__(self):
    self.item_dic = {}

  def add_item(self, product_name, price, quantity, discount):
    self.item_dic[product_name] = [price, quantity, discount]

  def update_product(self, info_to_update, name_of_product, new_value):
    if self.item_dic.__contains__(name_of_product):
      if info_to_update == 'name':
        product_info = self.item_dic[name_of_product]
        del self.item_dic[name_of_product]
        self.item_dic[new_value] = product_info
      elif info_to_update == 'quantity':
        new_value = int(new_value)
        product_info = self.item_dic[name_of_product]
        price_per_item = product_info[0]/product_info[1]
        product_info[1] = new_value
        product_info[0] = price_per_item * new_value
        self.item_dic[name_of_product] = product_info
      elif info_to_update == 'discount':
        new_value = int(new_value)
        product_info = self.item_dic[name_of_product]
        product_info[2] = new_value
        self.item_dic[name_of_product] = product_info
    else:
      print("Product does not exist")

  def remove_product(self, name_of_product):
    if self.item_dic.__contains__(name_of_product):
      del self.item_dic[name_of_product]
    else:
      print("Product does not exist")


  def display_items(self):
    for item in self.item_dic:
      info = self.item_dic[item]
      output = "\n" + "Name: " + item \
      + "\n" + "Total Price: " + str(info[0]) \
      + "\n" + "Quantity: " + str(info[1]) \
      + "\n" + "Discount: " + str(info[2]) \

      print(output)


myBasket = Item()

while True:
  feature = input("Enter (a)dd, (u)pdate, (r)emove, (d)isplay, (q)uit: ")
  if feature == 'a':
    name = input("Enter product name: ")
    price = input("Enter product total price: ")
    quantity = input("Enter product quantity: ")
    discount = input("Enter discount(Discount will be applied at check-out): ")

    myBasket.add_item(name, int(price), int(quantity), int(discount))

  elif feature == 'u':
    info_to_update = input("Enter info to update('name', 'quantity', 'discount'): ")
    name = input("Enter product name: ")
    new_value = input("Enter new value: ")
    myBasket.update_product(info_to_update, name, new_value)

  elif feature == 'r':
    name = input("Enter product name to remove: ")
    myBasket.remove_product(name)

  elif feature == 'd':
    myBasket.display_items()

  elif feature == 'q':
    print("Goodbye!")
    break