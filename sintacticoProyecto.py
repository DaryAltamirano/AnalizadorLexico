# Yacc example

import ply.yacc as yacc
# import lexicoProyecto

# Get the token map from the lexer.  This is required.
from lexicoProyecto import tokens
from lexicoProyecto import reserverd




##################################################
# EMPIEZA AQUÍ DARIEN ALTAMIRANO

def p_todo(p):
     '''todo : lista 
               | variable 
               | conjunto 
               | pair'''

##Listas listo
def p_Todaslaslistas(p):
     '''lista :  ListaConTipo 
               | ListaSinTipo '''
##Variable listo.
def p_Todaslasvariables(p):
     '''variable : variableConTipo 
                | variableSinTipo '''
##Conjunto listo.
def p_TodaslosConjunto(p):
     '''conjunto : ConjuntoConTipo 
                | ConjuntoSinTipo '''  

#################################################VARIABLE####################################################
# Variable con tipo
def p_variableConTipoString(p):
    'variableConTipo :  valovar VARIABLE DOSPUNTOS STRING IGUAL STRINGPALABRA'
def p_variableConTipoInt(p):
    'variableConTipo :  valovar VARIABLE DOSPUNTOS INT IGUAL NUMBER'
    #FALTA AÑADIR BOOL
def p_variableConTipoBool(p):
    'variableConTipo :  valovar VARIABLE DOSPUNTOS BOOLEAN IGUAL '
# Variable sin tipo 
def p_variableSinTipo(p):
     'variableSinTipo : valovar VARIABLE IGUAL datosprimitivos ' 
#################################################LISTAS#######################################################

# val primos: List<Int> = listOf (2)
# val nombres: List<String> = listOf("Juan")
# val listaMezclada = listOf() 

# Corregir que ingrese mas de un elemento 
def p_ListadeTipoInt(p):
     'ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE INT MAYORQUE IGUAL LISTOF LPAREN repeInt RPAREN'
def p_ListadeTipoString(p):
     'ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE STRING MAYORQUE IGUAL LISTOF LPAREN repeString RPAREN'
     #FALTA BOOL
def p_ListadeTipoBool(p):
     'ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE BOOLEAN MAYORQUE IGUAL LISTOF LPAREN  RPAREN'
#Lista sin tipo
def p_ListaSinTipo(p):
     'ListaSinTipo : valovar VARIABLE IGUAL LISTOF LPAREN repeCualquier RPAREN'
#################################################CONJUNTOS####################################################
# val conjunto: Set<Int> = setOf(1, 3, 4)
# val conjuntoMezclado = setOf(2, 4.454, "casa", 'c')  
def p_ConjuntodeTipoInt(p):
     'ConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE INT MAYORQUE IGUAL SETOF LPAREN repeInt RPAREN'
def p_ConjuntoTipoString(p):
     'ConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE STRING MAYORQUE IGUAL SETOF LPAREN repeString RPAREN'
     #FALTA BOOL
def p_ConjuntodeTipoBool(p):
     'ConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE BOOLEAN MAYORQUE IGUAL SETOF LPAREN  RPAREN'
#Lista sin tipo
def p_ConjuntoSinTipo(p):
     'ConjuntoSinTipo : valovar VARIABLE IGUAL SETOF LPAREN repeCualquier RPAREN'
#################################################PAIR####################################################

# var pair = Pair("Kotlin Pair",2)
def p_Pair(p):
     'pair : valovar VARIABLE IGUAL PAIR  LPAREN  datosprimitivos COMA  datosprimitivos RPAREN'
## TERMINA AQUI DARIEN ALTAMIRANO





# REGLAS QUE TE PUEDEN SERVIR 


# A ESTA REGLA LE FALTA EL BOOL
def p_algunTipo(p):
     '''datosprimitivos : NUMBER 
               | STRINGPALABRA
               | VARIABLE '''
               
def p_valovar(p):
     '''valovar :  VAR 
               | VAL'''

# PARA QUE SE REPITA INT 
# (2,4,5,6)
def p_repetirInt(p):
     'repeInt : valor'
def p_repetirInt_i(p):
     'repeInt : valor COMA repeInt'
def p_valor(p):
     '''valor : NUMBER
        | VARIABLE'''

# PARA QUE SE REPITA STRING
# ("hola","oli", "olas")
def p_repetirString(p):
     'repeString : String'
def p_repetirString_s(p):
     'repeString : String COMA repeString'
def p_String(p):
     '''String : STRINGPALABRA
        | VARIABLE'''


# PARA QUE SE REPITA CUALQUIERDATOPRIMITIVO
# (2,true,"asda",variab)
def p_repetirCualquiera(p):
     'repeCualquier : datosprimitivos'
def p_repetirCualquiera_i(p):
     'repeCualquier : datosprimitivos COMA repeCualquier'





def p_error(p):
    print("Syntax error in input!")

 # Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
