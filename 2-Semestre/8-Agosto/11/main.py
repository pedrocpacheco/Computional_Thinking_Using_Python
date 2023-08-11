from utils import get_file_content, parse_float, get_headers

def main(): 
    file_path = input("Informe no seu computador a localização do arquivo: ")
    file_content = get_file_content(file_path)
    if not file_content:
        return
    
    filter_abv = input("Digite o ABV: ")
    filter_abv = parse_float(filter_abv)
    
    if not filter_abv:
        return

    for line in file_content[1:]:
        columns = line.split(",")
        try:
            abv = round(float(columns[2]) * 100, 2)
        except ValueError:
            abv = 0
        
        if abv <= filter_abv:
            print(f"{columns[5]} - ABV: {abv}")
            
main()