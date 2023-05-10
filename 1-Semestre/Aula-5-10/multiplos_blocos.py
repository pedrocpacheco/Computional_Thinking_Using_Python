people = input("Quantas pessoas vão no churrasco: ")
value = input("Quanto deu o churrasco: ")

try:
    total = float(value) / int(people)
    print(f"O resultado foi {total}")
except TypeError as exception:
    print(f"Ocorreu um {exception.__class__.__name__}")
except ValueError as exception:
    print(f"Ocorreu um {exception.__class__.__name__}")
except ZeroDivisionError as exception:
    print(f"Ocorreu um {exception.__class__.__name__}")
except Exception as exception:
    print(f"Ocorreu um {exception.__class__.__name__} generico")

print("Fim do programa")