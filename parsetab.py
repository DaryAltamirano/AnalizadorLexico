
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER STRINGPALABRA PLUS MINUS TIMES DIVIDE LPAREN RPAREN MAYORQUE MENORQUE VARIABLE IGUAL MOD PUNTOYCOMA DOSPUNTOS ESIGUAL COMA DIFERENTE IF THEN ELSE WHILE VAR VAL INT STRING BOOLEAN FUN SIZE SETOF SET LISTOF LIST PAIR OR ANDtodo : lista \n               | variable \n               | conjunto \n               | pairlista :  ListaConTipo \n               | ListaSinTipo variable : variableConTipo \n                | variableSinTipo conjunto : ConjuntoConTipo \n                | ConjuntoSinTipo variableConTipo :  valovar VARIABLE DOSPUNTOS STRING IGUAL STRINGPALABRAvariableConTipo :  valovar VARIABLE DOSPUNTOS INT IGUAL NUMBERvariableConTipo :  valovar VARIABLE DOSPUNTOS BOOLEAN IGUAL variableSinTipo : valovar VARIABLE IGUAL datosprimitivos ListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE INT MAYORQUE IGUAL LISTOF LPAREN repeInt RPARENListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE STRING MAYORQUE IGUAL LISTOF LPAREN repeString RPARENListaConTipo : valovar VARIABLE DOSPUNTOS LIST MENORQUE BOOLEAN MAYORQUE IGUAL LISTOF LPAREN  RPARENListaSinTipo : valovar VARIABLE IGUAL LISTOF LPAREN repeCualquier RPARENConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE INT MAYORQUE IGUAL SETOF LPAREN repeInt RPARENConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE STRING MAYORQUE IGUAL SETOF LPAREN repeString RPARENConjuntoConTipo : valovar VARIABLE DOSPUNTOS SET MENORQUE BOOLEAN MAYORQUE IGUAL SETOF LPAREN  RPARENConjuntoSinTipo : valovar VARIABLE IGUAL SETOF LPAREN repeCualquier RPARENpair : valovar VARIABLE IGUAL PAIR  LPAREN  datosprimitivos COMA  datosprimitivos RPARENdatosprimitivos : NUMBER \n               | STRINGPALABRA\n               | VARIABLE valovar :  VAR \n               | VALrepeInt : valorrepeInt : valor COMA repeIntvalor : NUMBER\n        | VARIABLErepeString : StringrepeString : String COMA repeStringString : STRINGPALABRA\n        | VARIABLErepeCualquier : datosprimitivosrepeCualquier : datosprimitivos COMA repeCualquier'
    
