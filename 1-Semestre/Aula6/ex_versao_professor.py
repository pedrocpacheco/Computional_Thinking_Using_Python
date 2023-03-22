nomes = []

print("<Bem vindo ao programa>")
print("Digite 0 -> Sair do Programa")
print("Digite 1 -> Cadastrar Usuario")



while True:
    opcao = input("O que você deseja fazer? 0 ou 1? ")
    if opcao == str(0):
        break
    nome = input("Digite um nome para ser cadastrado: ")
    nomes.append(nome)    

print(nomes)
