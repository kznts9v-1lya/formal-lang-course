grammar gql ;

prog: ((stm NEWLINE)* EOF);


stm
    : var '=' expr
    | 'PRINT' expr
    ;

var
    : IDENTIFIER addr
    | IDENTIFIER
    ;

addr
    : '[' INT ']' addr
    | '[' INT ']'
    ;

val:    INT | STRING;

setVal: '{' setElem '}';

setElem
    : val ',' setElem
    |
    ;

expr
    : var
    | val
    | set_start expr ') TO' expr
    | set_final expr ') TO' expr
    | add_start expr ') TO' expr
    | add_final expr ') TO' expr
    | get_start
    | get_final
    | get_reachable
    | get_vertices
    | get_edges
    | get_labels
    | mapsys
    | filtersys
    | load
    | expr intersect expr
    | expr concat expr
    | expr union expr
    | star
    | setVal
    ;

intersect:  '&&';
concat: '..';
union:  '||';
star:   '(' expr ')**';

set_start: 'SET START OF (';
set_final: 'SET FINAL OF (';
add_start: 'ADD START OF (';
add_final: 'ADD FINAL OF (';

get_start: 'SELECT STARTS OF (' expr ')';
get_final: 'SELECT FINALS OF (' expr ')';
get_reachable: 'SELECT REACHABLE OF (' expr ')';
get_vertices: 'SELECT VERTICES OF (' expr ')';
get_edges: 'SELECT EDGES OF (' expr ')';
get_labels: 'SELECT LABELS OF (' expr ')';

mapsys:    'MAP (' lambdasys ')(' expr ')';
filtersys: 'FILTER (' lambdasys ')(' expr ')';

load
    : 'LOAD GRAPH FROM' path
    | 'LOAD GRAPH' path
    ;

path:   STRING;

lambdasys: 'FUN (' var ') ->' op;

inop:  'IN';
multop: '*';
plusop:  '+';

op
    : var inop expr
    | (var | val) multop (var | val)
    | (var | val) plusop (var | val)
    | (var | val)
    ;

NEWLINE     : [\r\n]+ ;
INT         : [0-9]+ ;
IDENTIFIER  : [A-Za-z0-9]+ ;
STRING      : '\'' ~('\'')+ '\'';
WS          :   [ \t\r\n]+ -> skip;
