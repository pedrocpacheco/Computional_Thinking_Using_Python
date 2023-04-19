nomes = []

print("<Bem vindo ao programa>")
print("Digite 1 -> Cadastrar Usuario")
print("Digite 0 -> Sair do Programa")

opcao = input("Digite sua opcao: ")

while opcao == str(1):
    nome = input("Digite um nome para ser cadastrado: ")
    nomes.append(nome)
    resposta = input("O que você deseja fazer agora? 1 ou 0? ")
    if resposta == str(1):
        continue
    else:
        break

print(nomes)
