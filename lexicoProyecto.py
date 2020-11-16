import ply.lex as lex
# KOTLIN!!!!
# List of token names.   This is always required

reserverd ={
    'if ':'IF',
    'then': 'THEN',
    'else' :'ELSE',
    'while' :'WHILE',
    'var':'VAR',
    'val':'VAL',
    'int':'INT',
    'String':'STRING',
    'boolean':'BOOLEAN',
    'var':'VAR',
    'val':'VAL',
    'fun':'FUN',
    'size': 'SIZE',
    'setof':'SETOF',
    'listof':'LISTOF',
    'tuple':'TUPLE',
    'or' :'OR',
    'and':'AND',
    }
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MAYORQUE',
    'MENORQUE',
    'VARIABLE',
    'IGUAL',
    'MOD',
    'PUNTOYCOMA',
    'DOSPUNTOS',
    'ESIGUAL'
 ) + tuple(reserverd.values())
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MAYORQUE =  r'>'
t_MENORQUE =  r'<'
t_MOD = r'%'
t_IGUAL= r'='
t_PUNTOYCOMA=r';'
t_DOSPUNTOS=r':'
t_ESIGUAL=r'=='

# RESERVADOS
t_INT=r'(int)'
t_ELSE =r'(else)'
t_IF=r'(if)'
t_THEN=r'(then)'
t_AND=r'(and)'
t_OR= r'(or)'
t_VAR=r'(var)'
t_VAL=r'(val)'
t_STRING=r'(string)'
t_BOOLEAN=r'(boolean)'
t_FUN=r'(fun)'
t_SIZE=r'(size\(\))'
t_WHILE=r'(while)'
t_SETOF=r'(setof\(\))'
t_LISTOF=r'(listof\(\))'
t_TUPLE=r'(tuple\(\))'


# VARIABLE
t_VARIABLE= r'\w+'
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
# Test it out

archivo=open("TextoAnalizadorLexicoGrupal.txt")
data = archivo.read()

#data ='''setof() tuple() listof() size()'''
# var count: Int = 10
# Give the lexer some input
#lexer.input(data)
# Tokenize

def analizar (data):
    lexer.input(data)
    while True:
        tok=lexer.token()
        if not tok:
            break
        print (tok)

analizar(data)