_lr_action_items = {'VAR':([0,],[13,]),'VAL':([0,],[14,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,18,20,23,24,36,45,46,51,53,68,89,92,93,95,97,98,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-26,-14,-24,-25,-13,-12,-11,-18,-22,-23,-17,-21,-15,-16,-19,-20,]),'VARIABLE':([12,13,14,16,30,31,32,50,52,75,76,78,79,94,96,],[15,-27,-28,18,18,18,18,18,18,81,85,81,85,81,85,]),'IGUAL':([15,26,27,28,54,55,56,57,58,59,],[16,34,35,36,62,63,64,65,66,67,]),'DOSPUNTOS':([15,],[17,]),'PAIR':([16,],[19,]),'LISTOF':([16,62,63,64,],[21,69,70,71,]),'SETOF':([16,65,66,67,],[22,72,73,74,]),'NUMBER':([16,30,31,32,34,50,52,75,78,94,],[23,23,23,23,45,23,23,84,84,84,]),'STRINGPALABRA':([16,30,31,32,35,50,52,76,79,96,],[24,24,24,24,46,24,24,88,88,88,]),'LIST':([17,],[25,]),'STRING':([17,33,37,],[27,43,48,]),'INT':([17,33,37,],[26,42,47,]),'BOOLEAN':([17,33,37,],[28,44,49,]),'SET':([17,],[29,]),'COMA':([18,23,24,38,40,81,83,84,85,87,88,],[-26,-24,-25,50,52,-32,94,-31,-36,96,-35,]),'RPAREN':([18,23,24,39,40,41,60,61,77,80,81,82,83,84,85,86,87,88,90,91,99,100,],[-26,-24,-25,51,-37,53,68,-38,89,92,-32,93,-29,-31,-36,95,-33,-35,97,98,-30,-34,]),'LPAREN':([19,21,22,69,70,71,72,73,74,],[30,31,32,75,76,77,78,79,80,]),'MENORQUE':([25,29,],[33,37,]),'MAYORQUE':([42,43,44,47,48,49,],[54,55,56,57,58,59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'todo':([0,],[1,]),'lista':([0,],[2,]),'variable':([0,],[3,]),'conjunto':([0,],[4,]),'pair':([0,],[5,]),'ListaConTipo':([0,],[6,]),'ListaSinTipo':([0,],[7,]),'variableConTipo':([0,],[8,]),'variableSinTipo':([0,],[9,]),'ConjuntoConTipo':([0,],[10,]),'ConjuntoSinTipo':([0,],[11,]),'valovar':([0,],[12,]),'datosprimitivos':([16,30,31,32,50,52,],[20,38,40,40,60,40,]),'repeCualquier':([31,32,52,],[39,41,61,]),'repeInt':([75,78,94,],[82,90,99,]),'valor':([75,78,94,],[83,83,83,]),'repeString':([76,79,96,],[86,91,100,]),'String':([76,79,96,],[87,87,87,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> todo","S'",1,None,None,None),
  ('todo -> lista','todo',1,'p_todo','sintacticoProyecto.py',17),
  ('todo -> variable','todo',1,'p_todo','sintacticoProyecto.py',18),
  ('todo -> conjunto','todo',1,'p_todo','sintacticoProyecto.py',19),
  ('todo -> pair','todo',1,'p_todo','sintacticoProyecto.py',20),
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
  ('ListaConTipo -> valovar VARIABLE DOSPUNTOS LIST MENORQUE BOOLEAN MAYORQUE IGUAL LISTOF LPAREN RPAREN','ListaConTipo',11,'p_ListadeTipoBool','sintacticoProyecto.py',60),
  ('ListaSinTipo -> valovar VARIABLE IGUAL LISTOF LPAREN repeCualquier RPAREN','ListaSinTipo',7,'p_ListaSinTipo','sintacticoProyecto.py',63),
  ('ConjuntoConTipo -> valovar VARIABLE DOSPUNTOS SET MENORQUE INT MAYORQUE IGUAL SETOF LPAREN repeInt RPAREN','ConjuntoConTipo',12,'p_ConjuntodeTipoInt','sintacticoProyecto.py',68),
  ('ConjuntoConTipo -> valovar VARIABLE DOSPUNTOS SET MENORQUE STRING MAYORQUE IGUAL SETOF LPAREN repeString RPAREN','ConjuntoConTipo',12,'p_ConjuntoTipoString','sintacticoProyecto.py',70),
  ('ConjuntoConTipo -> valovar VARIABLE DOSPUNTOS SET MENORQUE BOOLEAN MAYORQUE IGUAL SETOF LPAREN RPAREN','ConjuntoConTipo',11,'p_ConjuntodeTipoBool','sintacticoProyecto.py',73),
  ('ConjuntoSinTipo -> valovar VARIABLE IGUAL SETOF LPAREN repeCualquier RPAREN','ConjuntoSinTipo',7,'p_ConjuntoSinTipo','sintacticoProyecto.py',76),
  ('pair -> valovar VARIABLE IGUAL PAIR LPAREN datosprimitivos COMA datosprimitivos RPAREN','pair',9,'p_Pair','sintacticoProyecto.py',81),
  ('datosprimitivos -> NUMBER','datosprimitivos',1,'p_algunTipo','sintacticoProyecto.py',96),
  ('datosprimitivos -> STRINGPALABRA','datosprimitivos',1,'p_algunTipo','sintacticoProyecto.py',97),
  ('datosprimitivos -> VARIABLE','datosprimitivos',1,'p_algunTipo','sintacticoProyecto.py',98),
  ('valovar -> VAR','valovar',1,'p_valovar','sintacticoProyecto.py',101),
  ('valovar -> VAL','valovar',1,'p_valovar','sintacticoProyecto.py',102),
  ('repeInt -> valor','repeInt',1,'p_repetirInt','sintacticoProyecto.py',107),
  ('repeInt -> valor COMA repeInt','repeInt',3,'p_repetirInt_i','sintacticoProyecto.py',109),
  ('valor -> NUMBER','valor',1,'p_valor','sintacticoProyecto.py',111),
  ('valor -> VARIABLE','valor',1,'p_valor','sintacticoProyecto.py',112),
  ('repeString -> String','repeString',1,'p_repetirString','sintacticoProyecto.py',117),
  ('repeString -> String COMA repeString','repeString',3,'p_repetirString_s','sintacticoProyecto.py',119),
  ('String -> STRINGPALABRA','String',1,'p_String','sintacticoProyecto.py',121),
  ('String -> VARIABLE','String',1,'p_String','sintacticoProyecto.py',122),
  ('repeCualquier -> datosprimitivos','repeCualquier',1,'p_repetirCualquiera','sintacticoProyecto.py',128),
  ('repeCualquier -> datosprimitivos COMA repeCualquier','repeCualquier',3,'p_repetirCualquiera_i','sintacticoProyecto.py',130),
]
