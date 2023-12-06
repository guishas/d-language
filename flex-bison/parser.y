%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();
void yyerror(const char *s) { printf("ERROR: %s\n", s); }
%}

%token STRING_LITERAL INT_LITERAL DOUBLE_LITERAL BOOL_LITERAL
%token IDENTIFIER FUNCTION ASK 
%token TYPE VOID
%token AND OR
%token NOT EQUAL NOT_EQUAL LESS_THAN LESS_EQUAL GREATER_THAN GREATER_EQUAL
%token PRINT
%token IF ELSE WHILE
%token RETURN ARROW
%token PLUS MINUS 
%token MULT DIV POW REMAINDER
%token LPAREN RPAREN
%token LBRACE RBRACE
%token COMMA SEMICOLON
%token ASSIGN

%start program

%%

program:
    statement_list
    ;

statement_list:
    statement 
    | statement_list statement 
    ;

statement:
    type_statement SEMICOLON
    | assignment_statement SEMICOLON 
    | function_definition_statement
    | function_call_statement SEMICOLON
    | print_statement SEMICOLON 
    | while_statement
    | if_statement
    | return_statement SEMICOLON
    ;

block:
    LBRACE statement_list RBRACE
    ;

type_statement:
    TYPE IDENTIFIER
    | TYPE IDENTIFIER ASSIGN relexpression
    ;

assignment_statement:
    IDENTIFIER ASSIGN relexpression
    ;

function_definition_statement:
    FUNCTION IDENTIFIER LPAREN function_parameters RPAREN ARROW function_return_type function_body
    ;

function_parameters:
    /* empty */
    | function_parameter_list
    ;

function_parameter_list:
    parameter
    | function_parameter_list COMMA parameter
    ;

parameter:
    TYPE IDENTIFIER
    ;

function_return_type:
    TYPE
    | VOID
    ;

function_body:
    block
    ;

function_call_statement:
    IDENTIFIER LPAREN function_arguments RPAREN
    ;

function_arguments:
    /* empty */
    | function_argument_list
    ;

function_argument_list:
    relexpression
    | function_argument_list COMMA relexpression
    ;

print_statement:
    PRINT LPAREN relexpression RPAREN
    ;

while_statement:
    WHILE LPAREN relexpression RPAREN block
    ;

if_statement:
    IF LPAREN relexpression RPAREN block
    | IF LPAREN relexpression RPAREN block ELSE block
    ;

return_statement:
    RETURN relexpression
    | RETURN 
    ;

relexpression: 
    expression LESS_THAN expression
    | expression LESS_EQUAL expression
    | expression EQUAL expression
    | expression NOT_EQUAL expression
    | expression GREATER_EQUAL expression
    | expression GREATER_THAN expression
    | expression
    ;

expression:
    term PLUS term
    | term MINUS term
    | term OR term
    | term 
    ;

term:
    exponent MULT exponent
    | exponent DIV exponent
    | exponent REMAINDER exponent
    | exponent AND exponent
    | exponent
    ;

exponent:
    factor POW factor
    | factor
    ;

factor:
    INT_LITERAL
    | DOUBLE_LITERAL
    | BOOL_LITERAL
    | STRING_LITERAL
    | IDENTIFIER
    | NOT factor
    | PLUS factor
    | MINUS factor
    | LPAREN relexpression RPAREN
    | ask
    | function_call_statement
    ;

ask:
    ASK LESS_THAN TYPE GREATER_THAN LPAREN RPAREN
    | ASK LESS_THAN TYPE GREATER_THAN LPAREN STRING_LITERAL RPAREN
%%

int main() {
    yyparse();
    return 0;
}
