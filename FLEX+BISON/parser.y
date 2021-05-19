%{
    #include "node.h"
    NBlock *programBlock; /* the top level root node of our final AST */
 
    extern int yylex();
    void yyerror(const char *s) { printf("ERROR: %s/n", s); }
%}

%union {
  int number;
  string *strType; // goes with string_const in lex
}

%token<number> TINTEGER
%token<strType>  TIDENTIFIER 
%token TCEQ TCNE TCLT TCGT TEQUAL TLPAREN TRPAREN TLBRACE TRBRACE TTWOP TCOMMA TPLUS TMINUS TMUL TDIV TAND TOR TDEF TIF TELSE TENDIF TPRINT TWHILE TENDWHILE TINT TBOOL TSTRING TCALL TINPUT TTRUE TFALSE

 
/* Operator precedence for mathematical operators */
%left TPLUS TMINUS 
%left TMUL TDIV


%start Program
%%
Program: Def Program | Def;

Def: TDEF TIDENTIFIER TLPAREN Argument TRPAREN TLBRACE Block TRBRACE;

Block: Command Block| Command;

Command: TIF TLPAREN RealExpression TRPAREN TTWOP Block TENDIF | TIF TLPAREN RealExpression TRPAREN TTWOP Block TELSE Block TENDIF | TIDENTIFIER TEQUAL RealExpression | TPRINT TLPAREN RealExpression TRPAREN | TWHILE TLPAREN RealExpression TRPAREN TTWOP Block TENDWHILE | Type TIDENTIFIER | TCALL TIDENTIFIER TLPAREN Loop TRPAREN;

Type: TINT | TBOOL | TSTRING;

Argument: | Type TIDENTIFIER | Type TIDENTIFIER TCOMMA Argument;

Loop: | RealExpression | RealExpression TCOMMA Loop;

RealExpression: Expression | Expression TCEQ Expression | Expression TCGT Expression | Expression TCLT Expression;

Expression: Term | Term TPLUS Term | Term TMINUS Term | Term TOR Term;

Term: Factor | Factor TMUL Factor | Factor TDIV Factor | Factor TAND Factor;

Factor: TINTEGER | TTRUE | TFALSE | TINPUT | TLPAREN RealExpression TRPAREN | TPLUS Factor | TMINUS Factor | TCNE Factor | TIDENTIFIER | TIDENTIFIER TLPAREN Loop TRPAREN;
%%
