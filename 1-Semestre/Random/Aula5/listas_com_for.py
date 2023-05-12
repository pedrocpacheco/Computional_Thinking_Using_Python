# For com Listas
games = ["Red Dead Redemption 2", "Cyberpunk 2077", "Tales From Borderlands"]
names = ["Pedro", "Daniel", "Kauã"]

for game in games:
  print ("Game " + game)

# Break Com for
for name in names:
  if not name == "Daniel": 
    print(name)
  else:
    break # o break para o laço de repetição

# Continue com For
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
  print("Inicio do Laço")
  if number % 2 == 0: # vendo se o numero é par
    continue # o continue volta o laço desde o começo
                
  print(number) # só serão impressos os numeros impares
                # Pois se o numero for par, ele parara no continue 
                # o laço vai voltar pra cima