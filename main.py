from src.downloader import download_file
from src.excel_reader import read_excel
from src.browser import create_driver
from src.uibank import UiBankPage


# Link para download da planilha
spreadsheet_url = (
    "https://docs.google.com/spreadsheets/d/"
    "1FJeNr6pSydj4dNNmjklWWDsdUiCo55Uw/"
    "export?format=xlsx"
)

# Caminho onde a planilha será salva
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

# Exibe quantos registros foram carregados
print(
    f"{len(loan_requests)} solicitações carregadas."
)

# Cria o navegador
driver = create_driver()

# Acessa a página do UiBank
driver.get(
    "https://uibank.uipath.com/loans/apply"
)

# Cria a página do formulário
page = UiBankPage(driver)

# Seleciona o primeiro registro da planilha
request = loan_requests[0]

# Preenche o formulário
page.fill_form(request)

# Envia o formulário
page.submit()

# Mantém o navegador aberto para testes
input("Pressione ENTER para fechar: ")

