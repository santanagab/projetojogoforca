from encodings import utf_8
from random import random, choice

# desenvolver o delete de cada palavra já jogada
with open('frutas.txt', encoding='utf_8') as arquivo:
    linhas = arquivo.read()
    frutas = linhas.split()
with open('africa.txt', encoding='utf_8') as arquivo:
    linhas = arquivo.read()
    africa = linhas.split()
with open('praias.txt', encoding='utf_8') as arquivo:
    linhas = arquivo.read()
    praias = linhas.split()   
with open('banco.txt', encoding='utf_8') as arquivo:
    linhas = arquivo.read()
    banco = linhas.split()   

# listas de palavras separadas por categorias 
# frutas = ['pitomba', 'jambo', 'seriguela', 'caja', 'mangaba', 'umbu', 'pitanga', 'caju', 'acerola']
# africa = ['angola', 'senegal', 'nigeria', 'moçambique', 'congo', 'quenia', 'gana', 'marrocos', 'camaroes']
# praias = ['seixas', 'arapuca', 'tambaba', 'tabatinga', 'camboinha', 'fagundes']


nome = str(input('INFORME SEU NOME: ')).upper().strip()

def forca_erro1():
    print("  _______     ")
    print(" |/      |    ")
    print(" |      (_)   ")
    print(" |            ")
    print(" |            ")
    print(" |            ")
    print(" |            ")
    print("_|___         ")

def forca_erro2():
    print("  _______     ")
    print(" |/      |    ")
    print(" |      (_)   ")
    print(" |       |    ")
    print(" |       |    ")
    print(" |            ")
    print(" |            ")
    print("_|___         ")

def forca_erro3():
    print("  _______     ")
    print(" |/      |    ")
    print(" |      (_)   ")
    print(" |      \|    ")
    print(" |       |    ")
    print(" |            ")
    print(" |            ")
    print("_|___         ")

def forca_erro4():
    print("  _______     ")
    print(" |/      |    ")
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |            ")
    print(" |            ")
    print("_|___         ")

def forca_erro5():
    print("  _______     ")
    print(" |/      |    ")
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |      /     ")
    print(" |            ")
    print("_|___         ")

def forca_erro6():
    print("  _______     ")
    print(" |/      |    ")
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |      / \   ")
    print(" |            ")
    print("_|___         ")

def forca_erro7():
    print("  _______     ")
    print(" |/      |    ")
    print(" |      (_)   ")
    print(" |     \ | /  ")
    print(" |       |    ")
    print(" |      / \   ")
    print(" |            ")
    print("_|___         ")


def menu():
    print('>' * 20, 'UNIESP'.center(20), '<' * 20)
    print('#'.ljust(15), 'INTRODUÇÃO À PROGRAMAÇÃO'.center(30), '#'.rjust(15))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#'.ljust(15), 'BEM-VINDO(A) AO JOGO DA FORCA,'.center(30), '#'.rjust(15))
    print('#'.ljust(15), '{}'.format(nome).center(30), '#'.rjust(15))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#'.ljust(15), 'MENU DE CATEGORIAS'.center(30), '#'.rjust(15))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#'.ljust(15), '[1] Frutas Nordestinas'.center(15), '#'.rjust(23))
    print('#'.ljust(15), '[2] Países Africanos'.center(15), '#'.rjust(25))
    print('#'.ljust(15), '[3] Praias da Paraíba'.center(15), '#'.rjust(24))
    print('#'.ljust(15), '[0] SAIR DO JOGO'.center(5), '#'.rjust(29))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#'.ljust(3), 'Grupo:', '#'.rjust(51))
    print('#'.ljust(3), 'Brunno Medeiros - 2022111510029@iesp.edu.br', '#'.rjust(14))
    print('#'.ljust(3), 'Camylla Neves - 2022111510089@iesp.edu.br', '#'.rjust(16))
    print('#'.ljust(3), 'Eduardo Urbieta - 2022111510044@iesp.edu.br', '#'.rjust(14))
    print('#'.ljust(3), 'Gabriel Santana - 2022111510010@iesp.edu.br', '#'.rjust(14))
    print('#'.ljust(3), 'Ianny Mamedes - 2022111510025@iesp.edu.br', '#'.rjust(16))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#' * 62)
