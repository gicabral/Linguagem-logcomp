%{
#include "node.h"
#include "parser.hpp"
#define SAVE_TOKEN yylval.string = new std::string(yytext, yyleng)
#define TOKEN(t) (yylval.token = t)
extern "C" int yywrap() { }
%}
 
%%
 
"="                     {return TEQUAL;}
","                     {return TCOMMA;}
"=="                    {return TCEQ;}
"!="                    {return TCNE;}
"<"                     {return TCLT;}
">"                     {return TCGT;}
"("                     {return TLPAREN;}
")"                     {return TRPAREN;}
"{"                     {return TLBRACE;}
"}"                     {return TRBRACE;}
"+"                     {return TPLUS;}
"-"                     {return TMINUS;}
"*"                     {return TMUL;}
"/"                     {return TDIV;}
"def"                   {return TDEF;}
"if"                    {return TIF;}
"else"                  {return TELSE;}
"endif"                 {return TENDIF;}
"print"                 {return TPRINT;}
"while"                 {return TWHILE;}
":"                     {return TTWOP;}
"endwhile"              {return TENDWHILE;}
"&&"                    {return TAND;}
"||"                    {return TOR;}
"int"                   {return TINT;}
"bool"                  {return TBOOL;}
"string"                {return TSTRING;}
"call"                  {return TCALL;}
"input"                 {return TINPUT;}
"true"                  {return TTRUE;}
"false"                 {return TFALSE;}
[ /t/n]                 ;

[a-zA-Z_][a-zA-Z0-9_]*  SAVE_TOKEN; return TIDENTIFIER;
[0-9]+                  SAVE_TOKEN; return TINTEGER;

.                       printf("Unknown token!/n"); yyterminate();
 
%%