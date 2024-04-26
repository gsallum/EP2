from module import *
import random
from copy import deepcopy
from art import *
from constants import *

def GameTitle():
    system('cls')
    sleep(0.7)
    output = '\n'
    string = '''==================================================================================================================================='''
    for ch in string:
        output += colored_text(ch, random.choice(COLORS))
    output += '\n'
    print(output)
    print(text2art('BATALHA   NAVAL', space=2))
    print(output)
    sleep(0.35)
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
        # output += '\n'
        i += 1
        print(output)
        sleep(0.2)
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
    sleep(1)
    

def cria_mapa(n):
    output: list = []

    for _ in range(n):
        output.append([' '] * n)
    
    return output

def posicao_suporta(mapa: list, blocos: int, linha: int, coluna: int, orientação: str) -> bool:

    if orientação == 'v':
        col_list = [R[coluna] for R in mapa]

        col_list = col_list[linha:]
        if blocos > len(col_list):
            return False
        
        elif blocos < len(col_list):
            col_list = col_list[:blocos]

        if 'N' in col_list:
            return False
        else:
            return True
    
    elif orientação == 'h':
        row_list = mapa[linha]
        row_list = row_list[coluna:]
        if blocos > len(row_list):
            return False
        elif blocos < len(row_list):
            row_list = row_list[:blocos]

        if 'N' in row_list:
            return False
        else:
            return True

def foi_derrotado(matriz: list) -> bool:
    for row in matriz:
        for num in row:
            if num == 'N':
                return False
    return True

def _Comp_aloca_navios(comp_board: list, blocos: list) -> list[str]:
    
    n = len(comp_board[0])

    for navio in blocos:
        while True:
            clinha = random.randint(0, n-1)
            ccoluna = random.randint(0, n-1)
            corientacao = random.choice(['h', 'v'])
            
            if posicao_suporta(mapa=comp_board, blocos=navio, linha=clinha, 
                            coluna=ccoluna, orientação=corientacao):
                i = clinha
                i2 = ccoluna
                for _ in range(navio):
                    if corientacao == 'v':
                        comp_board[i][ccoluna] = 'N'
                        i += 1
                    elif corientacao == 'h':
                        comp_board[clinha][i2] = 'N'
                        i2 += 1
                break
    return comp_board

if __name__ == '__main__':
    GameTitle()
    progress_bar()
    InicializeGame()