menu()
print()

corretas = []
erradas = []
digitadas = []
palavra = []
palpite = []
erros = 0
tema = ''
while tema != '0':
    tema = input('{}, escolha o TEMA para iniciar o jogo: '.format(nome)).upper().strip()
    if tema == '1':
        tema = 'Frutas Nordestinas'
    elif tema == '2':
        tema = 'Países Africanos'
    elif tema == '3':
        tema = 'Praias Paraibanas'
    elif tema == '0':
        print('Opção Escolhida: SAIR DO JOGO')
        print('Jogo encerrando...')
        print('Jogo encerrado!')    # colocar temporizador
        break
    else:
        print('Opção Inválida. Tente outra vez!')
        print('''
        [1] Frutas Nordestinas
        [2] Países Africanos
        [3] Praias da Paraíba
        [0] SAIR DO JOGO''')
        continue
    print('TEMA ESCOLHIDO: {} \nVamos lá! Bom jogo!'.format(tema))
    print()
    if tema == 'Frutas Nordestinas':
        palavra = choice(frutas).upper()
    elif tema == 'Países Africanos':
        palavra = choice(africa).upper()
    elif tema == 'Praias Paraibanas':
        palavra = choice(praias).upper()
    while palavra != '0':
        print(palavra)
        oculta = ''
        print('PALAVRA: ', end='')
        for letra in palavra:
            oculta += letra if letra in corretas else '_'
        print(oculta)
        if oculta == palavra:
            print('AÊ, PORRA! VOCÊ VENCEU!')
            continuar = str(input('Nova Rodada? [S/N] ')).strip().upper()
            if continuar == 'S':
                tipo = str(input('Deseja nova palavra [P] ou mudar de tema [T]? [P/T]: ')).strip().upper()  # terminar as próximas linhas com nova palavra e novo tema.
                if tipo == 'P':  # falta desenvolver. só está aparecendo a partir do input de palpite
                    break
                elif tipo == 'T':     # novo tema
                    menu()
                    corretas = []
                    digitadas = []
                    erros = 0
                    break 
            else: 
                continuar == 'N' # corrigido 
                print('Jogo encerrado') 
                tema = '0'
                break  
        palpite = str(input("\n\n{}, qual é o seu palpite? Digite uma letra: ".format(nome))).upper()
        if palpite in digitadas:
            print('Essa LETRA já foi digitada. Tente uma diferente!')
            print('Letras digitadas: {}'.format(digitadas))
            continue
        elif palpite not in banco:
            print('Isso não é uma letra. Tente desta vez uma letra')
            continue
        else:
            digitadas.append(palpite)
        if palpite in palavra:
            corretas.append(palpite)
            print('Acertou uma letra!')
            print('Letras Informadas:')
            print('Letras Corretas: {}'.format(corretas))
            print('Letras Erradas: {}'.format(erradas))
        else:
            print('Errou!')
            erradas.append(palpite)
            print('Letras Informadas:')
            print('Letras Corretas: {}'.format(corretas))
            print('Letras Erradas: {}'.format(erradas))
            erros += 1
        if erros == 1:
            forca_erro1()
        elif erros == 2:
            forca_erro2()
        elif erros == 3:
            forca_erro3()
        elif erros == 4:
            forca_erro4()
        elif erros == 5:
            forca_erro5()
        elif erros == 6:
            forca_erro6()                     
        if erros == 7:
            forca_erro7()
            print('ENFORCADO! Você Perdeu!')
            print('PALAVRA era: {}'.format(palavra))
            continuar = str(input('Nova rodada? [S/N]: ')).upper().strip()
            if continuar == 'S': 
                menu()
                corretas = []
                digitadas = []
                erros = 0
                break
            else: # corrigido
                print('Jogo encerrado')
                tema = '0'
                break
            