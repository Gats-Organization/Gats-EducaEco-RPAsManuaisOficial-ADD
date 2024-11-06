# Esse RPA tem como objetivo receber um excel com o nomes dos alunos, a partir disso, ele vai criar um e-mail e senha para esse aluno e cadastrar no firebase, para ele poder ter acesso ao APP.

# Importações

import firebase_admin
from firebase_admin import auth, credentials
import pandas as pd

# Conectando ao firebase
cred = credentials.Certificate("C:/Users/murilomoreira-ieg/Downloads/educaeco-f6078-firebase-adminsdk-ynozd-97a4db936e.json")

firebase_admin.initialize_app(cred)

# Função para cadastrar os clientes
def cadastrar_clientes(email, password):
    # Verificando se a quantidade de caracteres da senha for menor que 6, tem que ser pelo menos 6
    if len(password) < 6:
        print("ERRO: A senha deve ter pelo menos 6 caracteres.")
        return
    
    # Try except para tratamento
    try:
        # Criando usuário a partir das informações
        usuario = auth.create_user(
            email = email,
            password = password
        )
        print(f"Cliente cadastrado com sucesso! UID: {usuario.uid}")

    except Exception as e:
        # ERRO
        print(f"Erro ao cadastrar cliente: {e}")


# Função para cadastrar os usuários a partir do usuários pegos do excel
def cadastrar_usuarios_excel(arquivo_excel):
    # Lendo o excel
    df = pd.read_excel(arquivo_excel)

    # for para percorrer o df, pegar o nome, tratar o nome e transformar em e-mail e senha padrão
    for index, row in df.iterrows():
        nome = row[0] # Nome do aluno
        nome = nome.split()
        email = nome[0] + "." + nome[-1] + "@gats.com"
        password = "Gats2024@"

        # Chamando a função cadastrar clientes
        cadastrar_clientes(email, password)


arquivo_excel = r"C:\Users\murilomoreira-ieg\OneDrive - Instituto Germinare\Área de trabalho\Trabalho Interdisciplinar 2°ano\Análise de Dados\usuarios.xlsx"
cadastrar_usuarios_excel(arquivo_excel)