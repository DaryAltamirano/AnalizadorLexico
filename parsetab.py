
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOLEAN BOOLEANPALABRA COMA DIFERENTE DIVIDE DOSPUNTOS ELSE ESIGUAL FOR FUN IF IGUAL IN INT LIST LISTOF LLLAVE LPAREN MAYORQUE MENORQUE MINUS MOD NUMBER OR PAIR PLUS PUNTO PUNTOYCOMA RLLAVE RPAREN SET SETOF SIZE STRING STRINGPALABRA THEN TIMES VAL VAR VARIABLE WHEN WHILEtodo : lista \n               | variable \n               | conjunto \n               | pair\n               | control\n               | funcion lista :  ListaConTipo \n               | ListaSinTipo variable : variableConTipo \n                | variableSinTipo conjunto : ConjuntoConTipo \n                | ConjuntoSinTipo variableConTipo :  valovar VARIABLE DOSPUNTOS STRING IGUAL STRINGPALABRAvariableConTipo :  valovar VARIABLE DOSPUNTOS INT IGUAL NUMBERvariableConTipo :  valovar VARIABLE DOSPUNTOS BOOLEAN IGUAL variableSinTipo : valovar VARIABLE IGUAL datosprimitivos ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE INT MAYORQUE IGUAL LISTOF LPAREN repeInt RPARENListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE STRING MAYORQUE IGUAL LISTOF LPAREN repeString RPARENListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE BOOLEAN MAYORQUE IGUAL LISTOF repeBool LPAREN  RPARENListaSinTipo : valovar VARIABLE IGUAL LISTOF LPAREN repeCualquier RPARENConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE INT MAYORQUE IGUAL SETOF LPAREN repeInt RPARENConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE STRING MAYORQUE IGUAL SETOF LPAREN repeString RPARENConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE BOOLEAN MAYORQUE IGUAL SETOF LPAREN  repeBool RPARENConjuntoSinTipo : valovar VARIABLE IGUAL SETOF LPAREN repeCualquier RPARENpair : valovar VARIABLE IGUAL PAIR  LPAREN  datosprimitivos COMA  datosprimitivos RPARENdatosprimitivos : NUMBER \n               | STRINGPALABRA\n               | BOOLEANPALABRA\n               | VARIABLE valovar :  VAR \n               | VALrepeInt : valorrepeInt : valor COMA repeIntvalor : NUMBER\n        | VARIABLErepeString : StringrepeString : String COMA repeStringString : STRINGPALABRA\n        | VARIABLErepeBool : boolrepeBool : bool COMA repeBoolbool : BOOLEANPALABRA\n        | VARIABLErepeCualquier : datosprimitivosrepeCualquier : datosprimitivos COMA repeCualquiercomparacion : valor operadoresComp valoroperadoresComp : MAYORQUE\n                        | DIFERENTE\n                        | MENORQUE\n                        | ESIGUALtipoDato : INT\n                | STRING\n                | BOOLEANargumento : tipoDato VARIABLErepeArg : argumentorepeArg : argumento COMA repeArgcontrol : if\n              | when\n              | forif : ifBoolean\n            | ifComparacion\n            | ifVariablewhen : whenVacio\n           | whenVariablefor : forRango\n           | forVariableifBoolean : IF LPAREN BOOLEANPALABRA RPAREN LLLAVE RLLAVEifComparacion : IF LPAREN comparacion RPAREN LLLAVE RLLAVEifVariable : IF LPAREN VARIABLE RPAREN LLLAVE RLLAVEwhenVariable : WHEN LPAREN VARIABLE RPAREN LLLAVE RLLAVEwhenVacio : WHEN LLLAVE RLLAVEforVariable : FOR LPAREN VARIABLE IN VARIABLE RPAREN LLLAVE RLLAVEforRango : FOR LPAREN VARIABLE IN NUMBER PUNTO PUNTO NUMBER RPAREN LLLAVE RLLAVE funcion : funConSalidaArg\n                | funConSalida\n                | funSinSalidaArg\n                | funSinSalidafunConSalida : FUN VARIABLE LPAREN repeArg RPAREN DOSPUNTOS tipoDato LLLAVE RLLAVEfunSinSalida : FUN VARIABLE LPAREN repeArg RPAREN LLLAVE RLLAVEfunConSalidaArg : FUN VARIABLE LPAREN RPAREN DOSPUNTOS tipoDato LLLAVE RLLAVEfunSinSalidaArg : FUN VARIABLE LPAREN RPAREN LLLAVE RLLAVE'
    
