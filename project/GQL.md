# Graph Query Language (GQL)

## Описание абстрактного синтаксиса

```
prog = List<stmt>

stmt =
    Bind of var * expr
  | Print of expr

val =
    String of string
  | Int of int
  | Bool of bool
  | Path of path
  | List of string
  | List of int
  | List of bool

expr =
    Var of var                   // переменные
  | Val of val                   // константы
  | Set_start of Set<val> * expr // задать множество стартовых состояний
  | Set_final of Set<val> * expr // задать множество финальных состояний
  | Add_start of Set<val> * expr // добавить состояния в множество стартовых
  | Add_final of Set<val> * expr // добавить состояния в множество финальных
  | Get_start of expr            // получить множество стартовых состояний
  | Get_final of expr            // получить множество финальных состояний
  | Get_reachable of expr        // получить все пары достижимых вершин
  | Get_vertices of expr         // получить все вершины
  | Get_edges of expr            // получить все рёбра
  | Get_labels of expr           // получить все метки
  | Map of lambda * expr         // классический map
  | Filter of lambda * expr      // классический filter
  | Load of path                 // загрузка графа
  | Intersect of expr * expr     // пересечение языков
  | Concat of expr * expr        // конкатенация языков
  | Union of expr * expr         // объединение языков
  | Star of expr                 // замыкание языков (звезда Клини)
  | Smb of expr                  // единичный переход

lambda =
    Lambda of List<var> * expr
```

## Правила вывода типов

Константы типизируются очевидным образом.

Тип переменной определяется типом выражения, с которым она связана.
```
[b(v)] => t
_________________
[Var (v)](b) => t
```

Загрузить можно только автомат.
```
_________________________
[Load (p)](b) => FA<int>
```

Установка финальных состояний, а так же добавление стартовых и финальных типизируется аналогично типизации установки стартовых, которая приведена ниже.
```
[s](b) => Set<t> ;  [e](b) => FA<t>
___________________________________
[Set_start (s, e)](b) => FA<t>

[s](b) => Set<t> ;  [e](b) => RSM<t>
____________________________________
[Set_start (s, e)](b) => RSM<t>
```

Получение финальных типизируется аналогично получению стартовых, правила для которого приведены ниже.
```
[e](b) => FA<t>
____________________________
[Get_start (e)](b) => Set<t>

[e](b) => RSM<t>
____________________________
[Get_start (e)](b) => RSM<t>
```

```
[e](b) => FA<t>
__________________________________
[Get_reachable (e)](b) => Set<t*t>

[e](b) => RSM<t>
__________________________________
[Get_reachable (e)](b) => Set<t*t>
```

```
[e](b) => FA<t>
_______________________________
[Get_vertices (e)](b) => Set<t>

[e](b) => RSM<t>
_______________________________
[Get_vertices (e)](b) => Set<t>

[e](b) => FA<t>
______________________________________
[Get_edges (e)](b) => Set<t*string*t>

[e](b) => RSM<t>
______________________________________
[Get_edges (e)](b) => Set<t*string*t>

[e](b) => FA<t>
__________________________________
[Get_labels (e)](b) => Set<string>

[e](b) => RSM<t>
__________________________________
[Get_labels (e)](b) => Set<string>
```

Правила для ```map``` и ```filter``` традиционные.
```
[f](b) => t1 -> t2 ; [q](b) => Set<t1>
_______________________________________
[Map (f,q)](b) => Set<t2>

[f](b) => t1 -> bool ; [q](b) => Set<t1>
________________________________________
[Filter (f,q)](b) => Set<t1>
```

Пересечение для двух КС не определено.
```
[e1](b) => FA<t1> ;  [e2](b) => FA<t2>
______________________________________
[Intersect (e1, e2)](b) => FA<t1*t2>

[e1](b) => FA<t1> ;  [e2](b) => RSM<t2>
_______________________________________
[Intersect (e1, e2)](b) => RSM<t1*t2>

[e1](b) => RSM<t1> ;  [e2](b) => FA<t2>
_______________________________________
[Intersect (e1, e2)](b) => RSM<t1*t2>
```

Остальные операции над автоматами типизируются согласно формальных свойств классов языков.
```
[e1](b) => FA<t> ;  [e2](b) => FA<t>
_____________________________________
[Concat (e1, e2)](b) => FA<t>

[e1](b) => FA<t> ;  [e2](b) => RSM<t>
______________________________________
[Concat (e1, e2)](b) => RSM<t>

[e1](b) => RSM<t> ;  [e2](b) => FA<t>
______________________________________
[Concat (e1, e2)](b) => RSM<t>

[e1](b) => RSM<t> ;  [e2](b) => RSM<t>
______________________________________
[Concat (e1, e2)](b) => RSM<t>
```

