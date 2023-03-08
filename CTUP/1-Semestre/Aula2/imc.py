peso = input("Quanto você pesa? ")
altura = input("Qual a sua altura? ")

peso = int(peso)
altura = float(altura)

imc = peso / (altura * altura)
imc = str(imc)

print("Seu imc é: " + imc)
