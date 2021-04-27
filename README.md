# APS- Uma Linguagem de Programação

O objetivo dessa atividade é criar uma linguagem de programação com todas as estruturas básicas: variáveis, condicionais, loops e funções. 

## EBNF dessa linguagem 

```diff
DEF = "def", IDENTIFIER, "(", (" "| IDENTIFIER), ")", "{", COMMANDS, "}";
BLOCK = (" " | COMMANDS, {COMMANDS});
COMMANDS = " "|("if", "(", EXPRESSIONIF, ")", ":", BLOCK, {"else", ":", BLOCK}, "endif") | (IDENTIFIER, "=", EXPRESSION)|("print", 
"(", EXPRESSION, ")") | ("while", "(", EXPRESSIONIF, ")", ":", BLOCK, "endwhile");
FACTOR = NUMBER| ("(", EXPRESSIONIF, ")") | (("+"|"-"|"not"), FACTOR) | IDENTIFIER;
TERM = FACTOR, {("*"|"/"|"and"), FACTOR};
EXPRESSION = TERM, {("+"|"-"|"or"), TERM};
EXPRESSIONIF = EXPRESSION, {("="|">"|"<"), EXPRESSION};
IDENTIFIER = LETTER, {LETTER | DIGIT | "_"};
NUMBER = DIGIT, {DIGIT};
LETTER = (a | ... | z | A | ... | Z);
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );
```

## Diagrama Sintático dessa linguagem

![](/imagens/diagrama.png)
