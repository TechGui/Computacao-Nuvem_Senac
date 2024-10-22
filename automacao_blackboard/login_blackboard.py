from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# ⬇ Insira aqui seu CPF e senha do Blackboard ⬇
cpf = os.getenv('BLACKBOARD_CPF')
senha = os.getenv('BLACKBOARD_SENHA')
# ⬆ Insira aqui seu CPF e senha do Blackboard ⬆

# Verifica se as variáveis foram carregadas corretamente
if not cpf or not senha:
    raise ValueError("As variáveis BLACKBOARD_CPF e BLACKBOARD_SENHA não foram carregadas corretamente do arquivo .env")

print()
print("Seja bem vindo ao Blackboard via terminal! Aqui você pode acessar suas aulas de forma rápida.")
print()

cadeira = int(input("1. Segunda-feira\n2. Terça-feira\n3. Quarta-feira\n4. Quinta-feira\n5. Sexta-feira\nOpção: "))

if cadeira < 1 or cadeira > 5:
    while cadeira < 1 or cadeira > 5:
        print("Valor inválido!")
        cadeira = int(input("1. Segunda-feira\n2. Terça-feira\n3. Quarta-feira\n4. Quinta-feira\n5. Sexta-feira\nOpção: "))

navegador = webdriver.Firefox()
navegador.maximize_window()
navegador.get('https://senac.blackboard.com')

campoCPF = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.NAME, 'user_id_tmp'))
)

campoSenha = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)

campoCPF.send_keys(cpf)
campoSenha.send_keys(senha)

navegador.find_element(By.ID, 'entry-login').click()

# Espera até que a página principal carregue completamente após o login
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.ID, 'global-nav-link'))
)

btnSalas = WebDriverWait(navegador, 120).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Salas de Aula'))
)
btnSalas.click()

# Espera 10 segundos para garantir que a página carregue completamente
navegador.implicitly_wait(10)

# Localiza a barra de pesquisa input courses-overview-filter-search
campoPesquisa = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.ID, 'courses-overview-filter-search'))
)

cadeiras = {
    1: 'Projeto Integrador',
    2: 'Gestão Ágil de Projetos',
    3: 'Computação em Nuvem',
    4: 'Linguagens de Programação Emergentes',
    5: 'Automação e Programabilidade em Redes'
}

# Recebe o primeiro nome da cadeira para pesquisar
primeiro_nome_cadeira = cadeiras[cadeira].split()[0]

# Clica enter para pesquisar a cadeira pelo primeiro nome
campoPesquisa.send_keys(primeiro_nome_cadeira)

try:
    # Verifica se o link da matéria está disponível
    link_cadeira = WebDriverWait(navegador, 60).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, cadeiras[cadeira]))
    )
    link_cadeira.click()
except Exception as e:
    print(f"Erro: {e}")
    
    # Verifica se os links presentes na página estão corretos
    links_presentes = navegador.find_elements(By.TAG_NAME, "a")
    for link in links_presentes:
        print(link.text)

input("Pressione Enter para fechar o navegador...")
navegador.quit()
