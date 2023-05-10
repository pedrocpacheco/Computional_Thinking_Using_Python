def create_users(users):
    if not isinstance(users, list):
        raise TypeError("Precisa ser uma lista")
    if not users:
        raise ValueError("Não pode ser nulo")
    print(users)

users = ["Pedro", "Thiago"]

try:
    create_users(users) # Funciona, pois uma lista esta sendo passada
except TypeError as ex:
    print(ex)

try:
    create_users("Pedro") # Exceção Lançada, pois não passamos uma Lista
except TypeError as ex:
    print(ex)

users_empty = []

try:
    create_users(users_empty)
except TypeError as ex:
    print(ex)
