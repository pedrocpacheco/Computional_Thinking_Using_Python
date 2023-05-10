people = input("Quantas pessoas vão no churrasco: ")
value = input("Quanto deu o churrasco: ")

try:
    total = float(value) / int(people)
    print(f"O resultado foi {total}")
except (TypeError, ZeroDivisionError, ValueError):
    print("Não foi digitado um numero")

print("Fim do programa")