```
[e1](b) => FA<t> ;  [e2](b) => FA<t>
______________________________________
[Union (e1, e2)](b) => FA<t>

[e1](b) => FA<t> ;  [e2](b) => RSM<t>
_______________________________________
[Union (e1, e2)](b) => RSM<t>

[e1](b) => RSM<t> ;  [e2](b) => FA<t>
_______________________________________
[Union (e1, e2)](b) => RSM<t>

[e1](b) => RSM<t> ;  [e2](b) => RSM<t>
_______________________________________
[Union (e1, e2)](b) => RSM<t>
```

```
[e](b) => FA<t>
______________________
[Star (e)](b) => FA<t>

[e](b) => RSM<t>
______________________
[Star (e](b) => RSM<t>
```

```
[e](b) => string
________________________
[Smb (e)](b) => FA<int>
```

## Динамическая семантика языка запросов

Связывание переопределяет имя.

```
[e](b1) => x,b2
_____________________________________
[Bind (v, e)](b1) => (), (b1(v) <= x)
```

Загрузить можно только автомат и у него все вершины будут стартовыми и финальными.

```
[p](b1) => s,b2 ; read_fa_from_file s => fa
_____________________________________
[Load (p)](b1) => (fa | fa.start = fa.vertices, fa.final = fa.vertices), b1
```

## Описание конкретного синтаксиса языка

[...] - скобки грамматики

(...) - скобки конкретного синтаксиса

<...> - скобки полиморфизма типов

-> - стрелка грамматики

=> - стрелка конкретного синтаксиса

```
program -> stmt ; program | eps
stmt -> var = expr | PRINT ( expr )

lower_symbol -> [a-z]
upper_symbol -> [A-Z]
digit -> [0-9]

int -> 0 | [1-9] digit*
string -> [_ | . | lower_symbol | upper_symbol] [_ | . | lower_symbol | upper_symbol | digit]*
bool -> TRUE | FALSE
path -> " [\ | : | / | _ | . | lower_symbol | upper_symbol | digit]+ "

var -> string
val ->
    int
    | " string "
    | bool
    | path
    | list<int>
    | list<" string ">
    | list<bool>
set ->
    set<int>
    | set<" string ">
    | RANGE ( int , int )

expr -> var
expr -> val
expr -> graph
graph -> " string "
graph -> SET_START ( set , graph )
graph -> SET_FINAL ( set , graph )
graph -> ADD_START ( set , graph )
graph -> ADD_FINAL ( set , graph )

expr -> vertex | vertices
vertex -> int
vertices -> set<vertex> | RANGE ( int , int )
vertices -> GET_START ( graph )
vertices -> GET_FINAL ( set , graph )

expr -> vertices_pair
vertices_pair -> set<(int, int)>
vertices_pair -> GET_REACHABLE ( graph )

vertices -> GET_VERTICES ( graph )

expr -> edge | edges
edge -> (int, " string ", int) | (int, int, int)
edges -> set<edge>
edges -> GET_EDGES ( graph )

expr -> labels
labels -> set<int> | set<" string ">
labels -> GET_LABELS ( graph )

expr -> MAP ( lambda , expr )
expr -> FILTER ( lambda , expr )
graph -> LOAD ( path )
graph -> INTERSECT ( graph , graph )
graph -> CONCAT ( graph , graph )
graph -> UNION ( graph , graph )
graph -> STAR ( graph , graph )

lambda -> ( list<var> => [bool_expr | expr] )
bool_expr ->
    bool_expr or bool_expr
    | bool_expr and bool_expr
    | not bool_expr
    | bool
    | HAS_LABEL ( edge , " string " )
    | IS_START ( vertex )
    | IS_FINAL ( vertex )
    | x IN set<x>

list<x> -> LIST ( x [, x]* ) | LIST ( )
set<x> -> SET ( x [, x]* ) | SET ( )
```

## Пример программы

Данный скрипт загружает граф "core" и создаёт его копию с заданными стартовыми и финальными вершинами.
Затем создает два запроса на метках графа. Наконец, выполняет пересечение исходного графа (все вершины
тогда будут стартовыми и финальными по умолчанию) с первым запросом и его копии со вторым запросом,
печатая результат.

```
graph1 = LOAD("core")
graph2 = SET_START(RANGE(1, 10), SET_FINAL(GET_VERTICES(graph), graph)))

query_part = UNION("label1", "label2")

query1 = STAR(UNION("type_of", query_part))
query2 = CONCAT("sub_class_of", query_part)

result1 = INTERSECT(graph1, query1)
result2 = INTERSECT(graph2, query2)

PRINT(result1)
PRINT(result2)
```