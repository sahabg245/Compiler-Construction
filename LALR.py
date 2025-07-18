
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftGTLTGEQLEQEQNEQleftPLUSMINUSleftTIMESDIVIDEAND ASSIGN BOOL CASE DIVIDE ELSE EQ FLOAT FOR GEQ GT ID IF INT LBRACE LEQ LPAREN LT MINUS NEQ NOT NUMBER OR PLUS PRINT RBRACE RETURN RPAREN SEMICOLON STRING STRING SWITCH TIMES WHILEprogram : statement_liststatement_list : statement\n                      | statement_list statementstatement : INT ID SEMICOLON\n                 | FLOAT ID SEMICOLON\n                 | BOOL ID SEMICOLON\n                 | STRING ID SEMICOLON\n                 | INT ID ASSIGN expression SEMICOLON\n                 | FLOAT ID ASSIGN expression SEMICOLON\n                 | BOOL ID ASSIGN expression SEMICOLON\n                 | STRING ID ASSIGN expression SEMICOLONstatement : ID ASSIGN expression SEMICOLONstatement : IF LPAREN expression RPAREN statement ELSE statement\n                 | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACEstatement : WHILE LPAREN expression RPAREN statement\n                 | WHILE LPAREN expression RPAREN LBRACE statement_list RBRACEstatement : PRINT LPAREN expression RPAREN SEMICOLONexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : expression GT expression\n                  | expression LT expression\n                  | expression GEQ expression\n                  | expression LEQ expression\n                  | expression EQ expression\n                  | expression NEQ expressionexpression : expression AND expression\n                  | expression OR expression\n                  | NOT expressionexpression : NUMBERexpression : IDexpression : STRING'
    
