import requests  # Importa a biblioteca para fazer requisições HTTP

# Exibe o menu de ações para o usuário
print("== Menu de ações ==")
print("1 - GET (Buscar post)")
print("2 - POST (Criar post)")
print("3 - PATCH (Atualizar título)")
print("4 - DELETE (Apagar post)")

# Lê a opção escolhida pelo usuário
opcao = input("Escolha uma opção (1-4): ")

# === GET ===
if opcao == "1":
    post_id = input("Digite o ID do post: ")  # Solicita o ID do post ao usuário
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"  # Monta a URL

    try:
        r = requests.get(url)  # Faz a requisição GET
        if r.status_code == 200:
            post = r.json()  # Converte a resposta JSON para dicionário
            if post:
                print("Resposta:", post)  # Exibe o post
            else:
                print("Post não encontrado.")
        else:
            print(f"Erro ao buscar o post. Código: {r.status_code}")
    except requests.RequestException as e:  # Corrigido 'request' para 'requests'
        print("Erro de conexão:", e)

# === POST ===
elif opcao == "2":
    url = "https://jsonplaceholder.typicode.com/posts"

    # Cria o dicionário com os dados do novo post
    novo_post = {
        "title": input("Título: "),   # Solicita o título do post
        "body": input("Conteúdo: "),  # Solicita o corpo do post
        "userId": 1                   # Define um usuário fixo
    }

    try:
        r = requests.post(url, json=novo_post)  # Envia os dados usando POST
        if r.status_code in [200, 201]:
            print("Post criado:", r.json())  # Exibe o post criado
        else:
            print("Erro ao criar o post.")
    except requests.RequestException as e:
        print("Erro de conexão:", e)

# === PATCH ===
elif opcao == "3":
    post_id = input("Digite o ID do post que deseja atualizar: ")
    novo_titulo = input("Novo título: ")

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    dados_patch = {
        "title": novo_titulo  # Apenas o campo título será alterado
    }

    try:
        r = requests.patch(url, json=dados_patch)  # Envia PATCH com os dados
        if r.status_code == 200:
            print("Post atualizado:", r.json())  # Exibe a resposta da API
        else:
            print("Erro ao atualizar o post.")
    except requests.RequestException as e:
        print("Erro de conexão:", e)

# === DELETE ===
elif opcao == "4":
    post_id = input("Digite o ID do post que deseja apagar: ")
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        r = requests.delete(url)  # Envia requisição DELETE
        if r.status_code == 200:
            print("Post apagado com sucesso.")
        else:
            print(f"Erro ao apagar o post. Código: {r.status_code}")
    except requests.RequestException as e:
        print("Erro de conexão:", e)

# === Opção inválida ===
else:
    print("Opção inválida. Escolha entre 1 e 4.")
