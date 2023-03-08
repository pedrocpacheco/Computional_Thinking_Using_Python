peso = float(input("Quanto você pesa? "))
altura = float(input("Qual a sua altura? "))


imc = peso / (altura * altura)
print("Seu imc é: " + str(imc))