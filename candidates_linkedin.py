from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def login(driver, email, senha):
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    
    campo_email = driver.find_element(By.ID, "username")
    campo_email.send_keys(email)
    
    campo_senha = driver.find_element(By.ID, "password")
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)
    
    time.sleep(3)

def buscar_candidatos(driver, palavra_chave, localizacao):
    url = f"https://www.linkedin.com/search/results/people/?keywords={palavra_chave}"
    if localizacao:
        url += f"&origin=GLOBAL_SEARCH_HEADER&location={localizacao}"
    
    driver.get(url)
    time.sleep(5)  # Espera para carregar a página
    
    candidatos = driver.find_elements(By.CLASS_NAME, "entity-result")
    dados = []
    
    for candidato in candidatos[:10]:  #só os 10 primeiros perfis
        try:
            nome = candidato.find_element(By.CLASS_NAME, "entity-result__title-text").text
            cargo = candidato.find_element(By.CLASS_NAME, "entity-result__primary-subtitle").text
            localizacao = candidato.find_element(By.CLASS_NAME, "entity-result__secondary-subtitle").text
            link = candidato.find_element(By.TAG_NAME, "a").get_attribute("href")
            
            dados.append([nome, cargo, localizacao, link])
        except Exception as e:
            print(f"Erro ao buscar candidato: {e}")
            continue
    
    return dados

def buscar_por_multiplas_palavras_chave(driver, palavras_chave, localizacao):
    all_candidatos = []
    for palavra in palavras_chave:
        print(f"Buscando candidatos para: {palavra}")
        candidatos = buscar_candidatos(driver, palavra, localizacao)
        all_candidatos.extend(candidatos)
        
        # Espera de 5 minutos entre as buscas para dar tempo de visualizar os resultados
        print(f"Aguardando 5 minutos antes de próxima busca...")
        time.sleep(300)  #Espera maior entre as buscas para dar tempo de olhar os resultados
    
    return all_candidatos

if __name__ == "__main__":
    email = input("Digite seu e-mail do LinkedIn: ")
    senha = getpass.getpass("Digite sua senha do LinkedIn: ")
    
    palavras_chave = input("Digite as palavras-chave para buscar candidatos (separadas por vírgula): ").split(",")
    palavras_chave = [palavra.strip() for palavra in palavras_chave]
    
    #localização/cidadania para filtrar
    localizacao = input("Digite a localização/cidadania (ou pressione Enter para não usar filtro): ").strip()
    
    driver = iniciar_driver()
    try:
        login(driver, email, senha)
        candidatos = buscar_por_multiplas_palavras_chave(driver, palavras_chave, localizacao)
        
        # Exibir os resultados
        for candidato in candidatos:
            nome, cargo, localizacao, link = candidato
            print(f"Nome: {nome}")
            print(f"Cargo: {cargo}")
            print(f"Localização: {localizacao}")
            print(f"Link: {link}")
            print("-" * 50)
    finally:
        driver.quit()
