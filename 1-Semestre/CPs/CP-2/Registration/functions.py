from Store.functions import define_store, print_store_infos

def run_registration():
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
      for store in store_list:
        print_store_infos(store)

    else:
      break