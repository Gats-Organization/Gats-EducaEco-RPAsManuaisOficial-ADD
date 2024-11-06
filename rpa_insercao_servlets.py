# RPA para inserção de dados no servlets

# Pandas para analisar o excel
import pandas as pd

# Selenium para automação
from selenium import webdriver
from selenium.webdriver.common.by import By

# Sleep para tempo entre as atividades
from time import sleep

# Pyautogui para realizar o Login
import pyautogui

# Dotenv para puxar informações do login
from dotenv import load_dotenv

# Puxar a dotenv
import os

# Carregando as variáveis do .env
load_dotenv()

# E-mail e senha de administradores para o login no servlets
email_admin = os.getenv("EMAIL_ADMIN")
senha_admin = os.getenv("SENHA_ADMIN")

# Entrando no site do EducaEco
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get("https://gats-educaeco-servlets.onrender.com/educaeco/index.html")

sleep(2)

# Fazendo login - e-mail
x_email = 1245
y_email = 706

pyautogui.click(x_email, y_email)
pyautogui.write(email_admin)

# Fazendo login - senha
x_senha = 1245
y_senha = 850

pyautogui.click(x_senha, y_senha)
pyautogui.write(senha_admin)

# Clicando em Login
botao_login = driver.find_element('xpath', '//*[@id="botão-login"]')
botao_login.click()

sleep(5)

# FIM LOGIN

# Lendo o excel
df = pd.read_excel(r"C:\Users\murilomoreira-ieg\OneDrive - Instituto Germinare\Área de trabalho\Trabalho Interdisciplinar 2°ano\Análise de Dados\RPAs Manuais\rpa_insercao_firebase.py")

# For para Inserir informações no Servlets

for index, row in df.iterrows():
    # <-- COMEÇO INSERÇÃO ESCOLA-->
# --------------------------------------------------------------------------------------------
    # Entrando na Tabela Escola
    botao_escola = driver.find_element('xpath', '//*[@id="botaoEscola"]')
    botao_escola.click()
    sleep(5)

    # Adicionando a Escola
    botao_adicionar_escola = driver.find_element('xpath', '//*[@id="addEscola"]')
    botao_adicionar_escola.click()
    sleep(3)

    # Preenchendo informações da escola
    nome_escola = driver.find_element('xpath', '//*[@id="inputNome"]')
    nome_escola.click()
    nome_escola.send_keys(row['Nome Escola'])

    email_escola = driver.find_element('xpath', '//*[@id="inputEmail"]')
    email_escola.click()
    email_escola.send_keys(row['E-mail Escola'])

    telefone_escola = driver.find_element('xpath', '//*[@id="inputTelefone"]')
    telefone_escola.click()
    telefone_escola.send_keys(row['Telefone Escola'])

    endereco_escola = driver.find_element('xpath', '//*[@id="inputEndereco"]')
    endereco_escola.click()
    endereco_escola.send_keys(row['Endereço Escola'])

    # Clicando em Salvar
    salvar_insercao = driver.find_element('xpath', '//*[@id="salvar"]')
    salvar_insercao.click()

    sleep(10)

    # Voltando a Home
    voltar_home = driver.find_element('xpath', '/html/body/div[1]/a[1]')
    voltar_home.click()

    # <-- FIM INSERÇÃO ESCOLA-->
# --------------------------------------------------------------------------------------------

    # <-- COMEÇO INSERÇÃO PROFESSOR -->

# --------------------------------------------------------------------------------------------
    # Entrando na Tabela Professor
    botao_professor = driver.find_element('xpath', '//*[@id="botaoProfessor"]')
    botao_professor.click()

    sleep(5)

    # Clicando no botão para adicionar professor
    botao_adicionar_professor = driver.find_element('xpath', '//*[@id="addProfessor"]')
    botao_adicionar_professor.click()
    sleep(3)

    # Preenchendo informações do professor
    nome_professor = driver.find_element('xpath', '//*[@id="inputNome"]')
    nome_professor.click()
    nome_professor.send_keys(row['Nome Professor'])

    sobrenome_professor = driver.find_element('xpath', '//*[@id="inputSobrenome"]')
    sobrenome_professor.click()
    sobrenome_professor.send_keys(row['Sobrenome Professor'])

    email_professor = driver.find_element('xpath', '//*[@id="inputEmail"]')
    email_professor.click()
    email_professor.send_keys(row['E-mail Professor'])

    senha_professor = driver.find_element('xpath', '//*[@id="inputSenha"]')
    senha_professor.click()
    senha_professor.send_keys(row['Senha Professor'])

    # Clicando em Salvar
    salvar_insercao.click()
    
    sleep(10)

    # Voltando a Home
    voltar_home.click()

    # <-- FIM INSERÇÃO PROFESSOR-->
# --------------------------------------------------------------------------------------------

    # <-- COMEÇO INSERÇÃO TURMA-->
