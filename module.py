from rich.progress import track
from time import sleep
from os import system

# BARRA DE PROGRESSO
def progress_bar():
    print('\n')
    for i in track(range(35), description='Loading...'):
        sleep(0.09)
    print('\n')

# TEXTO NEGRITO
def bold_text(text):
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end

# TEXTO ITALICO
def italic_text(text):
    italic_start = '\x1B[3m'
    italic_end = '\x1B[0m'
    return italic_start + text + italic_end

# TEXTO SUBLINHADO
def underline_text(text):
    start = '\u001b[4m'
    end = '\u001b[0m'
    return start + text + end

# COLORE TEXTO OU BACKGROUND
def colored_text(text, color):
    colors = {
        'Reset': 0,
        'Black': 30,
        'Red': 31,
        'Green': 32,
        'Yellow': 33,
        'Blue': 34,
        'Magenta': 35,
        'Cyan': 36,
        'White': 37,
        'Background Black': 40,
        'Background Red': 41,
        'Background Green': 42,
        'Background Yellow': 43,
        'Background Blue': 44,
        'Background Magenta': 45,
        'Background Cyan': 46,
        'Background White': 47}
    body = "\u001b["
    start = body + str(colors[color]) + 'm'
    end = body + str(colors['Reset']) + 'm'
    return start + text + end
