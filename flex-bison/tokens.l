%{
#include "parser.tab.h"
#include <stdio.h>
#include <stdlib.h>
%}

%%

"True"|"False"                      { printf("BOOL_LITERAL\n"); return BOOL_LITERAL; }
"string"|"int"|"double"|"bool"      { printf("TYPE\n"); return TYPE; }
"void"                              { printf("VOID\n"); return VOID; } 
"print"                             { printf("PRINT\n"); return PRINT; }
"ask"                               { printf("ASK\n"); return ASK; }
"if"                                { printf("IF\n"); return IF; }
"else"                              { printf("ELSE\n"); return ELSE; }
"while"                             { printf("WHILE\n"); return WHILE; }
"func"                              { printf("FUNCTION\n"); return FUNCTION; }
"return"                            { printf("RETURN\n"); return RETURN; }
"+"                                 { printf("PLUS\n"); return PLUS; }
"-"                                 { printf("MINUS\n"); return MINUS; }    
"*"                                 { printf("MULT\n"); return MULT; }
"/"                                 { printf("DIV\n"); return DIV; }
"%"                                 { printf("REMAINDER\n"); return REMAINDER; }
"^"                                 { printf("POW\n"); return POW; }
"and"                               { printf("AND\n"); return AND; }
"or"                                { printf("OR\n"); return OR; }
"="                                 { printf("ASSIGN\n"); return ASSIGN; }
"<"                                 { printf("LESS_THAN\n"); return LESS_THAN; }
"<="                                { printf("LESS_EQUAL\n"); return LESS_EQUAL; }
"=="                                { printf("EQUAL\n"); return EQUAL; }
"!="                                { printf("NOT_EQUAL\n"); return NOT_EQUAL; }
">="                                { printf("GREATER_EQUAL\n"); return GREATER_EQUAL; }
">"                                 { printf("GREATER_THAN\n"); return GREATER_THAN; }
"!"                                 { printf("NOT\n"); return NOT; }
";"                                 { printf("SEMICOLON\n"); return SEMICOLON; }
"->"                                { printf("ARROW\n"); return ARROW; }
"{"                                 { printf("LBRACE\n"); return LBRACE; }
"}"                                 { printf("RBRACE\n"); return RBRACE; }
"("                                 { printf("LPAREN\n"); return LPAREN; }
")"                                 { printf("RPAREN\n"); return RPAREN; }
","                                 { printf("COMMA\n"); return COMMA; }
[A-Za-z_][A-Za-z0-9_]*              { printf("IDENTIFIER\n"); return IDENTIFIER; }
[0-9]+                              { printf("INT_LITERAL\n"); return INT_LITERAL; }
[0-9]+\.[0-9]+                      { printf("DOUBLE_LITERAL\n"); return DOUBLE_LITERAL; }
\"([^\\\"]|\\.)*\"                  { printf("STRING_LITERAL\n"); return STRING_LITERAL; }
[\t\n\f\r ]+                        /* ignore whitespace */
.                                   { printf("Invalid character: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
