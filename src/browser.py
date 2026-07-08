from selenium import webdriver
# Controla o navegador

from selenium.webdriver.chrome.service import Service
# Configura o serviço do ChromeDriver

from webdriver_manager.chrome import ChromeDriverManager
# Baixa e configura o ChromeDriver automaticamente


def create_driver():
    # Cria o serviço do ChromeDriver
    service = Service(
        ChromeDriverManager().install()
    )

    # Inicializa o navegador
    driver = webdriver.Chrome(
        service=service
    )

    # Maximiza a janela
    driver.maximize_window()

    # Retorna o navegador
    return driver