_lr_action_items = {'INT':([0,2,3,12,21,28,30,32,38,55,56,58,71,72,73,75,76,77,78,79,80,81,82,84,86,87,88,],[4,4,-2,-3,-4,-5,-6,-7,-12,4,4,-8,-9,-10,-11,4,-15,4,-17,4,4,4,-13,-16,4,4,-14,]),'FLOAT':([0,2,3,12,21,28,30,32,38,55,56,58,71,72,73,75,76,77,78,79,80,81,82,84,86,87,88,],[6,6,-2,-3,-4,-5,-6,-7,-12,6,6,-8,-9,-10,-11,6,-15,6,-17,6,6,6,-13,-16,6,6,-14,]),'BOOL':([0,2,3,12,21,28,30,32,38,55,56,58,71,72,73,75,76,77,78,79,80,81,82,84,86,87,88,],[7,7,-2,-3,-4,-5,-6,-7,-12,7,7,-8,-9,-10,-11,7,-15,7,-17,7,7,7,-13,-16,7,7,-14,]),'STRING':([0,2,3,12,14,18,19,20,21,22,25,28,29,30,31,32,33,38,39,40,41,42,43,44,45,46,47,48,49,50,55,56,58,71,72,73,75,76,77,78,79,80,81,82,84,86,87,88,],[8,8,-2,-3,27,27,27,27,-4,27,27,-5,27,-6,27,-7,27,-12,27,27,27,27,27,27,27,27,27,27,27,27,8,8,-8,-9,-10,-11,8,-15,8,-17,8,8,8,-13,-16,8,8,-14,]),'ID':([0,2,3,4,6,7,8,12,14,18,19,20,21,22,25,28,29,30,31,32,33,38,39,40,41,42,43,44,45,46,47,48,49,50,55,56,58,71,72,73,75,76,77,78,79,80,81,82,84,86,87,88,],[5,5,-2,13,15,16,17,-3,23,23,23,23,-4,23,23,-5,23,-6,23,-7,23,-12,23,23,23,23,23,23,23,23,23,23,23,23,5,5,-8,-9,-10,-11,5,-15,5,-17,5,5,5,-13,-16,5,5,-14,]),'IF':([0,2,3,12,21,28,30,32,38,55,56,58,71,72,73,75,76,77,78,79,80,81,82,84,86,87,88,],[9,9,-2,-3,-4,-5,-6,-7,-12,9,9,-8,-9,-10,-11,9,-15,9,-17,9,9,9,-13,-16,9,9,-14,]),'WHILE':([0,2,3,12,21,28,30,32,38,55,56,58,71,72,73,75,76,77,78,79,80,81,82,84,86,87,88,],[10,10,-2,-3,-4,-5,-6,-7,-12,10,10,-8,-9,-10,-11,10,-15,10,-17,10,10,10,-13,-16,10,10,-14,]),'PRINT':([0,2,3,12,21,28,30,32,38,55,56,58,71,72,73,75,76,77,78,79,80,81,82,84,86,87,88,],[11,11,-2,-3,-4,-5,-6,-7,-12,11,11,-8,-9,-10,-11,11,-15,11,-17,11,11,11,-13,-16,11,11,-14,]),'$end':([1,2,3,12,21,28,30,32,38,58,71,72,73,76,78,82,84,88,],[0,-1,-2,-3,-4,-5,-6,-7,-12,-8,-9,-10,-11,-15,-17,-13,-16,-14,]),'RBRACE':([3,12,21,28,30,32,38,58,71,72,73,76,78,80,81,82,84,87,88,],[-2,-3,-4,-5,-6,-7,-12,-8,-9,-10,-11,-15,-17,83,84,-13,-16,88,-14,]),'ASSIGN':([5,13,15,16,17,],[14,22,29,31,33,]),'LPAREN':([9,10,11,],[18,19,20,]),'SEMICOLON':([13,15,16,17,23,24,26,27,37,51,52,53,54,57,59,60,61,62,63,64,65,66,67,68,69,70,],[21,28,30,32,-32,38,-31,-33,58,-30,71,72,73,78,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,]),'NOT':([14,18,19,20,22,25,29,31,33,39,40,41,42,43,44,45,46,47,48,49,50,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'NUMBER':([14,18,19,20,22,25,29,31,33,39,40,41,42,43,44,45,46,47,48,49,50,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'ELSE':([21,28,30,32,38,58,71,72,73,74,76,78,82,83,84,88,],[-4,-5,-6,-7,-12,-8,-9,-10,-11,79,-15,-17,-13,85,-16,-14,]),'PLUS':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,39,-31,-33,39,39,39,39,39,39,39,39,-18,-19,-20,-21,39,39,39,39,39,39,39,39,]),'MINUS':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,40,-31,-33,40,40,40,40,40,40,40,40,-18,-19,-20,-21,40,40,40,40,40,40,40,40,]),'TIMES':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,41,-31,-33,41,41,41,41,41,41,41,41,41,41,-20,-21,41,41,41,41,41,41,41,41,]),'DIVIDE':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,42,-31,-33,42,42,42,42,42,42,42,42,42,42,-20,-21,42,42,42,42,42,42,42,42,]),'GT':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,43,-31,-33,43,43,43,43,43,43,43,43,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,43,43,]),'LT':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,44,-31,-33,44,44,44,44,44,44,44,44,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,44,44,]),'GEQ':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,45,-31,-33,45,45,45,45,45,45,45,45,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,45,45,]),'LEQ':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,46,-31,-33,46,46,46,46,46,46,46,46,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,46,46,]),'EQ':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,47,-31,-33,47,47,47,47,47,47,47,47,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,47,47,]),'NEQ':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,48,-31,-33,48,48,48,48,48,48,48,48,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,48,48,]),'AND':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,49,-31,-33,49,49,49,49,-30,49,49,49,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,49,]),'OR':([23,24,26,27,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,50,-31,-33,50,50,50,50,-30,50,50,50,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,]),'RPAREN':([23,26,27,34,35,36,51,59,60,61,62,63,64,65,66,67,68,69,70,],[-32,-31,-33,55,56,57,-30,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,]),'LBRACE':([55,56,85,],[75,77,86,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,75,77,86,],[2,80,81,87,]),'statement':([0,2,55,56,75,77,79,80,81,86,87,],[3,12,74,76,3,3,82,12,12,3,12,]),'expression':([14,18,19,20,22,25,29,31,33,39,40,41,42,43,44,45,46,47,48,49,50,],[24,34,35,36,37,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',18),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',22),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',23),
  ('statement -> INT ID SEMICOLON','statement',3,'p_statement_declaration','parser.py',28),
  ('statement -> FLOAT ID SEMICOLON','statement',3,'p_statement_declaration','parser.py',29),
  ('statement -> BOOL ID SEMICOLON','statement',3,'p_statement_declaration','parser.py',30),
  ('statement -> STRING ID SEMICOLON','statement',3,'p_statement_declaration','parser.py',31),
  ('statement -> INT ID ASSIGN expression SEMICOLON','statement',5,'p_statement_declaration','parser.py',32),
  ('statement -> FLOAT ID ASSIGN expression SEMICOLON','statement',5,'p_statement_declaration','parser.py',33),
  ('statement -> BOOL ID ASSIGN expression SEMICOLON','statement',5,'p_statement_declaration','parser.py',34),
  ('statement -> STRING ID ASSIGN expression SEMICOLON','statement',5,'p_statement_declaration','parser.py',35),
  ('statement -> ID ASSIGN expression SEMICOLON','statement',4,'p_statement_assignment','parser.py',49),
  ('statement -> IF LPAREN expression RPAREN statement ELSE statement','statement',7,'p_statement_if_else','parser.py',62),
  ('statement -> IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE','statement',11,'p_statement_if_else','parser.py',63),
  ('statement -> WHILE LPAREN expression RPAREN statement','statement',5,'p_statement_while','parser.py',72),
  ('statement -> WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE','statement',7,'p_statement_while','parser.py',73),
  ('statement -> PRINT LPAREN expression RPAREN SEMICOLON','statement',5,'p_statement_print','parser.py',79),
  ('expression -> expression PLUS expression','expression',3,'p_expression_arithmetic','parser.py',85),
  ('expression -> expression MINUS expression','expression',3,'p_expression_arithmetic','parser.py',86),
  ('expression -> expression TIMES expression','expression',3,'p_expression_arithmetic','parser.py',87),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_arithmetic','parser.py',88),
  ('expression -> expression GT expression','expression',3,'p_expression_relational','parser.py',92),
  ('expression -> expression LT expression','expression',3,'p_expression_relational','parser.py',93),
  ('expression -> expression GEQ expression','expression',3,'p_expression_relational','parser.py',94),
  ('expression -> expression LEQ expression','expression',3,'p_expression_relational','parser.py',95),
  ('expression -> expression EQ expression','expression',3,'p_expression_relational','parser.py',96),
  ('expression -> expression NEQ expression','expression',3,'p_expression_relational','parser.py',97),
  ('expression -> expression AND expression','expression',3,'p_expression_boolean','parser.py',101),
  ('expression -> expression OR expression','expression',3,'p_expression_boolean','parser.py',102),
  ('expression -> NOT expression','expression',2,'p_expression_boolean','parser.py',103),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',112),
  ('expression -> ID','expression',1,'p_expression_identifier','parser.py',116),
  ('expression -> STRING','expression',1,'p_expression_string','parser.py',125),
]
