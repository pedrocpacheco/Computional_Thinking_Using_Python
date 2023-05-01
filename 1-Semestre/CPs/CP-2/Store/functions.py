from Product.functions import define_product, print_product

def define_store(id, name):
  store = {
    "id": id,
    "name": name
  }

  product_list = []
  while(True):
    option = input("What you want to do? \n1- Define Products | 2- Finish Product List \n")
    
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
  print("<Store Info>\n")
  print("-" * 15)
  print(f"Store ID: ", store["id"], "\n")
  print(f"Store Name: ", store["name"], "\n")
  print("Store's Products:")
  for product in store["product_list"]:
    print_product(product)
  print("*" * 15)