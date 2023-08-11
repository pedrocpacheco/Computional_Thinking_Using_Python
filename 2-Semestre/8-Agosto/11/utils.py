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
        
def get_headers(content): 
    headers = content.split(",")
    return headers

def columns_to_dict(headers, content):
    data = {}
    for index, column in enumerate(content):
        header_name = headers[index]
        header_name = header_name.strip('"')
        data[header_name] = column
    return data