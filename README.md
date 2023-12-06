# D Language

## Descrição

Linguagem de programação inspirada em Python e Java. 

## Desenvolvedor

Guilherme Lunetta

## EBNF

`LETTER = ( "A" | ... | "Z" | "a" | ... | "z" );`

`DIGIT = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" );`

`SYMBOL = ( "!" | '"' | "#" | "$" | "%" | "&" | "'" | "(" | ")" | "*" | "+" | "," | "-" | "." | "/" | ":" | ";" | "<" | "=" | ">" | "?" | "@" | "[" | "\\" | "]" | "^" | "_" | "{" | "|" | "}" | "~" );`

`CHARACTER = ( LETTER | DIGIT | SYMBOL );`

`BOOL = ( "True" | "False" );`

`INT = DIGIT, {DIGIT};`

`DOUBLE = DIGIT, {DIGIT}, ".", {DIGIT};`

`STRING = '"', {CHARACTER}, '"';`

`TYPE = ( "string" | "int" | "double" | "bool" );`

`IDENTIFIER = LETTER, {LETTER, DIGIT, "_"};`

`IDENTIFIER_DECLARATION = TYPE, IDENTIFIER;`

`ASSIGNMENT = TYPE, IDENTIFIER, "=", RELEXPRESSION | IDENTIFIER, "=", RELEXPRESSION;`

`PRINT = "print", "(", RELEXPRESSION, ")";`

`IF = "if", "(", RELEXPRESSION, ")", BLOCK, [ "else", BLOCK ];`

`WHILE = "while", "(", RELEXPRESSION, ")", BLOCK;`

`FUNCTION_DECLARATION = "func", IDENTIFIER, "(", [ TYPE, IDENTIFIER, {",", TYPE, IDENTIFIER} ], ")", "->", ( TYPE | "void" ), "{", FUNCTION_BODY, "}";`

`FUNCTION_BODY = {STATEMENT}, FUNCTION_RETURN;`

`FUNCTION_RETURN = "return", RELEXPRESSION | "return";`

`FUNCTION_CALL = IDENTIFIER, "(", [ IDENTIFIER, {",", IDENTIFIER} ], ")";`

`RELEXPRESSION = EXPRESSION, { ( "<" | "<=" | "==" | "!=" | ">=" | ">" ), EXPRESSION };`

`EXPRESSION = TERM, { ( "+" | "-" | "or" ), TERM };`

`TERM = FACTOR, { ( "*" | "/" | "%" | "and" ), FACTOR };`

`FACTOR = INT | DOUBLE | BOOL | STRING | IDENTIFIER | ( ( "+" | "-" | "!" ), FACTOR ) | "(", EXPRESSION, ")" | ASK | FUNCTION_CALL;`

`ASK = "ask", "<", ( "int" | "double" | "string" ), ">", "(", {STRING}, ")"`;

`STATEMENT = ( λ | IDENTIFIER_DECLARATION | ASSIGNMENT | FUNCTION_DEFINITION | FUNCTION_CALL | PRINT | WHILE | IF ), ";";`

`BLOCK = "{", {STATEMENT}, "}";`

`PROGRAM = {STATEMENT};`

## Exemplo de programa

```java
int a = 2;
double b = 3.5;
bool isD = True;
string fileExtension = ".d";

print(b);
print(fileExtension);

func isGreater(int a, int b) -> bool {
  return a > b;
}

func showMessage(string message) -> void {
  print(message);
}

while (isD == True) {
  a = a * 2;
  print(a);

  if (a > 1000) {
    isD = False;
  }
}
```
