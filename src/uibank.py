from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
# Localiza elementos da página

from selenium.webdriver.support.ui import Select
# Manipula campos do tipo <select>


class UiBankPage:
    # Representa a página de empréstimos do UiBank

    def __init__(self, driver):
        # Recebe o navegador criado pelo Selenium
        self.driver = driver

    def fill_email(self, email):
        # Localiza e preenche o campo de e-mail
        field = self.driver.find_element(
            By.ID,
            "email"
        )

        field.send_keys(email)

    def fill_amount(self, amount):
        # Localiza e preenche o valor do empréstimo
        field = self.driver.find_element(
            By.ID,
            "amount"
        )

        field.send_keys(str(amount))

    def select_term(self, term):
        # Seleciona o prazo do empréstimo
        field = self.driver.find_element(
            By.ID,
            "term"
        )

        select = Select(field)

        select.select_by_value(str(term))

    def fill_income(self, income):
        # Localiza e preenche a renda anual
        field = self.driver.find_element(
            By.ID,
            "income"
        )

        field.send_keys(str(income))

    def fill_age(self, age):
        # Localiza e preenche a idade
        field = self.driver.find_element(
            By.ID,
            "age"
        )

        field.send_keys(str(age))

    def fill_form(self, request):
    #preenche todo formulario com os dados da planilha
        self.fill_email(
            request["Email do Solicitante"]
        )

        self.fill_amount(
            request["Montante do Empréstimo"]
        )

        self.select_term(
            request["Termo do Empréstimo"]
        )

        self.fill_income(
            request["Renda Anual Atual( Antes dos Impostos)"]
        )

        self.fill_age(
            request["Idade"]
        )

    def submit(self):
        # Envia o formulário
        button = self.driver.find_element(
            By.ID,
            "submitButton"
        )
        button.click()

    def get_result(self):
        # Aguarda o resultado aparecer
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "rateValue")
            )
            )

        # Captura a taxa APR
        rate = self.driver.find_element(
            By.ID,
            "rateValue"
            ).text

        # Captura o ID do empréstimo
        loan_id = self.driver.find_element(
            By.ID,
            "loanID"
        ).text

        # Retorna os dados da solicitação
        return {
            "APR": rate,
            "Loan ID": loan_id
        }
