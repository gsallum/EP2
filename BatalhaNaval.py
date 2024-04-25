from module import *

import random
from copy import deepcopy

PAISES = {
    'Brasil': {'cruzador': 1, 'torpedeiro': 2, 'destroyer': 1, 'couracado': 1, 'porta-avioes': 1}, 
    'França': {'cruzador': 3, 'porta-avioes': 1, 'destroyer': 1, 'submarino': 1, 'couracado': 1},
    'Austrália': {'couracado': 1, 'cruzador': 3, 'submarino': 1, 'porta-avioes': 1, 'torpedeiro': 1},
    'Rússia': {'cruzador': 1, 'porta-avioes': 1, 'couracado': 2, 'destroyer': 1, 'submarino': 1},
    'Japão': {'torpedeiro': 2, 'cruzador': 1, 'destroyer': 2, 'couracado': 1, 'submarino': 1}
}

# quantidade de blocos por modelo de navio
CONFIGURACAO = {'destroyer': 3, 'porta-avioes': 5, 'submarino': 2,
                'torpedeiro': 3, 'cruzador': 2, 'couracado': 4}

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
