import requests

name = input("Digite seu nome: ").strip()
name_json = requests.get(
    f'http://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}'
).json()

def print_name_info(name_json):
    name = name_json[0]
    print("\n<NAME INFO>\n")
    print("(NORMAL INFOS)")
    print(f"Name: ", name["nome"])
    print(f"Sex: ", name["sexo"])
    print(f"Location: ", name["localidade"])
    print()
    for res in name["res"]:
        print("(RESIDENCIA) ")
        print(f"Periodo Res: ", res["periodo"].strip("[").replace(",", " até "))
        print(f"Frequência Res: ", res["frequencia"])
        print()
    
print_name_info(name_json)
