#Fazendo lista
lista = []
lista.append("item 1")
lista.append("lista 2")

#Fazendo dicionario
dicionario = {
  'first_name': 'Pedro',
  'last_name': 'Pacheco',
  'age': 17
}

# Printando chave first_name
nome = dicionario['first_name']
print(nome)

# Printando chave last_name
sobrenome = dicionario['last_name']
print(sobrenome)

# Printando chave first_name
idade = dicionario['age']
print(idade)

print(dicionario)

# Deletando Chave
del dicionario ['age']
print(dicionario)

# Atualizando dicionario

  # Podemos atualizar direto
dicionario.update({
  'first_name': 'Pedro',
  'last_name': 'Pacheco',
  'age': 17,
  'atualizado': True
})
print(dicionario)

  # Podemos criar outra variavel e atribuir ao dicionario
dicionario_atualizado = {
  'first_name': 'Pedro',
  'last_name': 'Pacheco',
  'age': 17,
  'atualizado': True
}
dicionario.update(dicionario_atualizado)
print(dicionario)

# Loopando por dicionario
for key in dicionario:
  print("Chave:", key)

def criar_usuario():
  first_name = input("Qual seu primeiro nome?")
  last_name = input("Qual seu sobrenome?")
  age = input("Qual sua idade?")
  
  info_usuario = {
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
    u