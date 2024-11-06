# Projeto RPA: Cadastro de Usuários e Dados Acadêmicos

Este projeto consiste em duas automações RPA (Robotic Process Automation) desenvolvidas para facilitar o cadastro de usuários e informações acadêmicas. A primeira automação cadastra usuários no Firebase Authentication com base na planilha `usuarios.xlsx`. A segunda automação insere dados de Alunos, Professores, Responsáveis, Escolas e Turmas em um banco de dados SQL usando a planilha `informacoesteste.xlsx` como base de dados.

## Visão Geral do Projeto

### RPA 1 - Cadastro de Usuários no Firebase
Este RPA é responsável por ler dados da planilha `usuarios.xlsx` e realizar o cadastro de usuários no Firebase Authentication. Cada entrada na planilha contém informações de e-mail e senha do usuário a ser registrado.

### RPA 2 - Cadastro de Dados Acadêmicos no Banco de Dados SQL
A segunda automação é focada no cadastro de informações de Alunos, Professores, Responsáveis, Escolas e Turmas em um banco de dados SQL. Ela utiliza a planilha `informacoesteste.xlsx` como fonte de dados e executa as operações de inserção diretamente no banco de dados.

## Estrutura do Projeto

- **usuarios.xlsx**: Planilha de teste para o cadastro de usuários no Firebase.
- **informacoesteste.xlsx**: Planilha de teste para o cadastro de informações acadêmicas no banco de dados SQL.
- **rpa_insercao_firebase**: RPA para cadastrar usuários no firebase.
- **rpa_insercao_servkets**: RPA para inserir Alunos, Professores, Responsáveis, Escola e Turmas no Banco de Dados Relacional SQL

## Pré-requisitos

1. **Python** (versão 3.7 ou superior) com as bibliotecas necessárias instaladas.
2. **Firebase Authentication** configurado para autenticação de usuários.
3. **Banco de Dados SQL** PostgreSQL
4. Credenciais de acesso ao banco de dados SQL e ao Firebase.

## Configuração

### Clonando o Repositório

Para iniciar, clone o repositório para sua máquina local:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

## Execução das Automações

### RPA - Cadastro no Firebase
```base
python rpa_insercao_firebase.py
```

### RPA - Cadastro no Banco de Dados SQL
```base
python rpa_insercao_servlets.py
```

## Criadores
- Murilo de Oliveira Moreira
- Carlos Henrique de Godoy Santos
