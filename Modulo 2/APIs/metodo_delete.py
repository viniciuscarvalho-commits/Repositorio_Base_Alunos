# Metódo DELETE (excluir)

import requests

url = 'https://jsonplaceholder.typicode.com/posts8'

response = requests.delete(url) # Response é para armazenar nossa requisição

print("Status code", response.status_code)
print("Resposta da API:", response.text) # Retorno deve ser vazio

