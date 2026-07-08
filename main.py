from src.downloader import download_file
from src.excel_reader import read_excel


spreadsheet_url = (
    "https://docs.google.com/spreadsheets/d/"
    "1FJeNr6pSydj4dNNmjklWWDsdUiCo55Uw/"
    "export?format=xlsx"
)


file_path = "files/planilha.xlsx"


download_file(
    spreadsheet_url,
    file_path
)


loan_requests = read_excel(
    file_path
)


print(
    f"{len(loan_requests)} solicitações carregadas."
)