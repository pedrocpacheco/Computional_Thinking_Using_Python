def define_product(id, name, description, value):
  product = {
    "id": id,
    "name": name,
    "description": description,
    "value": value
  }
  return product

def print_product(product):
  print(product["id"], "\n")
  print(product["name"], "\n")
  print(product["description"], "\n")
  print(product["value"], "\n")