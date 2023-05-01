#Fazendo lista
example_list = []
example_list.append("item 1")
example_list.append("lista 2")

#Fazendo dicionario
example_dictionary = {
  'first_name': 'Pedro',
  'last_name': 'Pacheco',
  'age': 17
}

# Printando chave first_name
name = example_dictionary['first_name']
print(name)

# Printando chave last_name
last_name = example_dictionary
print(last_name)

# Printando chave first_name
age = example_dictionary['age']
print(age)

print(example_dictionary)

# Deletando Chave
del example_dictionary ['age']
print(example_dictionary)

# Atualizando dicionario

  # Podemos atualizar direto
example_dictionary.update({
  'first_name': 'Pedro',
  'last_name': 'Pacheco',
  'age': 17,
  'new_version': True
})
print(example_dictionary)

  # Podemos criar outra variavel e atribuir ao dicionario
new_dictionary = {
  'first_name': 'Pedro',
  'last_name': 'Pacheco',
  'age': 17,
  'atualizado': True
}
example_dictionary.update(new_dictionary)
print(example_dictionary)

# Loopando por dicionario
for key in example_dictionary:
  print("Chave:", key)

def create_user():
  first_name = input("Whats your first name?\n")
  last_name = input("Whats your last name?\n")
  age = input("How Old are You?\n")
  
  user_info = {
    'first_name': first_name,
    'last_name': last_name,
    'first_name': age,
  }

  return user_info

user_list = []
while True:
  print("Welcome to the Program! What do you want to do?")
  print("1- Create User")
  print("2- Locate a User by it's name")
  print("0- Exit")
  option = int(input(""))
  if option == 0:
    break
  elif option == 1:
    user_list.append(create_user())
    continue

print(user_list)