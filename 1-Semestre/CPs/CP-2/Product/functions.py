def define_product(id, name, description, value):
  product = {
    "id": id,
    "name": name,
    "description": description,
    "value": value
  }
  return product

def print_product(product):
  print(f"Product ID: ", product["id"])
  print(f"Product Name: ", product["name"])
  print(f"Product Description: ", product["description"])
  print(f"Product Value: ", product["value"])