_lr_action_items = {'VAR':([0,],[22,]),'VAL':([0,],[23,]),'FUN':([0,],[31,]),'IF':([0,],[32,]),'WHEN':([0,],[33,]),'FOR':([0,],[34,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,24,25,26,27,28,29,30,49,52,54,57,58,59,88,110,111,116,120,121,122,123,127,129,138,149,151,153,160,183,184,186,188,190,191,192,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-57,-58,-59,-74,-75,-76,-77,-60,-61,-62,-63,-64,-65,-66,-71,-29,-16,-26,-27,-28,-15,-14,-13,-81,-67,-68,-69,-70,-20,-24,-79,-80,-72,-25,-78,-73,-17,-18,-19,-21,-22,-23,]),'VARIABLE':([14,22,23,31,37,39,40,41,66,69,70,71,75,76,77,78,79,81,82,83,84,126,128,156,162,163,168,169,170,179,185,187,],[35,-30,-31,36,46,50,51,52,92,-51,-52,-53,99,-47,-48,-49,-50,101,52,52,52,52,52,164,99,174,99,174,164,164,99,174,]),'LPAREN':([32,33,34,36,53,55,56,154,155,157,158,159,164,165,166,167,189,],[37,39,40,43,82,83,84,162,163,168,169,170,-43,178,-40,-42,-41,]),'LLLAVE':([33,65,69,70,71,72,73,74,80,93,115,124,137,161,],[38,91,-51,-52,-53,95,96,97,100,118,136,139,150,171,]),'IGUAL':([35,61,62,63,130,131,132,133,134,135,],[41,86,87,88,143,144,145,146,147,148,]),'DOSPUNTOS':([35,65,93,],[42,90,117,]),'BOOLEANPALABRA':([37,41,82,83,84,126,128,156,170,179,],[44,59,59,59,59,59,59,167,167,167,]),'NUMBER':([37,41,75,76,77,78,79,81,82,83,84,86,126,128,140,162,168,185,],[48,57,48,-47,-48,-49,-50,102,57,57,57,110,57,57,152,48,48,48,]),'RLLAVE':([38,91,95,96,97,100,118,136,139,150,171,],[49,116,120,121,122,123,138,149,151,160,183,]),'PAIR':([41,],[53,]),'LISTOF':([41,143,144,145,],[55,154,155,156,]),'SETOF':([41,146,147,148,],[56,157,158,159,]),'STRINGPALABRA':([41,82,83,84,87,126,128,163,169,187,],[58,58,58,58,111,58,58,177,177,177,]),'LIST':([42,],[60,]),'STRING':([42,43,85,89,90,94,117,],[62,70,108,113,70,70,70,]),'INT':([42,43,85,89,90,94,117,],[61,69,107,112,69,69,69,]),'BOOLEAN':([42,43,85,89,90,94,117,],[63,71,109,114,71,71,71,]),'SET':([42,],[64,]),'RPAREN':([43,44,45,46,48,50,52,57,58,59,67,68,92,98,99,101,104,105,106,119,141,142,152,164,166,167,172,173,174,175,176,177,178,180,181,182,189,193,194,],[65,72,73,74,-34,80,-29,-26,-27,-28,93,-55,-54,-46,-35,124,127,-44,129,-56,153,-45,161,-43,-40,-42,184,-32,-39,186,-36,-38,188,190,191,192,-41,-33,-37,]),'MAYORQUE':([46,47,48,107,108,109,112,113,114,],[-35,76,-34,130,131,132,133,134,135,]),'DIFERENTE':([46,47,48,],[-35,77,-34,]),'MENORQUE':([46,47,48,60,64,],[-35,78,-34,85,89,]),'ESIGUAL':([46,47,48,],[-35,79,-34,]),'COMA':([48,52,57,58,59,68,92,99,103,105,164,166,167,173,174,176,177,],[-34,-29,-26,-27,-28,94,-54,-35,126,128,-43,179,-42,185,-39,187,-38,]),'IN':([51,],[81,]),'PUNTO':([102,125,],[125,140,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'todo':([0,],[1,]),'lista':([0,],[2,]),'variable':([0,],[3,]),'conjunto':([0,],[4,]),'pair':([0,],[5,]),'control':([0,],[6,]),'funcion':([0,],[7,]),'ListaConTipo':([0,],[8,]),'ListaSinTipo':([0,],[9,]),'variableConTipo':([0,],[10,]),'variableSinTipo':([0,],[11,]),'ConjuntoConTipo':([0,],[12,]),'ConjuntoSinTipo':([0,],[13,]),'valovar':([0,],[14,]),'if':([0,],[15,]),'when':([0,],[16,]),'for':([0,],[17,]),'funConSalidaArg':([0,],[18,]),'funConSalida':([0,],[19,]),'funSinSalidaArg':([0,],[20,]),'funSinSalida':([0,],[21,]),'ifBoolean':([0,],[24,]),'ifComparacion':([0,],[25,]),'ifVariable':([0,],[26,]),'whenVacio':([0,],[27,]),'whenVariable':([0,],[28,]),'forRango':([0,],[29,]),'forVariable':([0,],[30,]),'comparacion':([37,],[45,]),'valor':([37,75,162,168,185,],[47,98,173,173,173,]),'datosprimitivos':([41,82,83,84,126,128,],[54,103,105,105,141,105,]),'tipoDato':([43,90,94,117,],[66,115,66,137,]),'repeArg':([43,94,],[67,119,]),'argumento':([43,94,],[68,68,]),'operadoresComp':([47,],[75,]),'repeCualquier':([83,84,128,],[104,106,142,]),'repeBool':([156,170,179,],[165,182,189,]),'bool':([156,170,179,],[166,166,166,]),'repeInt':([162,168,185,],[172,180,193,]),'repeString':([163,169,187,],[175,181,194,]),'String':([163,169,187,],[176,176,176,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> todo","S'",1,None,None,None),
  ('todo -> lista','todo',1,'p_todo','sintacticoProyecto.py',15),
  ('todo -> variable','todo',1,'p_todo','sintacticoProyecto.py',16),
  ('todo -> conjunto','todo',1,'p_todo','sintacticoProyecto.py',17),
  ('todo -> pair','todo',1,'p_todo','sintacticoProyecto.py',18),
  ('todo -> control','todo',1,'p_todo','sintacticoProyecto.py',19),
  ('todo -> funcion','todo',1,'p_todo','sintacticoProyecto.py',20),
  ('lista -> ListaConTipo','lista',1,'p_Todaslaslistas','sintacticoProyecto.py',24),
  ('lista -> ListaSinTipo','lista',1,'p_Todaslaslistas','sintacticoProyecto.py',25),
  ('variable -> variableConTipo','variable',1,'p_Todaslasvariables','sintacticoProyecto.py',28),
  ('variable -> variableSinTipo','variable',1,'p_Todaslasvariables','sintacticoProyecto.py',29),
  ('conjunto -> ConjuntoConTipo','conjunto',1,'p_TodaslosConjunto','sintacticoProyecto.py',32),
  ('conjunto -> ConjuntoSinTipo','conjunto',1,'p_TodaslosConjunto','sintacticoProyecto.py',33),
  ('variableConTipo -> valovar VARIABLE DOSPUNTOS STRING IGUAL STRINGPALABRA','variableConTipo',6,'p_variableConTipoString','sintacticoProyecto.py',38),
  ('variableConTipo -> valovar VARIABLE DOSPUNTOS INT IGUAL NUMBER','variableConTipo',6,'p_variableConTipoInt','sintacticoProyecto.py',40),
  ('variableConTipo -> valovar VARIABLE DOSPUNTOS BOOLEAN IGUAL','variableConTipo',5,'p_variableConTipoBool','sintacticoProyecto.py',43),
  ('variableSinTipo -> valovar VARIABLE IGUAL datosprimitivos','variableSinTipo',4,'p_variableSinTipo','sintacticoProyecto.py',46),
  ('ListaConTipo -> valovar VARIABLE DOSPUNTOS LIST MENORQUE INT MAYORQUE IGUAL LISTOF LPAREN repeInt RPAREN','ListaConTipo',12,'p_ListadeTipoInt','sintacticoProyecto.py',55),
  ('ListaConTipo -> valovar VARIABLE DOSPUNTOS LIST MENORQUE STRING MAYORQUE IGUAL LISTOF LPAREN repeString RPAREN','ListaConTipo',12,'p_ListadeTipoString','sintacticoProyecto.py',57),
  ('ListaConTipo -> valovar VARIABLE DOSPUNTOS LIST MENORQUE BOOLEAN MAYORQUE IGUAL LISTOF repeBool LPAREN RPAREN','ListaConTipo',12,'p_ListadeTipoBool','sintacticoProyecto.py',60),
  ('ListaSinTipo -> valovar VARIABLE IGUAL LISTOF LPAREN repeCualquier RPAREN','ListaSinTipo',7,'p_ListaSinTipo','sintacticoProyecto.py',63),
  ('ConjuntoConTipo -> valovar VARIABLE DOSPUNTOS SET MENORQUE INT MAYORQUE IGUAL SETOF LPAREN repeInt RPAREN','ConjuntoConTipo',12,'p_ConjuntodeTipoInt','sintacticoProyecto.py',68),
  ('ConjuntoConTipo -> valovar VARIABLE DOSPUNTOS SET MENORQUE STRING MAYORQUE IGUAL SETOF LPAREN repeString RPAREN','ConjuntoConTipo',12,'p_ConjuntoTipoString','sintacticoProyecto.py',70),
  ('ConjuntoConTipo -> valovar VARIABLE DOSPUNTOS SET MENORQUE BOOLEAN MAYORQUE IGUAL SETOF LPAREN repeBool RPAREN','ConjuntoConTipo',12,'p_ConjuntodeTipoBool','sintacticoProyecto.py',73),
  ('ConjuntoSinTipo -> valovar VARIABLE IGUAL SETOF LPAREN repeCualquier RPAREN','ConjuntoSinTipo',7,'p_ConjuntoSinTipo','sintacticoProyecto.py',76),
  ('pair -> valovar VARIABLE IGUAL PAIR LPAREN datosprimitivos COMA datosprimitivos RPAREN','pair',9,'p_Pair','sintacticoProyecto.py',81),
  ('datosprimitivos -> NUMBER','datosprimitivos',1,'p_algunTipo','sintacticoProyecto.py',93),
  ('datosprimitivos -> STRINGPALABRA','datosprimitivos',1,'p_algunTipo','sintacticoProyecto.py',94),
  ('datosprimitivos -> BOOLEANPALABRA','datosprimitivos',1,'p_algunTipo','sintacticoProyecto.py',95),
  ('datosprimitivos -> VARIABLE','datosprimitivos',1,'p_algunTipo','sintacticoProyecto.py',96),
  ('valovar -> VAR','valovar',1,'p_valovar','sintacticoProyecto.py',99),
  ('valovar -> VAL','valovar',1,'p_valovar','sintacticoProyecto.py',100),
  ('repeInt -> valor','repeInt',1,'p_repetirInt','sintacticoProyecto.py',105),
  ('repeInt -> valor COMA repeInt','repeInt',3,'p_repetirInt_i','sintacticoProyecto.py',107),
  ('valor -> NUMBER','valor',1,'p_valor','sintacticoProyecto.py',109),
  ('valor -> VARIABLE','valor',1,'p_valor','sintacticoProyecto.py',110),
  ('repeString -> String','repeString',1,'p_repetirString','sintacticoProyecto.py',115),
  ('repeString -> String COMA repeString','repeString',3,'p_repetirString_s','sintacticoProyecto.py',117),
  ('String -> STRINGPALABRA','String',1,'p_String','sintacticoProyecto.py',119),
  ('String -> VARIABLE','String',1,'p_String','sintacticoProyecto.py',120),
  ('repeBool -> bool','repeBool',1,'p_repetirBool','sintacticoProyecto.py',125),
  ('repeBool -> bool COMA repeBool','repeBool',3,'p_repetirBool_B','sintacticoProyecto.py',127),
  ('bool -> BOOLEANPALABRA','bool',1,'p_Bool','sintacticoProyecto.py',129),
  ('bool -> VARIABLE','bool',1,'p_Bool','sintacticoProyecto.py',130),
  ('repeCualquier -> datosprimitivos','repeCualquier',1,'p_repetirCualquiera','sintacticoProyecto.py',136),
  ('repeCualquier -> datosprimitivos COMA repeCualquier','repeCualquier',3,'p_repetirCualquiera_i','sintacticoProyecto.py',138),
  ('comparacion -> valor operadoresComp valor','comparacion',3,'p_comparacion','sintacticoProyecto.py',142),
  ('operadoresComp -> MAYORQUE','operadoresComp',1,'p_operadoresComp','sintacticoProyecto.py',145),
  ('operadoresComp -> DIFERENTE','operadoresComp',1,'p_operadoresComp','sintacticoProyecto.py',146),
  ('operadoresComp -> MENORQUE','operadoresComp',1,'p_operadoresComp','sintacticoProyecto.py',147),
  ('operadoresComp -> ESIGUAL','operadoresComp',1,'p_operadoresComp','sintacticoProyecto.py',148),
  ('tipoDato -> INT','tipoDato',1,'p_tipoDato','sintacticoProyecto.py',152),
  ('tipoDato -> STRING','tipoDato',1,'p_tipoDato','sintacticoProyecto.py',153),
  ('tipoDato -> BOOLEAN','tipoDato',1,'p_tipoDato','sintacticoProyecto.py',154),
  ('argumento -> tipoDato VARIABLE','argumento',2,'p_Argumento','sintacticoProyecto.py',158),
  ('repeArg -> argumento','repeArg',1,'p_repetirArgumento','sintacticoProyecto.py',162),
  ('repeArg -> argumento COMA repeArg','repeArg',3,'p_repetirArgumento_B','sintacticoProyecto.py',166),
  ('control -> if','control',1,'p_control','sintacticoProyecto.py',171),
  ('control -> when','control',1,'p_control','sintacticoProyecto.py',172),
  ('control -> for','control',1,'p_control','sintacticoProyecto.py',173),
  ('if -> ifBoolean','if',1,'p_if','sintacticoProyecto.py',176),
  ('if -> ifComparacion','if',1,'p_if','sintacticoProyecto.py',177),
  ('if -> ifVariable','if',1,'p_if','sintacticoProyecto.py',178),
  ('when -> whenVacio','when',1,'p_when','sintacticoProyecto.py',181),
  ('when -> whenVariable','when',1,'p_when','sintacticoProyecto.py',182),
  ('for -> forRango','for',1,'p_for','sintacticoProyecto.py',185),
  ('for -> forVariable','for',1,'p_for','sintacticoProyecto.py',186),
  ('ifBoolean -> IF LPAREN BOOLEANPALABRA RPAREN LLLAVE RLLAVE','ifBoolean',6,'p_ifBoolean','sintacticoProyecto.py',190),
  ('ifComparacion -> IF LPAREN comparacion RPAREN LLLAVE RLLAVE','ifComparacion',6,'p_ifComparacion','sintacticoProyecto.py',192),
  ('ifVariable -> IF LPAREN VARIABLE RPAREN LLLAVE RLLAVE','ifVariable',6,'p_ifVariable','sintacticoProyecto.py',194),
  ('whenVariable -> WHEN LPAREN VARIABLE RPAREN LLLAVE RLLAVE','whenVariable',6,'p_whenVariable','sintacticoProyecto.py',198),
  ('whenVacio -> WHEN LLLAVE RLLAVE','whenVacio',3,'p_whenVacio','sintacticoProyecto.py',200),
  ('forVariable -> FOR LPAREN VARIABLE IN VARIABLE RPAREN LLLAVE RLLAVE','forVariable',8,'p_forVariable','sintacticoProyecto.py',204),
  ('forRango -> FOR LPAREN VARIABLE IN NUMBER PUNTO PUNTO NUMBER RPAREN LLLAVE RLLAVE','forRango',11,'p_forRango','sintacticoProyecto.py',206),
  ('funcion -> funConSalidaArg','funcion',1,'p_funcion','sintacticoProyecto.py',211),
  ('funcion -> funConSalida','funcion',1,'p_funcion','sintacticoProyecto.py',212),
  ('funcion -> funSinSalidaArg','funcion',1,'p_funcion','sintacticoProyecto.py',213),
  ('funcion -> funSinSalida','funcion',1,'p_funcion','sintacticoProyecto.py',214),
  ('funConSalida -> FUN VARIABLE LPAREN repeArg RPAREN DOSPUNTOS tipoDato LLLAVE RLLAVE','funConSalida',9,'p_funcionConSalida','sintacticoProyecto.py',216),
  ('funSinSalida -> FUN VARIABLE LPAREN repeArg RPAREN LLLAVE RLLAVE','funSinSalida',7,'p_funcionSinSalida','sintacticoProyecto.py',218),
  ('funConSalidaArg -> FUN VARIABLE LPAREN RPAREN DOSPUNTOS tipoDato LLLAVE RLLAVE','funConSalidaArg',8,'p_funcionConSalidaArg','sintacticoProyecto.py',220),
  ('funSinSalidaArg -> FUN VARIABLE LPAREN RPAREN LLLAVE RLLAVE','funSinSalidaArg',6,'p_funcionSinSalidaArg','sintacticoProyecto.py',222),
  ('size -> lista PUNTO SIZE,234')
]
