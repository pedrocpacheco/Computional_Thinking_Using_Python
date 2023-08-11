file_path = input("Indique no seu computador a localização do arquivo")

try: 
    with open(file_path) as file:
        filter_abv = None
        try:
            filter_abv = float(input("Digite o ABV"))
        except:
            print("Informe um numero")
        if filter_abv:
            lines = file.readlines()
            for line in lines[1:]:
                columns = lines.split(",")
                try:
                    abv = round(float(columns[2] * 100, 2))
                except ValueError:
                    abv = 0
                if abv <= filter_abv:
                    print(f"{columns[5]} - ABV: {abv}")
except FileNotFoundError:
    print("Arquivo não encontrado")