def criar_usuario():
  first_name = input("Qual seu primeiro nome? ")
  last_name = input("Qual seu sobrenome? ")
  age = input("Qual sua idade? ")
  info_usuario = {
    'first_name': first_name,
    'last_name': last_name,
    'first_name': age,
  }
  return info_usuario

def procurar_usuario():
  first_name = input("Digite o nome do usuario que deseja encontrar: ")
  for user in usuarios:
    if user['first_name'] == first_name:
      return user

usuarios = []
while True:
  print("Selecione a Opção Desejada")
  print("1- Cadastrar Usuario")
  print("2- Localizar usuario pelo primeiro nome")
  print("0- Sair")
  option = int(input(""))
  if option == 0:
    print(usuarios)
    break
  elif option == 1:
    usuarios.append(criar_usuario())
    continue
  print(usuarios)
    