
# Criando uma Lista
items = ['Pedro', 'Luane']
print(items)

# Metodos de uma Lista
items.append('Kaua')
print(items)

items.remove("Pedro")
print(items)

items.insert(2, 'Daniel')
print(items)

items.pop()
print(items)

# Listas dentro de listas                 
series = ["Breaking Bad", "Prison Break", ["The Walking Dead", "Fear The Walking Dead", "The Walking Dead Summit"]]
print(series[2][0]) # o item 3 de series é uma lista de TWD, o item 1 de TWD é The Walking Dead

# For com Listas
games = ["Red Dead Redemption 2", "Cyberpunk 2077", "Tales From Borderlands"]

for game in games:
  print ("Game " + game)

# While com Listas
number = 1 
while number <= 10:
    print("Chegando em 10, falta pouco! Já estamos em: " + str(number))
    number += 1  