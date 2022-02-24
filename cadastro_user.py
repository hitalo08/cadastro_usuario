pessoas_dicionarios = {}
conta_numeros = 0
cod_user = 1
qtd_cadastro = input('Quantas pessoas deseja cadastrar? ')

while not qtd_cadastro.isnumeric():
    print('Por favor, digite algo válido.\n')
    qtd_cadastro = input('Digite QUANTIDADE de pessoas:')
else:
    pass

qtd_cadastro = int(qtd_cadastro)

while conta_numeros < qtd_cadastro:
    pessoa = {'User_Name': input('Digite seu nome: '),
              'User_Idade': input('Digite seu idade: '),
              'User_Sexo': input('Digite sua sexualidade: '),
              'User_Cidade': input('Digite sua cidade: '),
              }

    pessoas_dicionarios[cod_user] = pessoa
    print('------------')
    cod_user += 1
    conta_numeros += 1

pergunta = input('Deseja visualizar o que foi adicionado? Digite sim: ')
tipos_verificacao = ['sim', 's', 'sin', 'yes', 'si', 'SiM', 'SIM', 'sIM', 'SI']

if pergunta in tipos_verificacao:
    for chave, valor in pessoas_dicionarios.items():
        print(f'Código usuário: \033[0;32m{chave}\033[0m\nValor: \033[0;36m{valor.values()})\033[0m')
        print('--------------')
else:
    print('Obrigado por essa utilização')
    exit()
