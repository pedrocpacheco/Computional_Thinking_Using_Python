people = input("Quantas pessoas vão no churrasco: ")
value = input("Quanto deu o churrasco: ")

try:
    total = float(value) / int(people)
    print(f"O resultado foi {total}")
except TypeError:
    print(f"Ocorreu um TypeError")
finally:
    print("Ocorrendo exceção ou não, eu apareço.")

print("Fim do programa")