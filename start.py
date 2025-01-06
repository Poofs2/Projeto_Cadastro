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
    # Alunos: Nome, Matrícula, Data de Nascimento, Sexo, Endereço, Telefone, E-mail.
    os.system('cls')
    nome = input("Digite o Nome do Aluno:\n")
    matricula = int(input("Digite a Matricula do Aluno:\n"))
    dataNasc = input("Digite a Data de Nascimento do Aluno:\n")
    genero = input("Digite o Genero do Aluno:\n")
    endereco= input("Digite o Genero do Aluno:\n")
    telefone = int(input("Digite o Genero do Aluno:\n"))
    email = input("Digite o Genero do Aluno:\n")
    return {
        'nome': nome,
        'matricula': matricula,
        'data_nascimento': dataNasc,
        'genero': genero,
        'endereco': endereco,
        'telefone': telefone,
        'email': email,
        }
# --- Cadastro de Alunos ---------

# --- Cadastro de Professores ----
def cadastro_prof():
    #- Professores: Nome, Matrícula, Data de Nascimento, Sexo, Endereço, Telefone, E-mail, Disciplina.
    os.system('cls')
    print("--- Cadastro do Professor ---") #Colocar Lá Embaixo Quando Puxar a Função
    nome = input("Digite o Nome do Professor:\n")
    matricula = int(input("Digite a Matricula do Professor:\n"))
    dataNasc = input("Digite a Data de Nascimento do Professor:\n")
    genero = input("Digite o Genero do Professor:\n")
    endereco= input("Digite o Genero do Professor:\n")
    telefone = int(input("Digite o Genero do Professor:\n"))
    email = input("Digite o Genero do Professor:\n")
    disciplina = input("Digite a Disciplina do Professor:\n")
    return {
        'nome': nome,
        'matricula': matricula,
        'data_nascimento': dataNasc,
        'genero': genero,
        'endereco': endereco,
        'telefone': telefone,
        'email': email,
        'disciplina': disciplina,
        }
# --- Cadastro de Professores ----

# --- Cadastro da Disciplina -----
def cadastro_disciplina():
    #- Disciplinas: Nome, Código (A1234), Carga Hotária, Professor.
    nome = input("Digite o Nome da Disciplina:\n")
    codigo = 'Funcao de Criar Codigo Aqui!'
    carga_horaria = int(input("Digite qual a Carga Horaria da Disciplina:\n"))
    professor = input("Digite o Nome do Professor da Disciplina:")
    return {
        'nome': nome,
        'codigo': codigo,
        'carga_horaria': carga_horaria,
        'professor': professor,
    }
# --- Cadastro da Disciplina -----

# --- Cadastro de Turmas ---------
    #- Turmas: Nome, Código (A1234), Disciplina, Professor, Alunos (Lista de Alunos na Turma).
def cadastro_turma():
    nome = input("Digite o Nome da Turma:\n")
    codigo = 'Funcao de Criar Codigo Aqui!'
    professor = input("Digite o Nome do Professor da Disciplina:")
    qnt_alunos = int(input("Quantos Alunos Tem na Turma?\n"))
    lista_alunos = lista_alunos(qnt_alunos)
    
    return {
        'nome': nome,
        'codigo': codigo,
        'professor': professor,
        'alunos': lista_alunos,
    }
# --- Cadastro de Turmas ---------

# --- Lista de Alunos na Turma ---
def lista_alunos(qnt):    
    return [input("Qual o Nome do Aluno?\n") for num in range(qnt)]
# --- Lista de Alunos na Turma ---

# --- Main Code -------------------------
os.system('cls')
while True:
    print("------ Bem Vindo -------")
    print("Selecione uma opcao abaixo:")
    print("1- Cadastrar um Aluno")
    print("2- Cadastrar um Professor")
    print("3- Cadastrar uma Disciplina")
    print("4- Cadastrar uma Turma")
    print("5- Alocar um Professor a Uma Disciplina")
    print("6- Alocar Disciplina em Turma") 
    print("7- Matricular um Aluno a Uma Turma")
    print("8- Filtrar Professores por Disciplinas")
    print("9- Consultar Alunos")
    print("0- Sair")
    
    opcao = int(input("Qual a Opcao Desejada?\n"))
    if opcao == 0:
        print("--- Até logo! :3 ---\n")
        break
    elif opcao == 1:
        os.system('cls')
        print("--- Opcao Selecionada: 1- Cadastrar um Aluno ---")
        
    elif opcao == 2:
        os.system('cls')
        print("--- Opcao Selecionada: 2- Cadastrar um Professor ---")
        
    elif opcao == 3:
        os.system('cls')
        print("--- Opcao Selecionada: 3- Cadastrar uma Disciplina ---")
        
    elif opcao == 4:
        os.system('cls')
        print("--- Opcao Selecionada: 4- Cadastrar uma Turma ---")
        
    elif opcao == 5:
        os.system('cls')
        print("--- Opcao Selecionada: 5- Alocar um Professor a Uma Disciplina ---")
        
    elif opcao == 6:
        os.system('cls')
        print("--- Opcao Selecionada: 6- Alocar Disciplina em Turma ---")
        
    elif opcao == 7:
        os.system('cls')
        print("--- Opcao Selecionada: 7- Matricular um Aluno a Uma Turma ---")
        
    elif opcao == 8:
        os.system('cls')
        print("--- Opcao Selecionada: 8- Filtrar Professores por Disciplinas ---")
        
    elif opcao == 9:
        os.system('cls')
        print("--- Opcao Selecionada: 9- Consultar Alunos ---")
        os.system('cls')
    else:
        print("Opcao Invalida, Tente Novamente")
        
# --- Main Code -------------------------