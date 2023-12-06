from Token import Token

class Tokenizer():
  
  def __init__(self, source_code):
    self.source_code = source_code
    self.position = 0
    self.types = ["int", "double", "string", "bool", "void"]
    self.reserved = ["print", "func", "return", "if", "else", "while", "ask", "True", "False"]
    self.next = None

  def spyNext(self):
    position = self.position
    next_token = self.next
    try:
      self.selectNext()
      return self.next
    finally:
      self.position = position
      self.next = next_token 

  def selectNext(self):
    if self.position == len(self.source_code):
      self.next = Token("EOF", "EOF")
      return
    
    while self.source_code[self.position] == ' ':
      self.position += 1

      if self.source_code[self.position] != ' ':
        last_token = self.next
        if last_token.type == "TT_INT" and self.source_code[self.position].isdigit():
          raise Exception("Whitespace between digits.")
        
    if self.source_code[self.position].isdigit():
      self.makeNumber()
    elif self.source_code[self.position] == '+':
      self.next = Token("TT_PLUS", "+")
      self.position += 1
    elif self.source_code[self.position] == '-':
      if self.source_code[self.position+1] == '>':
        self.next = Token("TT_RET_TYPE", "->")
        self.position += 2
      else:
        self.next = Token("TT_MINUS", "-")
        self.position += 1
    elif self.source_code[self.position] == '*':
      self.next = Token("TT_MULT", "*")
      self.position += 1
    elif self.source_code[self.position] == '^':
      self.next = Token("TT_RAISE", "^")
      self.position += 1
    elif self.source_code[self.position] == '/':
      self.next = Token("TT_DIV", "/")
      self.position += 1
    elif self.source_code[self.position] == '%':
      self.next = Token("TT_REMAINDER", "%")
      self.position += 1
    elif self.source_code[self.position] == ',':
      self.next = Token("TT_COMMA", ",")
      self.position += 1
    elif self.source_code[self.position] == ';':
      self.next = Token("TT_SEMICOLON", ";")
      self.position += 1
    elif self.source_code[self.position] == '(':
      self.next = Token("TT_LPAR", "(")
      self.position += 1
    elif self.source_code[self.position] == ')':
      self.next = Token("TT_RPAR", ")")
      self.position += 1
    elif self.source_code[self.position] == '{':
      self.next = Token("TT_LBRACKET", "{")
      self.position += 1
    elif self.source_code[self.position] == '}':
      self.next = Token("TT_RBRACKET", "}")
      self.position += 1
    elif self.source_code[self.position] == '=':
      if self.source_code[self.position+1] == '=':
        self.next = Token("TT_EQUAL", "==")
        self.position += 2
      else:
        self.next = Token("TT_ASSIGN", "=")
        self.position += 1
    elif self.source_code[self.position] == '!':
      if self.source_code[self.position+1] == '=':
        self.next = Token("TT_DIFF", "!=")
        self.position += 2
      else:
        self.next = Token("TT_NOT", "!")
        self.position += 1
    elif self.source_code[self.position] == '>':
      if self.source_code[self.position+1] == '=':
        self.next = Token("TT_GREATER_EQUAL", ">=")
        self.position += 2
      else:
        self.next = Token("TT_GREATER", ">")
        self.position += 1
    elif self.source_code[self.position] == '<':
      if self.source_code[self.position+1] == '=':
        self.next = Token("TT_LESS_EQUAL", "<=")
        self.position += 2
      else:
        self.next = Token("TT_LESS", "<")
        self.position += 1
    elif self.source_code[self.position] == '"':
      self.makeString()
    elif self.source_code[self.position].isalpha():
      self.makeVariable()
    else:
      raise Exception(f"Invalid character: {self.source_code[self.position]}")
    
  def makeNumber(self):
    num = ""
    dot_count = 0

    while self.position < len(self.source_code) and (self.source_code[self.position].isdigit() or self.source_code[self.position] == '.'):
      if self.source_code[self.position] == '.':
        dot_count += 1
        if dot_count > 1:
          raise Exception("A double should have only one \".\".")
        
      num += self.source_code[self.position]
      self.position += 1

    if dot_count == 1:
      self.next = Token("TT_DOUBLE", num)
    else:
      self.next = Token("TT_INT", num)
  
  def makeString(self):
    string = ""
    self.position += 1

    while self.position < len(self.source_code) and self.source_code[self.position] != '"':
      string += self.source_code[self.position]
      self.position += 1
    
    self.next = Token("TT_STRING", string)
    self.position += 1

  def makeVariable(self):
    var = ""

    while self.position < len(self.source_code) and (self.source_code[self.position].isalnum() or self.source_code[self.position] == '_'):
      var += self.source_code[self.position]
      self.position += 1

    if (var in self.reserved) or (var in self.types):
      if var in self.types:
        self.next = Token("TT_TYPE", var)
      else:
        if var in ["True", "False"]:
          if var == "True":
            self.next = Token("TT_BOOL", var)
          else:
            self.next = Token("TT_BOOL", "")
        else:
          self.next = Token("TT_" + var.upper(), var)
    else:
      self.next = Token("TT_IDENTIFIER", var)
