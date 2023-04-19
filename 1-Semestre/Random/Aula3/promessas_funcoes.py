# Vamos entender como existem as "promessas" de funções
# Eu que inventei esse termo, tem muito a ve com o C de importar funcao

def funcaoEngloba():
  print("Essa função tem uma função dentro dela")
  funcaoEnglobada()

# Por que não existe erro nesse codigo? Sendo que estamos
# Usando uma função que ainda não foi declarada dentro de outra?
# Não da erro, pois ainda não chamamos a função. Só importa a hora que chamamos ela
# funcaoEngloba() -> daria em erro, pois estamos chamando uma função que tem uma função ainda não declarada

def funcaoEnglobada():
  print("Essa função é englobada")

# As duas funções foram declaradas, então funciona.
funcaoEngloba()
