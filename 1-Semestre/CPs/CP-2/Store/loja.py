def define_product(id, name, description, value):
  product = {
    "id": id,
    "name": name,
    "description": description,
    "value": value
  }
  return product

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
    

def run_program():
  store_list = []
  while(True):
    option_menu = int(input("What do you want to do? \n1- Define Stores | 2- Print The Store Info | 3- Exit \n"))
    if(option_menu == 1):
      while(True):
        option_stores = int(input("What do you want to do? \n1- Define New Store | 2- Get back to menu \n"))
        if(option_stores == 2):
          break
        id = int(input("Whats the new store id? \n"))
        name = input("Whats the new store name? \n")
        store = define_store(id, name) 
        store_list.append(store)
    elif(option_menu == 2):
      print(store_list) 
    else:
      break   

run_program()