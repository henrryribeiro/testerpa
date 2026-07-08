import pandas as pd
# Manipula arquivos Excel


def read_excel(file_path):
    # Lê a planilha
    dataframe = pd.read_excel(file_path)

    # Converte cada linha em um dicionário
    return dataframe.to_dict(orient="records")