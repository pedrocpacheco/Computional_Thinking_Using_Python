peso = float(input("Quanto você pesa? "))
altura = float(input("Qual a sua altura? "))


imc = peso / (altura ** 2)
print("Seu imc é: " + str(imc))

if imc > 18.5 and imc < 24.9:
    print("IMC normal")
elif imc > 25 and imc < 29.9:
    print("IMC sobrepeso")
elif imc > 30 and imc < 34.9:
    print("IMC obesidade 1")
elif imc > 35:
    print("IMC obesidade 2")
else:
    print("IMC Abaixo do peso")