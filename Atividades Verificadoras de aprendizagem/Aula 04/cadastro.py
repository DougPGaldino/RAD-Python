def entradaUsuario():
    global acao  # Correção do nome da variável global
    print('''1: Cadastrar novo aluno.
2: Listar alunos cadastrados.
3: Procurar aluno pelo nome.
4: SAIR.''')
    acao = int(input('O que deseja fazer? '))

def cadastraAluno():
    print('Cadastro de aluno. Preencha as informações:')
    ok = 0  # Variável de controle para o loop
    while ok == 0:
        matricula = input('Matrícula: ')
        nome = input('Nome: ')
        email = input('E-mail: ')
        curso = input('Curso: ')
        
        # Tratar entradas vazias
        if not matricula or not nome or not email or not curso:
            print("Entrada vazia! Redigite.\n")
        elif any(char.isdigit() for char in nome):  # Verificar se há dígitos no nome
            print("Somente caracteres no nome! Redigite.\n")
        elif not matricula.isdigit():  # Verificar se a matrícula contém apenas números
            print("Somente números na matrícula! Redigite.\n")
        else:
            ok = 1  # Se tudo estiver correto, sair do loop
        
        if ok:
            aluno = f'{matricula}, {nome}, {email}, {curso}\n'
            with open('alunos.txt', 'a', encoding='UTF-8') as arquivo:
                arquivo.write(aluno)
                print('Cadastrado!\n')

def listaAluno():
    try:
        with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
            listaAlunos = arquivo.read().strip().split('\n')
            print('\nLista de alunos cadastrados:')
            print('Matrícula, Nome, Email, Curso')
            for aluno in listaAlunos:
                if aluno:  # Verifica se a linha não está vazia
                    print(aluno)
    except FileNotFoundError:
        print('Arquivo não existe. Cadastre primeiro!\n')

def procuraAluno():
    try:
        print('Buscar aluno por nome:')
        busca = input('Nome: ')
        if not busca:
            print('Entrada vazia!')
        else:
            with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
                listaAlunos = arquivo.read().strip().split('\n')
                resultado = None
                for aluno in listaAlunos:
                    if aluno:
                        nomeAluno = aluno.split(',')[1].strip()  # Ajuste para retirar espaços desnecessários
                        if busca.lower() == nomeAluno.lower():  # Comparação case-insensitive
                            resultado = aluno
                            break
                if resultado is None:
                    print('\nNão foi encontrado nenhum aluno com esse nome.\n')
                else:
                    print(resultado + '\n')
    except FileNotFoundError:
        print('Arquivo não existe. Cadastre primeiro!\n')

while True:
    entradaUsuario()
    if acao == 1:
        cadastraAluno()
    elif acao == 2:
        listaAluno()
    elif acao == 3:
        procuraAluno()
    elif acao == 4:
        break
    else:
        print('\n::::: Escolha uma das quatro opções! :::::\n')
