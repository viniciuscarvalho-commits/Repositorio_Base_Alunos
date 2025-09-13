import requests

# Solicitar os dados de entrada
cep = input("Digite o CEP (somente números): ").strip()

# Informar a URL
url = f"https://viacep.com.br/ws/{cep}/json/"

# Fazer a requisição
resposta = requests.get(url)

# Verificar o status da requisição
if resposta.status_code == 200:
    dados = resposta.json()
    if "erro" not in dados:
        print(f"CEP: {dados['cep']}")
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    else:
        print("CEP não foi encontrado.")
else:
    print(f"Erro na requisição. Código: {resposta.status_code}")

