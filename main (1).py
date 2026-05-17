import os
import time
import openpyxl

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Caminho e aba da planilha Excel
pasta_excel = 'gestao_de_vendas.xlsx'
aba_excel = 'Gestão de vendas'

def colunas_excel(texto):

    linhas_excel = []

    for linha in texto.strip().splitlines():

        partes = linha.split()


        linhas_excel.append(partes[:7])

   
    return linhas_excel

#Nome do contato ou grupo que será pesquisado no whatsapp
contato_procurado = input("Digite o nome do contato ou grupo: ")#"Gestão imobiliaria"

#Caminho do google
caminho_google = os.path.abspath("chrome_profile")

#Aguarda o elemento do whatsapp web ficar visível
painel_whatsapp = "//div[@id='pane-side']"

#Tempo para aguardar o carregamento do whatsapp web
tempo_espera = 120 # 2 minutos

#Caixa de pesquisa de contatos
pesquisar_contatos = "//input[@aria-label='Pesquisar ou começar uma nova conversa']"

def main():
    try:
        #Abre o google e entra no whatsapp web
        manager = ChromeDriverManager().install()
        options = Options()
        options.add_argument(f"--user-data-dir={caminho_google}")
        service = webdriver.chrome.service.Service(manager)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://web.whatsapp.com")

        #Aguarda o elemento da caixa de pesquisa
        print("Aguardando elemento do Whatsapp Web ficar visível...")
        wait = WebDriverWait(driver, tempo_espera)
        wait.until(EC.presence_of_element_located((
            webdriver.common.by.By.XPATH, 
            painel_whatsapp
            )))
        print("Elemento do Whatsapp Web visível!")

        #Abre a caixa de pesquisa e digita o nome do contato
        search_box = driver.find_element(webdriver.common.by.By.XPATH, pesquisar_contatos)
        search_box.click()
        time.sleep(0.5)

        #Digita o nome do contato
        for c in contato_procurado:
            search_box.send_keys(c)
            time.sleep(0.1)
        time.sleep(1)

        #Clica no contato do contato_procurado
        search_box.send_keys(webdriver.common.keys.Keys.ENTER)
        time.sleep(1)

        #Econtrar mensagens
        mensagens = driver.find_elements(By.XPATH, '//div[@data-pre-plain-text]')

        #Printa quantas mensagens foram encontradas
        total = len(mensagens)
        print(f"{total} mensagem(s) encontrada(s):")

        #Grava no Excel
        print("\nGravando dados no Excel...")

        planilha = openpyxl.load_workbook(pasta_excel)
        aba = planilha[aba_excel]

        dados_excel = []

        for msg in mensagens:

            texto = msg.find_element(By.XPATH,'.//span[contains(@class,"copyable-text")]').text

            dados_excel.extend(colunas_excel(texto))

        for linha in dados_excel:
            aba.append(linha)

        planilha.save(pasta_excel)

        print(f"{len(dados_excel)} linhas gravadas.")

    except Exception as e:
        print(f"Erro ao raspar o Whatsapp Web: {e}")

    input("Pressione Enter para fechar o driver...")
    driver.quit()

if __name__ == "__main__":
    main()