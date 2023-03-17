# Usando parametros na função
def funcao_com_parametros(nome, idade):
    print("Olá, " + nome + "você tem " + str(idade) + " anos de idade?")

funcao_com_parametros("pedro", 17)

# Função com parametro padrão
def funcao_com_parametros_padrao(nome, idade, cidade="São Paulo"):
  print("Olá " + nome + " você tem " + idade + " anos " + " e mora em " + cidade)

funcao_com_parametros_padrao("pedro", "17") # Não precisamos passar o valor de cidade, pois ja tem padrão
funcao_com_parametros_padrao("carlos", "18", cidade="Guarulhos") # Para trocar o padrão, precisamos colocar o cidade=" "