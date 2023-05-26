from Tokenizer import Tokenizer
from nodes.Block import Block
from nodes.BinOp import BinOp
from nodes.IntVal import IntVal
from nodes.DoubleVal import DoubleVal
from nodes.StrVal import StrVal
from nodes.BoolVal import BoolVal
from nodes.UnOp import UnOp
from nodes.Identifier import Identifier
from nodes.NoOp import NoOp
from nodes.Assignment import Assignment
from nodes.VarDec import VarDec
from nodes.Return import Return
from nodes.Print import Print

class Parser():

  def __init__(self, source):
    self.tokenizer = Tokenizer(source)

  def parseBlock(self):
    node = Block("BLOCK", [])
    while not self.tokenizer.next.type == "EOF":
      node.children.append(self.parseStatement())
    
    return node
  
  def parseStatement(self):
    if self.tokenizer.next.type == "TT_SEMICOLON":
      self.tokenizer.selectNext()
      return NoOp("NOOP", [])
    elif self.tokenizer.next.type == "TT_IDENTIFIER":
      value = self.tokenizer.next.value
      self.tokenizer.selectNext()

      if self.tokenizer.next.type == "TT_ASSIGN":
        self.tokenizer.selectNext()
        return Assignment("ASSIGNMENT", [Identifier(value, []), self.parseRelExpression()])
      else:
        raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
    elif self.tokenizer.next.type == "TT_TYPE":
      type = self.tokenizer.next.value
      self.tokenizer.selectNext()
      if self.tokenizer.next.type == "TT_IDENTIFIER":
        value = self.tokenizer.next.value
        self.tokenizer.selectNext()
        if self.tokenizer.next.type == "TT_ASSIGN":
          self.tokenizer.selectNext()
          return VarDec(type, [Identifier(value, []), self.parseRelExpression()])
        elif self.tokenizer.spyNext().type == "TT_SEMICOLON":
          if type == "int":
            return VarDec(type, [Identifier(value, []), IntVal(0, [])])
          elif type == "double":
            return VarDec(type, [Identifier(value, []), DoubleVal(0.0, [])])
          elif type == "string":
            return VarDec(type, [Identifier(value, []), StrVal("", [])])
          else:
            return VarDec(type, [Identifier(value, []), BoolVal(None, [])])
        else:
          raise Exception(f"Unexpected token after identifier: {self.tokenizer.spyNext().type}")
      else:
        raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
    elif self.tokenizer.next.type == "TT_RETURN":
      self.tokenizer.selectNext()
      if self.tokenizer.next.type == "TT_SEMICOLON":
        return Return("RETURN", [])
      else:
        return Return("RETURN", [self.parseExpression()])
    elif self.tokenizer.next.type == "TT_PRINT":
      self.tokenizer.selectNext()
      if self.tokenizer.next.type == "TT_LPAR":
        self.tokenizer.selectNext()
        node = Print("PRINT", [self.parseRelExpression()])

        if self.tokenizer.next.type == "TT_RPAR":
          self.tokenizer.selectNext()
          return node
        else:
          raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
      else:
        raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
    elif self.tokenizer.next.type == "TT_WHILE":
      pass
    elif self.tokenizer.next.type == "TT_IF":
      pass
    elif self.tokenizer.next.type == "TT_FUNC":
      pass
    else:
      raise Exception(f"Unexpected token: {self.tokenizer.next.type}")

  
  def parseRelExpression(self):
    node = self.parseExpression()

    while self.tokenizer.next.type in ["TT_LESS", "TT_GREATER", "TT_LESS_EQUAL", "TT_GREATER_EQUAL", "TT_DIFF", "TT_EQUAL"]:
      if self.tokenizer.next.type == "TT_LESS":
        self.tokenizer.selectNext()
        node = BinOp("<", [node, self.parseExpression()])
      elif self.tokenizer.next.type == "TT_GREATER":
        self.tokenizer.selectNext()
        node = BinOp(">", [node, self.parseExpression()])
      elif self.tokenizer.next.type == "TT_LESS_EQUAL":
        self.tokenizer.selectNext()
        node = BinOp("<=", [node, self.parseExpression()])
      elif self.tokenizer.next.type == "TT_GREATER_EQUAL":
        self.tokenizer.selectNext()
        node = BinOp(">=", [node, self.parseExpression()])
      elif self.tokenizer.next.type == "TT_DIFF":
        self.tokenizer.selectNext()
        node = BinOp("!=", [node, self.parseExpression()])
      else:
        self.tokenizer.selectNext()
        node = BinOp("==", [node, self.parseExpression()])
      
    return node

  def parseExpression(self):
    node = self.parseTerm()

    while self.tokenizer.next.type in ["TT_PLUS", "TT_MINUS", "TT_OR"]:
      if self.tokenizer.next.type == "TT_PLUS":
        self.tokenizer.selectNext()
        node = BinOp("+", [node, self.parseTerm()])
      elif self.tokenizer.next.type == "TT_MINUS":
        self.tokenizer.selectNext()
        node = BinOp("-", [node, self.parseTerm()])
      else:
        self.tokenizer.selectNext()
        node = BinOp("OR", [node, self.parseTerm()])
      
    return node

  def parseTerm(self):
    node = self.parseFactor()

    while self.tokenizer.next.type in ["TT_MULT", "TT_DIV", "TT_AND"]:
      if self.tokenizer.next.type == "TT_MULT":
        self.tokenizer.selectNext()
        node = BinOp("*", [node, self.parseFactor()])
      elif self.tokenizer.next.type == "TT_DIV":
        self.tokenizer.selectNext()
        node = BinOp("/", [node, self.parseFactor()])
      else:
        self.tokenizer.selectNext()
        node = BinOp("AND", [node, self.parseFactor()])

    return node

  def parseFactor(self):
    if self.tokenizer.next.type == "TT_INT":
      value = self.tokenizer.next.value
      self.tokenizer.selectNext()
      return IntVal(int(value), [])
    elif self.tokenizer.next.type == "TT_DOUBLE":
      value = self.tokenizer.next.value
      self.tokenizer.selectNext()
      return DoubleVal(float(value), [])
    elif self.tokenizer.next.type == "TT_STRING":
      value = self.tokenizer.next.value
      self.tokenizer.selectNext()
      return StrVal(str(value), [])
    elif self.tokenizer.next.type == "TT_BOOL":
      value = self.tokenizer.next.value
      self.tokenizer.selectNext()
      return BoolVal(bool(value), [])
    elif self.tokenizer.next.type == "TT_MINUS":
      self.tokenizer.selectNext()
      return UnOp("-", [self.parseFactor()])
    elif self.tokenizer.next.type == "TT_PLUS":
      self.tokenizer.selectNext()
      return UnOp("+", [self.parseFactor()])
    elif self.tokenizer.next.type == "TT_NOT":
      self.tokenizer.selectNext()
      return UnOp("!", [self.parseFactor()])
    elif self.tokenizer.next.type == "TT_LPAR":
      self.tokenizer.selectNext()
      node = self.parseRelExpression()

      if self.tokenizer.next.type == "TT_RPAR":
        self.tokenizer.selectNext()
        return node
      else:
        raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
    elif self.tokenizer.next.type == "TT_IDENTIFIER":
      value = self.tokenizer.next.value
      self.tokenizer.selectNext()

      if self.tokenizer.next.type == "TT_LPAR":
        pass
      else:
        return Identifier(value, [])
  
  def run(self, symbol_table):
    self.tokenizer.selectNext()
    result = self.parseBlock()
    if self.tokenizer.next.type != "EOF":
      raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
    
    return result.Evaluate(symbol_table)
