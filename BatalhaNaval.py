'''   IMPORTE A BIBLIOTECA 'art'
'pip install art'
'''

from module import *
import random
from copy import deepcopy
from art import text2art
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

def AlocarNavios(mapa=cria_mapa(10)):

    user_frota = [navio for navio, quant in PAISES[pais_user].items() 
             for _ in range(quant)]
    
    user_board = deepcopy(mapa)
    comp_board = deepcopy(mapa)
    
    comp_frota = [navio for navio, quant in PAISES[pais_comp].items() 
             for _ in range(quant)]
    blocos = [CONFIGURACAO[navio] for navio in comp_frota]

    comp_board = _Comp_aloca_navios(comp_board=comp_board, blocos=blocos)
    
    vazio_comp_board = cria_mapa(10)

    print_board(user_board, vazio_comp_board)

    while user_frota:
        navio_alocado = user_frota.pop(0)
        num_bloco = CONFIGURACAO[navio_alocado]
        string = str(num_bloco) + ' blocos'
        colored_str = colored_text(string, 'Yellow')
        print(f'> alocar: {bold_text(navio_alocado)}   > {colored_str} <')
        print('> próximos:', ', '.join(user_frota))

        while True:
            letra = input('\nInforme a letra: ').upper()
            if letra in LETRAS:
                coluna = LETRAS.index(letra)
                linha = input('Informe a linha: ')
                if linha in [str(i) for i in range(1, 11)]:
                    linha = int(linha)
                    linha = linha - 1
                    orientação = input('Informe a orientação  [v|h]: ').lower()
                    if orientação in 'hv':
                        if posicao_suporta(mapa=user_board, blocos=num_bloco, linha=linha, 
                                        coluna=coluna, orientação=orientação):
                            i = linha
                            i2 = coluna
                            for _ in range(num_bloco):
                                if orientação == 'v':
                                    user_board[i][coluna] = 'N'
                                    i += 1
                                elif orientação == 'h':
                                    user_board[linha][i2] = 'N'
                                    i2 += 1
                            break
                        else:
                            print('\n' + italic_text(' = posição inválida! = '))
                            print('Tente novamente...')
                    else:
                        print(italic_text('> Insira uma posição válida!'))
                else:
                    print(italic_text('> Insira uma linha válida!'))
            else:
                print(italic_text('> Insira uma letra válida!'))

        print_board(user_board, vazio_comp_board)
    return user_board, comp_board, vazio_comp_board

def print_board(user_board, vazio_comp_board):
    legenda1 = '\n        ' + u'\u2022' + bold_text(' PAÍS JOGADOR - ') + bold_text(pais_user)
    legenda2 = ' ' * 22 + u'\u2022' + bold_text(' PAÍS COMPUTADOR - ') + bold_text(pais_comp)
    print(legenda1 + legenda2)
    print('\n       ' + '  '.join(LETRAS) + '                 ' + '  '.join(LETRAS))

    for i, (user_row, comp_row) in enumerate(zip(user_board, vazio_comp_board), start=1):
        user_row_str = ''
        comp_row_str = ''

        for ch in user_row:
            if ch == 'N':
                user_row_str += colored_text('   ', 'Background Green')
            elif ch == 'A':
                user_row_str += colored_text('   ', 'Background Blue')
            elif ch == 'X':
                user_row_str += colored_text('   ', 'Background Red')
            else:
                user_row_str += '   '

        for ch in comp_row:
            if ch == 'N':
                comp_row_str += colored_text('   ', 'Background Green')
            elif ch == 'A':
                comp_row_str += colored_text('   ', 'Background Blue')
            elif ch == 'X':
                comp_row_str += colored_text('   ', 'Background Red')
            else:
                comp_row_str += '   '

        if i < 10:
            print(f'  {i}   {user_row_str}  {i}        {i}   {comp_row_str}  {i}')
        else:
            print(f' {i}   {user_row_str}  {i}      {i}   {comp_row_str}  {i}')
    print('       ' + '  '.join(LETRAS) + '                 ' + '  '.join(LETRAS) + '\n')


def PlayGame(user_board, comp_board, vazio_comp_board):
    print('\nCOMEÇANDO O JOGO EM:')
    for num in reversed(range(1, 6)):
        sleep(0.36)
        print(num)
    sleep(0.4)
    system('cls')
    sleep(0.05)
    print_board(user_board, vazio_comp_board)

    n = len(user_board[0])
    user_turns = []
    comp_turns = []
    while True:
        while True:
            print('Insira as coordenadas do seu disparo.')
            letra = input('Informe a letra: ').upper()
            if letra in LETRAS:
                coluna = LETRAS.index(letra)
                linha = input('Informe a linha: ')
                if linha in [str(i) for i in range(1, 11)]:
                    linha = int(linha)
                    linha = linha - 1

                    if (linha, coluna) not in user_turns:
                        user_turns.append((linha, coluna))
                        if comp_board[linha][coluna] == 'N':
                            vazio_comp_board[linha][coluna] = 'X' # acertou navio
                            comp_board[linha][coluna] = 'X'
                        elif comp_board[linha][coluna] == ' ':
                            vazio_comp_board[linha][coluna] = 'A' # agua
                        break
                    else:
                        print(italic_text('> Você já inseriu essa coordenada anteriormente!') + '\n')

                else:
                    print(italic_text('> Insira uma linha válida!') + '\n')
            else:
                print(italic_text('> Insira uma letra válida!') + '\n')

        if foi_derrotado(comp_board):
            print_board(user_board, vazio_comp_board)
            output = ''
            string = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
            for ch in string:
                if ch == '-':
                    output += colored_text(ch, random.choice(COLORS))
            print(output)
            print(bold_text('--> Acabou o jogo! Parabéns Jogador, você VENCEU!\n'))
            print(text2art('VITORIA !'))
            print(output)
            break

        # ! vez do computador
        while True:
            clinha = random.randint(0, n-1)
            ccoluna = random.randint(0, n-1)

            if (clinha, ccoluna) not in comp_turns:
                comp_turns.append((clinha, ccoluna))
                if user_board[clinha][ccoluna] == 'N':
                    user_board[clinha][ccoluna] = 'X'
                elif user_board[clinha][ccoluna] == ' ':
                    user_board[clinha][ccoluna] = 'A'
                break

        if foi_derrotado(user_board):
            print_board(user_board, vazio_comp_board)
            print('\n')
            print(bold_text(colored_text('Acabou o jogo! O computador venceu! Não foi dessa vez... =(', 'Red')))
            break
        
        print_board(user_board, vazio_comp_board)

        
if __name__ == '__main__':

    while True:
        GameTitle()
        progress_bar()
        InicializeGame()
        user, comp, vazio = AlocarNavios()
        # print_board(user, comp)
        sleep(0.5)
        PlayGame(user, comp, vazio)

        play_again = input('\n> Deseja jogar novamente? (sim/nao)\n> ')
        if play_again != 'sim':
            print(colored_text(bold_text('OBRIGADO POR JOGAR'), 'Yellow'))
            break
        else:
            print('Reiniciando em:')
            for num in reversed(range(1, 6)):
                sleep(0.36)
                print(num)
            sleep(0.4)