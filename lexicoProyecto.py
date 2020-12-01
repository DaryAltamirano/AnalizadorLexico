import ply.lex as lex

# KOTLIN!!!!
# List of token names.   This is always required
textoSalida = "" #Texto en el que se escribe la salida

reserverd ={
    'if ':'IF',
    'then': 'THEN',
    'else' :'ELSE',
    'while' :'WHILE',
    'for' : 'FOR',
    'when' : 'WHEN',
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
    'set':'SET',
    'listof':'LISTOF',
    'list':'LIST',
    'pair':'PAIR',
    'or' :'OR',
    'and':'AND',
    'in' : 'IN',
    'rindex': 'RINDEX',
    'contains':'CONTAINS',
    }
tokens = (
    'NUMBER',
    'STRINGPALABRA',
    'BOOLEANPALABRA',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LLLAVE',
    'RLLAVE',
    'MAYORQUE',
    'MENORQUE',
    'VARIABLE',
    'IGUAL',
    'MOD',
    'PUNTOYCOMA',
    'DOSPUNTOS',
    'ESIGUAL',
    'COMA',
    'PUNTO',
    'DIFERENTE',
    'LCLASP',
    'RCLASP'
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
t_PUNTO=r'\.'
t_PUNTOYCOMA=r';'
t_DOSPUNTOS=r':'
t_ESIGUAL=r'=='
t_COMA=r','
t_DIFERENTE=r'!='
t_LLLAVE=r'{'
t_RLLAVE=r'}'
t_LCLASP=r'\['
t_RCLASP=r'\]'


# RESERVADOS
t_INT=r'(Int) | (int) | (INT)'
t_ELSE =r'(else)'
t_IF=r'(if)'
t_THEN=r'(then)'
t_FOR = r'(for)'
t_WHEN = r'(when)'
t_AND=r'(and)'
t_OR= r'(or)'
t_VAR=r'(var)'
t_VAL=r'(val)'
t_STRING=r'(String)'
t_BOOLEAN=r'(Boolean)'
t_FUN=r'(fun)'
t_SIZE=r'(size\(\))'
t_RINDEX=r'(rindex)'
t_CONTAINS=r'(contains)'
t_WHILE=r'(while)'
t_SETOF=r'(setOf)'
t_LISTOF=r'(listOf)'
t_PAIR=r'(Pair)'
t_LIST=r'(List)'
t_SET=r'(Set)'
t_BOOLEANPALABRA=r'(True) | (False) '
t_IN = r'(in)'


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
    global textoSalida
    textoSalida +="No es reconocido '%s'" % t.value[0]+"\n"
    t.lexer.skip(1)

def t_STRINGPALABRA(t):
    r'"[a-zA-Z0-9\s]*" |\'[a-zA-Z0-9\s]*\''
    t.value = str(t.value)
    return t
# Build the lexer
lexer = lex.lex()
# Test it out

# archivo=open("C:/Users/LAPTOP/Documents/GitHub/AnalizadorLexico/a.txt")
# data = archivo.read()

# #data ='''setOf() tuple() listOf() size()'''
# # var count: Int = 10
# # Give the lexer some input
# #lexer.input(data)
# # Tokenize


def analizarLex (data):
    lexer.input(data)
    global textoSalida
    textoSalida=""
    while True:
        tok=lexer.token()
        if not tok:
            break
        textoSalida+= str(tok)+"\n"
    return textoSalida
