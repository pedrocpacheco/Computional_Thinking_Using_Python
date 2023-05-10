def calcular():
    number = input("Digite um numero: ")
    try:
        result = int(number) / 2
        print("O resultado foi: ", number)
    except ValueError:
        print("Você fez merda")
        calcular()
    except TypeError:
        print("Tipo errado")
    
calcular()