
from random import choice
import pygame
from time import sleep

# comando para importação das listas de palavras
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

nome = str(input('INFORME SEU NOME: ')).upper().strip()

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")

def vencedor():
    print()
    print('     (o_')
    print("(o_  //\\")
    print('(/)_ V_/_')


def menu():
    pygame.mixer.init()
    pygame.mixer.music.load('menu.wav')
    pygame.mixer.music.play()
    print('>' * 20, 'UNIESP'.center(20), '<' * 20)
    print('#'.ljust(15), 'INTRODUÇÃO À PROGRAMAÇÃO'.center(30), '#'.rjust(15))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#'.ljust(15), 'BEM-VINDO(A) AO JOGO DA FORCA,'.center(30), '#'.rjust(15))
    print('#'.ljust(15), '\033[33m{}\033[m'.format(nome).center(38), '#'.rjust(15))
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
    sleep(0.5)
menu()
print()

corretas = []
erradas = []
digitadas = []
palavra = []
palpite = []
erros = 0
tema = ''

# laço para escolha de tema para iniciar o jogo.
while tema != '0':
    tema = input('\033[33m{}\033[m, escolha o TEMA para iniciar o jogo: '.format(nome)).upper().strip()
    if tema == '1':
        tema = 'Frutas Nordestinas'
    elif tema == '2':
        tema = 'Países Africanos'
    elif tema == '3':
        tema = 'Praias Paraibanas'
    elif tema == '0':
        print('Opção Escolhida: SAIR DO JOGO')
        print('Jogo encerrando...')
        print('\033[33mJOGO ENCERRADO\033[m')    # colocar temporizador
        break
    else:
        print('\033[31mOpção Inválida. Tente outra vez!\033[m')
        print('''
        [1] Frutas Nordestinas
        [2] Países Africanos
        [3] Praias da Paraíba
        [0] SAIR DO JOGO''')
        print()
        continue
    
    # print informando o tema escolhido
    print('TEMA ESCOLHIDO: \033[33m{}\033[m'.format(tema))
    sleep(0.3)
    print()
    print('Vamos lá! Bom jogo!')
    pygame.mixer.init()
    pygame.mixer.music.load('lets-go.mp3')
    pygame.mixer.music.play()
    sleep(0.5)

    # condição indica o tema escolhido e abre a lista correspondente, escolhendo uma palavra de forma aleatória. 
    if tema == 'Frutas Nordestinas':
        palavra = choice(frutas).upper()
    elif tema == 'Países Africanos':
        palavra = choice(africa).upper()
    elif tema == 'Praias Paraibanas':
        palavra = choice(praias).upper()
    
    while palavra != '0':
        oculta = ''
        print()
        print('\033[33mPALAVRA:\033[m ', end='')
        for letra in palavra:
            oculta += letra if letra in corretas else '_'
        print('\033[33m{}\033[m'.format(oculta))
        print('\nA Palavra tem: \033[33m{} letras\033[m'.format(len(oculta)))   # informa a quantidade de letras que contém na palavra
        
        palpite = str(input("\n\n{}, qual é o seu palpite? Digite uma letra: ".format(nome))).upper()
        
        # condição que informa que a letra já foi utilizada anteriormente
        if palpite in digitadas:
            pygame.mixer.init()
            pygame.mixer.music.load('alert.mp3')
            pygame.mixer.music.play()
            print('Tema: \033[33m{}\033[m'.format(tema))
            print('\033[1;36mLETRA JÁ DIGITADA!\033[m Tente uma diferente!')
            print('Letras digitadas: \033[36m{}\033[m'.format(digitadas))
            continue
        
        # condição que informa que o caractere digitado não é válido
        elif palpite not in banco:
            pygame.mixer.init()
            pygame.mixer.music.load('alert.mp3')
            pygame.mixer.music.play()
            print('\033[1;36mIsso não é uma letra.\033[m Tente desta vez uma letra')
            continue
        
        else:
            digitadas.append(palpite)

        # condição que informa o acerto de uma letra
        if palpite in palavra:
            corretas.append(palpite)
            pygame.mixer.init()
            pygame.mixer.music.load('coin.wav')
            pygame.mixer.music.play()
            print('\033[1;32mACERTOU UMA LETRA!\033[m')
            print('Tema: \033[33m{}\033[m'.format(tema))
            print('Letras Informadas:')
            print('Letras Corretas: \033[32m{}\033[m'.format(corretas))
            print('Letras Erradas: \033[31m{}\033[m'.format(erradas))
            venceu = True
            for letra in palavra:
                if letra not in corretas:
                    venceu = False
            if venceu:   
                pygame.mixer.init()
                pygame.mixer.music.load('winner.wav')
                pygame.mixer.music.play()       
                print('\033[1;32mVOCÊ VENCEU!\033[m')
                print('PALAVRA era: \033[32m{}\033[m'.format(palavra))
                vencedor()
                
                # condições do laço para continuar o jogo
                while True:
                    continuar = str(input('\nNova Rodada? [S/N] ')).strip().upper()               
                    if continuar == 'S':    # continua no jogo, escolhe outro tema
                        menu()
                        corretas = []
                        digitadas = []
                        erradas = []
                        erros = 0
                        palavra = '0'
                        break                   
                    elif continuar == 'N':   # sai do jogo
                        print('\033[33mJOGO ENCERRADO\033[m') 
                        tema = '0'
                        palavra = '0'
                        break                 
                    else:   # informa que a escolha é inválida
                        print('Opção Inválida. Digite "S" para CONTINUAR ou "N" para SAIR')
                        continue
        
        # condição informando que o jogador errou uma letra e contabiliza um ponto de erro na forca
        else:
            palpite not in palavra
            pygame.mixer.init()
            pygame.mixer.music.load('erro.wav')
            pygame.mixer.music.play()
            print('\033[1;31mERROU!\033[m')
            erradas.append(palpite)
            print('Tema: \033[33m{}\033[m'.format(tema))
            print('Letras Informadas:')
            print('Letras Corretas: \033[32m{}\033[m'.format(corretas))
            print('Letras Erradas: \033[31m{}\033[m'.format(erradas))
            erros += 1
            desenha_forca(erros)
            
            if erros == 6:  
                pygame.mixer.init()
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.play()
                print('\033[1;31mENFORCADO! Você Perdeu!\033[m')
                print('PALAVRA era: \033[33m{}\033[m'.format(palavra))
                while True:
                    continuar = str(input('\nNova Rodada? [S/N] ')).strip().upper()
                    if continuar == 'S':
                        menu()
                        corretas = []
                        digitadas = []
                        erradas = []
                        erros = 0
                        palavra = '0'
                        break
                   
                    elif continuar == 'N':   # sai do jogo
                        print('\033[33mJOGO ENCERRADO\033[m') 
                        tema = '0'
                        palavra = '0'
                        break
                    
                    else:   # informa que a opção é inválida
                        print('Opção Inválida. Digite "S" para CONTINUAR ou "N" para SAIR')
                        continue                   
                
print('FIM')         