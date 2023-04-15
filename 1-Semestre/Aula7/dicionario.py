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
last_name = example_dictionary['last_name']
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
print(dicionario)

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
  first_name = input("Qual seu primeiro nome?")
  last_name = input("Qual seu last_name?")
  age = input("Qual sua idade?")
  
  user_info = {
    'first_name': first_name,
    'last_name': last_name,
    'first_name': age,
  }

usuario = []
while True:
  print("Selecione a Opção Desejada")
  print("1- Cadastrar Usuario")
  print("2- Localizar usuario pelo primeiro nome")
  print("0- Sair")
  option = int(input(""))
  if option == 0:
    break
  elif option == 1:
    return;