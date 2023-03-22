# Tipos de Data 
texto = "esse é um texto" # String - texto
num = 123 # int - numero
ponto_flutuante = 1.5 # float - numero flutuante
print(ponto_flutuante)
booleano = True


# list = ["item 1", "index 1", 3, 3 [4.1, 4.2], 5]
# print(list)

# FOR
for item in lista[0]:
    print("Item -> " + str(item))

# IF
if booleano:
    print("Variavel Booleana é verdadeira")
else:  
    print("Variavel não é verdadeira")

if not booleano:
    print("Variavel não é verdadeira")

#WHILE
valor = 0

while valor < 100:
    valor += 1
    if valor % 2 == 0:
        print("esse numero é par " + str(valor))
        continue
    print("esse valor é impar " + str(valor))

 # Listas
lista = ["meu nome", 12, [1, 2, 3, 4]] 
print(lista)

lista.append("Pedro")
lista.insert(0, "Primeiro item")
item_removido = lista.pop() # remove o item, mas retorna o item removido
lista.remove(12) # remove um item mas precisa do valor especifico