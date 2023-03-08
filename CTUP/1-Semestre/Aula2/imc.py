from xmlrpc.client import boolean


peso = float(input("Quanto você pesa? "))
altura = float(input("Qual a sua altura? "))


imc = peso / (altura ** 2)
print("Seu imc é: " + str(imc))

if imc > 30:
    print("reveja seus habitos")
elif imc < 10:
    print("você ta sumindo")
else:
    print("você ta tranquilo")

