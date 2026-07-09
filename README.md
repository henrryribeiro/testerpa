# Teste Técnico - Automação RPA com Python

## Descrição

Este projeto foi desenvolvido como parte de um teste técnico para a vaga de Programador RPA.

A automação realiza todo o processo de solicitação de empréstimos no UiBank, desde o download da planilha até a captura do resultado de cada solicitação.

## Funcionalidades

* Download automático da planilha do Google Drive.
* Leitura dos dados do arquivo Excel.
* Abertura automática do navegador.
* Preenchimento do formulário de empréstimo.
* Envio da solicitação.
* Captura do resultado da solicitação.
* Processamento de todas as linhas da planilha.
* Exibição dos resultados no console.

## Tecnologias utilizadas

* Python 3
* Selenium
* Pandas
* Requests
* WebDriver Manager
* OpenPyXL
* Git

## Estrutura do projeto

```text
teste-tecnicorpa/
│
├── files/
│   └── planilha.xlsx
│
├── src/
│   ├── browser.py
│   ├── downloader.py
│   ├── excel_reader.py
│   └── uibank.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/henrryribeiro/testerpa.git
```

### 2. Acesse a pasta do projeto

```bash
cd teste-tecnicorpa
```

### 3. Crie e ative um ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute o projeto

```bash
python main.py
```

## Fluxo da automação

1. Baixa a planilha do Google Drive.
2. Lê os dados do arquivo Excel.
3. Acessa o formulário do UiBank.
4. Preenche os dados de cada solicitação.
5. Envia o formulário.
6. Captura o resultado da solicitação.
7. Exibe os resultados no console.

## Exemplo de saída

```text
6 solicitações carregadas.

{'Status': 'Approved', 'APR': '8', 'Loan ID': '6a4fcfb10f79076a36ac35cc'}

{'Status': 'Approved', 'APR': '4', 'Loan ID': '6a4fcfb20f79076a36ac35cd'}

{'Status': 'Failed', 'Message': 'Loan was not approved'}
```

## Autor

Henrry Ribeiro
