from module import *
from constants import *
import random
from copy import deepcopy

def GameTitle():
    system('cls')
    sleep(0.7)
    print('\n' + bold_text('=========================== BATANLHA NAVAL ===========================') + '\n')
    sleep(1)
    print(italic_text('> by Enzo Savino e Gabriel Sallum. Insper - Dessoft - EP2'))
    sleep(0.7)

def InicializeGame(show=True):
    global pais_user, pais_comp
    output = ''
    i = 1
    for pais, frota in PAISES.items():
        output += bold_text(f'{i}: {pais}') + '\n'
        for navio, quant in frota.items():
            output += ' ' * 3
            output += f'- {quant} {navio}\n'
        output += '\n'
        i += 1
        print(output)
        sleep(0.3)
        output = ''

    while True:
        nacao = input('> Coloque o número da nação da sua frota desejada.\n> ')
        if nacao not in ['1', '2', '3', '4', '5']:
            print('Insira um númro válido...\n')
        else:
            nacao = int(nacao)
            break
    paises = list(PAISES.keys())
    for idx, pais in enumerate(paises):
        if (idx + 1) == nacao:
            pais_user = pais
    paises.remove(pais_user)
    pais_comp = random.choice(paises)

    print('\nNação escolhida por ' + italic_text('você') + ' -> ' + pais_user)
    print('Nação escolhida pelo ' + italic_text('computador') + ' -> ' + pais_comp)
    print('\nAgora aloque os navios da sua nação e prepare-se para a GUERRA!')

if __name__ == '__main__':
    GameTitle()
    progress_bar()
    InicializeGame()