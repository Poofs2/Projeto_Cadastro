'''
- Crie Sistema Escolar Que Permita Cadastrar Alunos, Professores, Disciplinas e Turmas.
    - Alunos: Nome, Matrícula, Data de Nascimento, Sexo, Endereço, Telefone, E-mail.
    - Professores: Nome, Matrícula, Data de Nascimento, Sexo, Endereço, Telefone, E-mail, Disciplina.
    - Disciplinas: Nome, Código (A1234), Carga Hotária, Professor.
    - Turmas: Nome, Código (A1234), Disciplina, Professor, Alunos (Lista de Alunos na Turma).

- O Sistema Deve Permitir a Filtragem de Professores por Disciplina.

Faker - Biblioteca
dica: Criar dicionário dentro da função com o return:
exemplo: return {'nome': nome}

- O Sistema Deve Permitir a Matrícula de Alunos em Turmas.
- O Sistema Deve Permitir a Alocação de Professores em Disciplinas.
- O Sistema Deve Permitir a Consulta de Alunos Matriculados em Turmas.
- O Sistema Deve Permitir a Consulta de Disciplinas Alocadas em Turmas.
- O Sistema Deve Permitir a Consulta de Professores Alocados em Disciplinas.

- Código Deve ser Infinito, Criar um Menu :3

        !!Entrega: Primeira Semana de Janeiro!!
               Dia 06, 07 ou 09 de Janeiro

    Chat GPT use apenas para refatorar o codigo para que ele fique mais limpo e organizado
    Pode usar para perguntar coisas
'''
import os

# --- Cadastro de Alunos -------
def cadastro_alunos():
    os.system('cls')
    print("--- Cadastro de Aluno ---")
    nome = input("Digite o Nome do Aluno:\n")
    matricula = input("Digite a Matrícula do Aluno:\n")
    data_nasc = input("Digite a Data de Nascimento do Aluno:\n")
    genero = input("Digite o Gênero do Aluno:\n")
    endereco = input("Digite o Endereço do Aluno:\n")
    telefone = input("Digite o Telefone do Aluno:\n")
    email = input("Digite o Email do Aluno:\n")
    aluno = {
        'nome': nome,
        'matricula': matricula,
        'data_nascimento': data_nasc,
        'genero': genero,
        'endereco': endereco,
        'telefone': telefone,
        'email': email,
    }
    system_data["alu_cad"].append(aluno)
    print(f"Aluno {nome} Cadastrado com Sucesso! :3")
    input("Pressione Enter Para Continuar...")

# --- Cadastro de Professores ---
def cadastro_prof():
    os.system('cls')
    print("--- Cadastro de Professor ---")
    nome = input("Digite o Nome do Professor:\n")
    matricula = input("Digite a Matrícula do Professor:\n")
    data_nasc = input("Digite a Data de Nascimento do Professor:\n")
    genero = input("Digite o Gênero do Professor:\n")
    endereco = input("Digite o Endereço do Professor:\n")
    telefone = input("Digite o Telefone do Professor:\n")
    email = input("Digite o Email do Professor:\n")
    disciplina = input("Digite a Disciplina do Professor:\n")
    professor = {
        'nome': nome,
        'matricula': matricula,
        'data_nascimento': data_nasc,
        'genero': genero,
        'endereco': endereco,
        'telefone': telefone,
        'email': email,
        'disciplina': disciplina,
    }
    system_data["prof_cad"].append(professor)
    print(f"Professor {nome} cadastrado com sucesso!")
    input("Pressione Enter para continuar...")

# --- Cadastro de Disciplinas ---
def cadastro_disciplina():
    os.system('cls')
    print("--- Cadastro de Disciplina ---")
    nome = input("Digite o Nome da Disciplina:\n")
    codigo = input("Digite o Código da Disciplina (ex: A1234):\n")
    carga_horaria = input("Digite a Carga Horária da Disciplina:\n")
    professor = input("Digite o Nome do Professor da Disciplina:\n")
    disciplina = {
        'nome': nome,
        'codigo': codigo,
        'carga_horaria': carga_horaria,
        'professor': professor,
    }
    system_data["disc_cad"].append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso!")
    input("Pressione Enter para continuar...")

# --- Cadastro de Turmas ---
def cadastro_turma():
    os.system('cls')
    print("--- Cadastro de Turma ---")
    nome = input("Digite o Nome da Turma:\n")
    codigo = input("Digite o Código da Turma (ex: A1234):\n")
    disciplina = input("Digite a Disciplina da Turma:\n")
    professor = input("Digite o Nome do Professor da Turma:\n")
    alunos = []
    while True:
        aluno = input("Digite o Nome do Aluno (Ou 'fim' Para Encerrar):\n")
        if aluno.lower() == "fim":
            break
        alunos.append(aluno)
    turma = {
        'nome': nome,
        'codigo': codigo,
        'disciplina': disciplina,
        'professor': professor,
        'alunos': alunos,
    }
    system_data["tur_cad"].append(turma)
    print(f"Turma {nome} Cadastrada com Sucesso!")
    input("Pressione Enter para Continuar...")

# --- Filtrar Professores por Disciplina ---
def filtrar_professores_por_disciplina():
    os.system('cls')
    print("--- Filtrar Professores por Disciplina ---")
    disciplina = input("Digite o Nome da Disciplina:\n")
    professores = [prof for prof in system_data["prof_cad"] if prof["disciplina"].lower() == disciplina.lower()]
    if professores:
        for prof in professores:
            print(f"- {prof['nome']} (Matrícula: {prof['matricula']})")
    else:
        print("Nenhum Professor Nessa Disciplina...")
    input("Pressione Enter Para Continuar...")

# --- Consultar Alunos em Turma ---
def consultar_alunos_turma():
    os.system('cls')
    print("--- Consultar Alunos em Turma ---")
    turma = input("Digite o Nome ou Código da Turma:\n")
    turma_encontrada = next((t for t in system_data["tur_cad"] if t["nome"] == turma or t["codigo"] == turma), None)
    if turma_encontrada:
        print(f"Alunos na Turma {turma_encontrada['nome']}:")
        for aluno in turma_encontrada["alunos"]:
            print(f"- {aluno}")
    else:
        print("Turma Nao Encontrada")
    input("Pressione Enter Para Continuar...")

# --- Main Code ---
os.system('cls')

system_data = {
    "alu_cad": [],
    "prof_cad": [],
    "disc_cad": [],
    "tur_cad": []
}

while True:
    os.system('cls')
    print("------ Bem Vindo -------")
    print("Selecione uma Opçao Abaixo:")
    print("1- Cadastrar um Aluno")
    print("2- Cadastrar um Professor")
    print("3- Cadastrar uma Disciplina")
    print("4- Cadastrar uma Turma")
    print("5- Filtrar Professores por Disciplina")
    print("6- Consultar Alunos em Turma")
    print("0- Sair")
    
    opcao = input("Qual a Opção Desejada?\n")
    if opcao == "0":
        print("--- Até logo! :3 ---")
        break
    elif opcao == "1":
        cadastro_alunos()
    elif opcao == "2":
        cadastro_prof()
    elif opcao == "3":
        cadastro_disciplina()
    elif opcao == "4":
        cadastro_turma()
    elif opcao == "5":
        filtrar_professores_por_disciplina()
    elif opcao == "6":
        consultar_alunos_turma()
    else:
        print("Opção Inválida. Tente Novamente!")
        input("Pressione Enter para continuar...")
# --- Main Code ---