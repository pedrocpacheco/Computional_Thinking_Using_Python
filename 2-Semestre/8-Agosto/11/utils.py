def parse_float(value):
    try:
        result = float(value)
        return result
    except ValueError:
        print("Informe um número valido")

def get_file_content(file_path):
    try:
        with open(file_path) as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print("Arquivo não encontrado")