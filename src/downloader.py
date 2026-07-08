#primeira parte do teste, fazer o download do arquivo.

import requests
# Realiza requisições HTTP


def download_file(url, destination):
    # Faz o download da planilha
    response = requests.get(url)

    # Salva o arquivo no computador
    with open(destination, "wb") as file:
        file.write(response.content)

    # Confirma o download
    print(f"Arquivo salvo: {destination}")
