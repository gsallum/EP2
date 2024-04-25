from rich.progress import track
from time import sleep
from os import system


def progress_bar():
    print('\n')
    for i in track(range(35), description='Loading...'):
        sleep(0.09)
    print('\n')

def bold_text(text):
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end

def italic_text(text):
    italic_start = '\x1B[3m'
    italic_end = '\x1B[0m'
    return italic_start + text + italic_end

def GameTitle():
    system('cls')
    sleep(0.7)
    print('\n' + bold_text('=========================== BATANLHA NAVAL ===========================') + '\n')
    sleep(1)
    print(italic_text('> by Enzo Savino e Gabriel Sallum. Insper - Dessoft - EP2'))
    sleep(0.7)