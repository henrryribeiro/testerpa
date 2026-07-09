from src.downloader import download_file
from src.excel_reader import read_excel
from src.browser import create_driver
from src.uibank import UiBankPage

# URL para download da planilha
spreadsheet_url = (
    "https://docs.google.com/spreadsheets/d/"
    "1FJeNr6pSydj4dNNmjklWWDsdUiCo55Uw/"
    "export?format=xlsx"
)

# URL do formulário do UiBank
loan_url = "https://uibank.uipath.com/loans/apply"

# Caminho da planilha
file_path = "files/planilha.xlsx"

# Baixa a planilha
download_file(
    spreadsheet_url,
    file_path
)

# Lê os dados da planilha
loan_requests = read_excel(
    file_path
)

# Exibe quantas solicitações foram carregadas
print(
    f"{len(loan_requests)} solicitações carregadas."
)

# Cria o navegador
driver = create_driver()

# Cria a página do UiBank
page = UiBankPage(driver)

# Lista para armazenar os resultados
results = []

# Processa todas as solicitações
for request in loan_requests:

    # Abre o formulário
    driver.get(loan_url)

    # Preenche o formulário
    page.fill_form(request)

    # Envia a solicitação
    page.submit()

    # Captura o resultado
    result = page.get_result()

    # Adiciona informações da planilha ao resultado
    result["Email"] = request["Email do Solicitante"]
    result["Valor"] = request["Montante do Empréstimo"]
    result["Prazo"] = request["Termo do Empréstimo"]

    # Armazena o resultado
    results.append(result)

    # Exibe o resultado da solicitação
    print(result)

# Exibe um resumo ao final
print("\n========== RESUMO DAS SOLICITAÇÕES ==========")

for result in results:
    print(result)

# Fecha o navegador
driver.quit()

print("\nAutomação finalizada com sucesso!")