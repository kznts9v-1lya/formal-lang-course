grammar gql ;

prog : (EOL? WS? stmt SEMICOLON EOL?)+ EOF ;

stmt : PRINT expr
     | var WS? ASSIGN WS? expr
     ;

expr : LP expr RP
     | anfunc
     | mapping
     | filtering
     | var
     | val
     | NOT expr
     | expr KLEENE
     | expr IN expr
     | expr AND expr
     | expr DOT expr
     | expr OR expr
     ;

val : boolean
    | graph
    | edges
    | labels
    | vertices
    ;

graph : load_graph
      | cfg
      | set_start
      | set_final
      | add_start
      | add_final
      | LP graph RP
      ;

load_graph : LOAD (string | path) ;
set_start : SET START OF (graph | var) TO (vertices | var) ;
set_final : SET FINAL OF (graph | var) TO (vertices | var) ;
add_start : ADD START OF (graph | var) TO (vertices | var) ;
add_final : ADD FINAL OF (graph | var) TO (vertices | var) ;

cfg: CFG ;

vertices : vertex
       | vertices_range
       | vertices_set
       | select_reachable
       | select_final
       | select_start
       | select_vertices
       | LP vertices RP
       ;

vertex : INT ;

edges : edge
      | edges_set
      | select_edges
      ;

edge : LP vertex COMMA label COMMA vertex RP
     | LP vertex COMMA vertex RP
     ;

labels : label
       | labels_set
       | select_labels
       ;

label : string ;

anfunc : FUN variables DOUBLE_ARROW expr
       | LP anfunc RP
       ;

mapping : MAP anfunc expr ;
filtering : FILTER anfunc expr ;

select_edges : SELECT EDGES FROM (graph | var) ;
select_labels : SELECT LABELS FROM (graph | var) ;
select_reachable : SELECT REACHABLE VERTICES FROM (graph | var) ;
select_start : SELECT START VERTICES FROM (graph | var) ;
select_final : SELECT FINAL VERTICES FROM (graph | var) ;
select_vertices : SELECT VERTICES FROM (graph | var) ;
vertices_range : LCB INT COLON INT RCB ;

string : STRING ;
path : PATH ;

vertices_set : LCB (INT COMMA)* (INT)? RCB
             | vertices_range
             ;

labels_set : LCB (STRING COMMA)* (STRING)? RCB ;

edges_set : LCB (edge COMMA)* (edge)? RCB ;

var : ID ;

var_edge : LP var COMMA var RP
         | LP var COMMA var COMMA var RP
         | LP LP var COMMA var RP COMMA var COMMA LP var COMMA var RP RP
         ;

variables : (var COMMA)* var?
     | var_edge
     ;

boolean : TRUE | FALSE ;

FUN : WS? 'FUN' WS? ;
LOAD : WS? 'LOAD' WS? ;
SET : WS? 'SET' WS? ;
ADD : WS? 'ADD' WS? ;
OF : WS? 'OF' WS? ;
TO : WS? 'TO' WS? ;
VERTICES : WS? 'VERTICES' WS? ;
LABELS : WS? 'LABELS' WS? ;
SELECT : WS? 'SELECT' WS? ;
EDGES : WS? 'EDGES' WS? ;
REACHABLE : WS? 'REACHABLE' WS? ;
START : WS? 'START' WS? ;
FINAL : WS? 'FINAL' WS? ;
FROM : WS? 'FROM' WS? ;
FILTER : WS? 'FILTER' WS? ;
MAP : WS? 'MAP' WS? ;
PRINT : WS? 'PRINT' WS? ;

TRUE : 'TRUE' ;
FALSE : 'FALSE' ;

ASSIGN : WS? '=' WS? ;
AND : WS? '&' WS? ;
OR : WS? '|' WS? ;
NOT : WS? 'NOT' WS? ;
IN : WS? 'IN' WS? ;
KLEENE : WS? '*' WS? ;
DOT : WS? '.' WS? ;
COMMA : WS? ',' WS? ;
SEMICOLON : ';' WS? ;
LCB : WS? '{' WS? ;
RCB : WS? '}' WS? ;
LP : WS? '(' WS? ;
RP : WS? ')' WS? ;
QUOT : '"' ;
COLON : WS? ':' WS? ;
DOUBLE_ARROW : WS? '=>' WS? ;

ARROW : '->' ;
TRIPLE_QUOT : '"""' ;
CFG : TRIPLE_QUOT (CHAR | DIGIT | ' ' | '\n' | ARROW)* TRIPLE_QUOT ;

ID : ('_' | CHAR) ID_CHAR* ;

INT : NONZERO_DIGIT DIGIT* | '0' ;
STRING : QUOT (CHAR | DIGIT | '_' | ' ')* QUOT ;
PATH : QUOT (CHAR | DIGIT | '_' | ' ' | '/' | '\\' | COLON | DOT)* QUOT ;
ID_CHAR : (CHAR | DIGIT | '_') ;
CHAR : [a-z] | [A-Z] ;
NONZERO_DIGIT : [1-9] ;
DIGIT : [0-9] ;

WS : [ \t\r]+ -> skip ;
EOL : [\n]+ ;
