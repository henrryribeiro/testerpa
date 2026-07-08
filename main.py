from urllib3.util import url

from src.downloader import download

url = "https://docs.google.com/spreadsheets/d/1FJeNr6pSydj4dNNmjklWWDsdUiCo55Uw/export?format=xlsx"

download(
    url,
    "files/planilha.xlsx"
)