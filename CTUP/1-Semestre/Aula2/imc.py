peso = float(input("Quanto você pesa? "))
altura = float(input("Qual a sua altura? "))


imc = peso / (altura ** 2)
print("Seu imc é: " + str(imc))

if imc > 30:
    print("reveja seus habitos")