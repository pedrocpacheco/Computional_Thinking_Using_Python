nomes = []

print("<Bem vindo ao programa>")
print("Digite 1 -> Cadastrar Usuario")
print("Digite 0 -> Sair do Programa")


while True:
    opcao = input("O que você deseja fazer? 1 ou 0? ")
    if opcao == str(0):
        break
    else:
        nome = input("Digite um nome para ser cadastrado: ")
        nomes.append(nome)    

print(nomes)
