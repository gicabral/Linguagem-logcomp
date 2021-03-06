# APS- Uma Linguagem de Programação

O objetivo dessa atividade é criar uma linguagem de programação com todas as estruturas básicas: variáveis, condicionais, loops e funções. 

## Motivação
A linguagem criada tem elementos do Python e do C, junto com algumas expressões para torná-la mais didática. Nessa linguagem, tanto as variáveis quanto as funções não precisam ser declaradas com o tipo, o que torna a linguagem mais simples. Além disso, as funções são delimitadas por chaves, para facilitar a vizualização do escopo das funções e não ter que se preocupar com a identação. Os loops e condicionais são escritos como Python, mas terminam com uma expressão intuitiva para facilitar a escrita da linguagem, como "endwhile" e "endif". Assim, o objetivo foi criar uma linguagem com elementos já conhecidos de 2 linguagem muito utilizadas e torná-la mais objetiva e fácil de entender. 

## Exemplos da Linguagem

Exemplo com função, print e operações aritiméticas (está no arquivo myfile.c):

```print(1)

def semestre_7(x,y)
{
    print(x*y)
    print(0)
    print(x+y)
    
    return x/y
}

a = 10
b = 4
print(a**(b-1))
print(semestre_7(a,b))
```

Exemplo com recursão e loop (está no arquivo myfile2.c):

```

def logcomp(x){
    if (x < 2) :
        return x
    endif else :
        return logcomp(x-1) + logcomp(x-1)
    endelse
}     

a = 7
b = 0
while (b < a): 
    print(logcomp(b))
    b = b+1
endwhile
```

Exemplo com operadores lógicos (está no arquivo myfile3.c):

```
a = 3
b = a + 4

print(b > a)

while (!(b == a) && b > 3 || a == 2): 
    a = a + 1
endwhile

print(a)
print(b)
```

## EBNF dessa linguagem 

```diff
PROGRAM = (BLOCK, {BLOCK});
BLOCK = (COMMANDS, {COMMANDS});
DEF = "def", IDENTIFIER, "(", (" "| DEFARGS), ")", "{", BLOCK, "}";
DEFARGS = IDENTIFIER, {",", IDENTIFIER};
DEFCALL = IDENTIFIER, "(", {ARGUMENTS}, ")";
ARGUMENTS = OREXPRESSION | {ARGUMENTS, ",", OREXPRESSION};
COMMANDS = DEF |("if", "(", OREXPRESSION, ")", ":", BLOCK, "endif", {"else", ":", BLOCK, "endelse"}) | (IDENTIFIER, "=", OREXPRESSION)|("print", 
"(", OREXPRESSION, ")") | ("while", "(", OREXPRESSION, ")", ":", BLOCK, "endwhile") | RETURN | OREXPRESSION;
RETURN = "return", {OREXPRESSION};
POWEXPRESSION = (NUMBER | IDENTIFIER | DEFCALL) | ("(", OREXPRESSION, ")");
POWER = POWEXPRESSION, "**", FACTOR;
FACTOR = (FACTOR | POWER), {("+"|"-"), (FACTOR | POWER)};
TERM = FACTOR, {("*"|"/"), FACTOR};
EXPRESSION = TERM, {("+"|"-"), TERM};
REALEXPRESSION = EXPRESSION, {("="|">"|"<"), EXPRESSION};
NOTEXPRESSION = ("!", (NOTEXPRESSION | REALEXPRESSION));
ANDEXPRESSION = NOTEXPRESSION, {"&&", NOTEXPRESSION};
OREXPRESSION = ANDEXPRESSION, {"||", ANDEXPRESSION};
IDENTIFIER = LETTER, {LETTER | DIGIT | "_"};
NUMBER = DIGIT, {DIGIT};
LETTER = (a | ... | z | A | ... | Z);
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );
```

## Ferramentas e Implementação
Para implementar essa linguagem foi utilizada uma biblioteca chamada RPLY, que é uma ferramenta que consegue gerar analisadores em python. 

Estrutura do programa:

```
compyler/
├── ast.py
├── lexer.py
├── main.py
├── files.c
├── parser1.c
└── symboltable.py
```

No arquivo ast.py estão definidos todos os nós da árvore, como declaração de funções e identificadores. No lexer.py estão definidos os símbolos permitidos na linguagem. No parser1.c são chamados os nós da ast e são chamados os tokens do lexer para implementar a EBNF. A symboltable.py implementa uma tabela de símbolos, funções e identificadores. 

## Como rodar
Para rodar o programa criado primeiro instale os requerimentos:

```
pip install -r requirements.txt
```

Depois rode:

```
python RPLY/main.py RPLY/[arquivo]
```
A opções de arquivos são: myfile.c, myfile2.c e myfile3.c
