import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PARAOPEN',
    'PARACLOSE',
    'CHAVOPEN',
    'CHAVCLOSE',
    'ANOTATIONS',
    'ANOTATIONSBIG',
    'FOR',
    'WHILE',
    'VAR',
    'PROGRAM',
    'FUNCTION',
    'IF',
    'PRINT',
    'ARR',
)

t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_PARAOPEN = r'\('
t_PARACLOSE = r'\)'
t_CHAVOPEN = r'\{'
t_CHAVCLOSE = r'\}'
t_ANOTATIONS = r'\#\.*\n'
t_ANOTATIONSBIG = r'\{\-\.*\-\}'
t_FOR = r'for \D+ in\[\d+\.\.\d+\]\{.*\}'
t_WHILE = r'while \D+\{\.*\}'
t_VAR = r'int \D+'
t_PROGRAM = r'program \D+\{.+\}'
t_FUNCTION = r'function \D+\{.+\}'
t_IF = r'if \D+\{\.*\}'
t_PRINT = r'print\(.+)'
t_ARR = r'\D+\[\d+\]'




def t_MINUS(t):
    r'\-'
    return t


def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


t_ignore = ' \t\n'


def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

data = '''
3 + 4 * 10
  + -20 *2
'''

lexer.input(data)

while tok := lexer.token():
    print(tok)
