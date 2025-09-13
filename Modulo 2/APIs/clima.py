# Criar um código que consuma api de clima e informe
# A temperatura e a descrição do clima em um lugar específico

import requests 

cidade = input("Digite o nome da cidade: ").strip()
api_key = "2a1ac38a32354cb7b19133643251408"
url =" https://api.weatherapi.com/v1/current.json"


parametros = {
    "key":api_key,
    "q":cidade,
    "lang" : "pt"
    }

# 3. Fazer a requisição 
resposta = requests.get(url, params= parametros)

# 4. Verificar se a requisição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados ['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'Temperatura na cidade {cidade} é {temperatura}°C.')
    print(f'Descrição: {descricao}')
else: 
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)