# --------------------------------------------------------------------------------------------
    # Entrando na Tabela Turma
    botao_turma = driver.find_element('xpath', '//*[@id="botaoTurma"]')
    botao_turma.click()

    sleep(5)

    # Clicando no botão para adicionar turma
    botao_adicionar_turma = driver.find_element('xpath', '//*[@id="addTurma"]')
    botao_adicionar_turma.click()
    sleep(3)

    # Preenchendo informações do professor
    serie_turma = driver.find_element('xpath', '//*[@id="inputSerie"]')
    serie_turma.click()
    serie_turma.send_keys(row['Serie Turma'])

    nomenclatura_turma = driver.find_element('xpath', '//*[@id="inputNomeclatura"]')
    nomenclatura_turma.click()
    nomenclatura_turma.send_keys(row['Nomenclatura'])

    ano_turma = driver.find_element('xpath', '//*[@id="inputAno"]')
    ano_turma.click()
    ano_turma.send_keys(row['Ano'])

    escola_turma = driver.find_element('xpath', '//*[@id="inputEscola"]')
    escola_turma.click()
    escola_turma.send_keys(row['Nome Escola'])

    professor_turma = driver.find_element('xpath', '//*[@id="inputProfessor"]')
    professor_turma.click()
    professor_turma.send_keys(f'{row['Nome Professor']} - {row['Nomenclatura']}')

    # Clicando em Salvar
    salvar_insercao.click()
    
    sleep(10)

    # Voltando a Home
    voltar_home.click()

    # <-- FIM INSERÇÃO TURMA-->
# --------------------------------------------------------------------------------------------

    # <-- COMEÇO INSERÇÃO ALUNO-->
# --------------------------------------------------------------------------------------------
    # Entrando na Tabela Aluno
    botao_aluno = driver.find_element('xpath', '//*[@id="botaoAluno"]')
    botao_aluno.click()

    sleep(5)

    # Clicando no botão para adicionar aluno
    botao_adicionar_aluno = driver.find_element('xpath', '//*[@id="addAluno"]')
    botao_adicionar_aluno.click()
    sleep(3)

    # Preenchendo informações do aluno
    nome_aluno = driver.find_element('xpath', '//*[@id="inputNome"]')
    nome_aluno.click()
    nome_aluno.send_keys(row['Nome Aluno'])

    sobrenome_aluno = driver.find_element('xpath', '//*[@id="inputSobrenome"]')
    sobrenome_aluno.click()
    sobrenome_aluno.send_keys(row['Sobrenome Aluno'])

    xp_aluno = driver.find_element('xpath', '//*[@id="inputXp"]')
    xp_aluno.click()
    xp_aluno.send_keys(row['XP'])

    email_aluno = driver.find_element('xpath', '//*[@id="inputEmail"]')
    email_aluno.click()
    email_aluno.send_keys(row['E-mail Aluno'])

    senha_aluno = driver.find_element('xpath', '//*[@id="inputSenha"]')
    senha_aluno.click()
    senha_aluno.send_keys(row['Senha Aluno'])

    turma_aluno = driver.find_element('xpath', '//*[@id="inputTurma"]')
    turma_aluno.click()
    turma_aluno.send_keys(f"{row['Serie Turma']} - {row['Nomenclatura']}")

    # Clicando em Salvar
    salvar_insercao.click()
    
    sleep(10)

    # Voltando a Home
    voltar_home.click()

    # <-- FIM INSERÇÃO ALUNO-->
# --------------------------------------------------------------------------------------------

    # <-- COMEÇO INSERÇÃO RESPONSÁVEL-->
# --------------------------------------------------------------------------------------------
    # Entrando na Tabela Responsável
    botao_responsavel = driver.find_element('xpath', '//*[@id="botaoResponsavel"]')
    botao_aluno.click()

    sleep(5)

    # Clicando no botão para adicionar aluno
    botao_adicionar_responsavel = driver.find_element('xpath', '//*[@id="addAluno"]')
    botao_adicionar_responsavel.click()
    sleep(3)

    # Preenchendo informações do aluno
    nome_responsavel = driver.find_element('xpath', '//*[@id="inputNome"]')
    nome_responsavel.click()
    nome_responsavel.send_keys(row['Nome Responsavel'])

    sobrenome_responsavel = driver.find_element('xpath', '//*[@id="inputSobrenome"]')
    sobrenome_responsavel.click()
    sobrenome_responsavel.send_keys(row['Sobrenome Responsavel'])

    email_responsavel = driver.find_element('xpath', '//*[@id="inputEmail"]')
    email_responsavel.click()
    email_responsavel.send_keys(row['Sobrenome Responsavel'])

    aluno_responsavel = driver.find_element('xpath', '//*[@id="inputIdAluno"]')
    aluno_responsavel.click()
    aluno_responsavel.send_keys(f"{row['Nome Aluno']} {row['Sobrenome Aluno']}")

    # Clicando em Salvar
    salvar_insercao.click()
    
    sleep(10)

    # Voltar a home
    voltar_home.click()

    # <-- FIM INSERÇÃO ALUNO-->

# --------------------------------------------------------------------------------------------

    # Saindo da conta
    botao_sair = driver.find_element('xpath', '/html/body/a')
    botao_sair.click()


# Saindo do navegador
driver.close()