#primeira parte do teste, fazer o download do arquivo.

import requests
import os


def download_file(url, output_path):

    response = requests.get(url)

    response.raise_for_status()

    with open(output_path, "wb") as file:
        file.write(response.content)

    if os.path.exists(output_path):
        print("Arquivo salvo:", output_path)
    else:
        print("Falha no download")