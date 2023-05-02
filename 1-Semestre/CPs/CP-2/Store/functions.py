from Product.functions import define_product, print_product

def define_store(id, name):
  store = {
    "id": id,
    "name": name
  }

  product_list = []
  while(True):
    option = input("What you want to do? \n1- Define New Product | 2- Finish Current Store Product List \n")
    
    if(int(option) != 1):
      break

    product = define_product(int(input("Whats the Product ID? \n")), input("Whats the product name? \n"), input("Whats the product description? \n"), float(input("Whats the value of the product? \n")))
    product_list.append(product)

  store.update({
        "id": id,
        "name": name,
        "product_list": product_list
      }
    )

  return store

def print_store_infos(store):
  print("<Store Info>")
  print(f"Store ID: ", store["id"])
  print(f"Store Name: ", store["name"])
  print("Store's Products:")
  print("=" * 15)
  for product in store["product_list"]:
    print("(Product)")
    print_product(product)
    print("=" * 15)
  print("-" * 15)