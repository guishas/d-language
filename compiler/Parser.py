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
from nodes.FuncCall import FuncCall
from nodes.FuncDec import FuncDec
from nodes.If import If
from nodes.While import While

class Parser():

  def __init__(self, source):
    self.tokenizer = Tokenizer(source)

  def parseBlock(self):
    node = Block("BLOCK", [])
    while not self.tokenizer.next.type == "EOF":
      node.children.append(self.parseStatement())
    
    return node
  
  def parseStatement(self):
    if self.tokenizer.next.type == "TT_IDENTIFIER":
      value = self.tokenizer.next.value
      self.tokenizer.selectNext()

      if self.tokenizer.next.type == "TT_ASSIGN":
        self.tokenizer.selectNext()
        node = Assignment("ASSIGNMENT", [Identifier(value, []), self.parseRelExpression()])
        if self.tokenizer.next.type == "TT_SEMICOLON":
          self.tokenizer.selectNext()
          return node
        else:
          raise Exception(f"Expected ; to end a line.")
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
          node = VarDec(type, [Identifier(value, []), self.parseRelExpression()])
          if self.tokenizer.next.type == "TT_SEMICOLON":
            self.tokenizer.selectNext()
            return node
          else:
            raise Exception(f"Expected ; to end a line.")
        elif self.tokenizer.next.type == "TT_SEMICOLON":
          self.tokenizer.selectNext()
          if type == "int":
            return VarDec(type, [Identifier(value, []), IntVal(0, [])])
          elif type == "double":
            return VarDec(type, [Identifier(value, []), DoubleVal(0.0, [])])
          elif type == "string":
            return VarDec(type, [Identifier(value, []), StrVal("", [])])
          else:
            return VarDec(type, [Identifier(value, []), BoolVal(None, [])])
        else:
          raise Exception(f"Unexpected token after identifier: {self.tokenizer.next.type}")
      else:
        raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
    elif self.tokenizer.next.type == "TT_RETURN":
      self.tokenizer.selectNext()
      if self.tokenizer.next.type == "TT_SEMICOLON":
        self.tokenizer.selectNext()
        return Return("RETURN", [])
      else:
        node = Return("RETURN", [self.parseExpression()])
        if self.tokenizer.next.type == "TT_SEMICOLON":
          self.tokenizer.selectNext()
          return node
        else:
          raise Exception(f"Expected ; to end a line.")
    elif self.tokenizer.next.type == "TT_PRINT":
      self.tokenizer.selectNext()
      if self.tokenizer.next.type == "TT_LPAR":
        self.tokenizer.selectNext()
        node = Print("PRINT", [self.parseRelExpression()])

        if self.tokenizer.next.type == "TT_RPAR":
          self.tokenizer.selectNext()
          if self.tokenizer.next.type == "TT_SEMICOLON":
            self.tokenizer.selectNext()
            return node
          else:
            raise Exception(f"Expected ; to end a line.")
        else:
          raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
      else:
        raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
    elif self.tokenizer.next.type == "TT_WHILE":
      self.tokenizer.selectNext()
      if self.tokenizer.next.type == "TT_LPAR":
        self.tokenizer.selectNext()
        condition = self.parseRelExpression()

        if self.tokenizer.next.type == "TT_RPAR":
          self.tokenizer.selectNext()
          if self.tokenizer.next.type == "TT_LBRACKET":
            self.tokenizer.selectNext()
            children = []
            while not self.tokenizer.next.type == "TT_RBRACKET":
              children.append(self.parseStatement())

            while_block = Block("BLOCK", children)

            if self.tokenizer.next.type == "TT_RBRACKET":
              self.tokenizer.selectNext()
              return While("WHILE", [condition, while_block])
            else:
              raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
          else:
            raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
        else:
          raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
      else:
        raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
    elif self.tokenizer.next.type == "TT_IF":
      self.tokenizer.selectNext()
      if self.tokenizer.next.type == "TT_LPAR":
        self.tokenizer.selectNext()
        condition = self.parseRelExpression()

        if self.tokenizer.next.type == "TT_RPAR":
          self.tokenizer.selectNext()
          if self.tokenizer.next.type == "TT_LBRACKET":
            self.tokenizer.selectNext()
            children = []
            while not self.tokenizer.next.type == "TT_RBRACKET":
              children.append(self.parseStatement())

            if_block = Block("BLOCK", children)

            if self.tokenizer.next.type == "TT_RBRACKET":
              self.tokenizer.selectNext()
              if self.tokenizer.next.type == "TT_ELSE":
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == "TT_LBRACKET":
                  self.tokenizer.selectNext()
                  else_children = []
                  while not self.tokenizer.next.type == "TT_RBRACKET":
                    else_children.append(self.parseStatement())

                  else_block = Block("BLOCK", else_children)

                  if self.tokenizer.next.type == "TT_RBRACKET":
                    self.tokenizer.selectNext()
                    return If("IF", [condition, if_block, else_block])
                  else:
                    raise Exception(f"Unexpected token: {self.tokenizer.next.type}.")
                else:
                  raise Exception(f"Unexpected token: {self.tokenizer.next.type}.")
              else:
                return If("IF", [condition, if_block])
            else:
              raise Exception(f"Unexpected token: {self.tokenizer.next.type}.")
          else:
            raise Exception(f"Unexpected token: {self.tokenizer.next.type}.")
        else:
          raise Exception(f"Unexpected token: {self.tokenizer.next.type}.")
      else:
        raise Exception(f"Unexpected token: {self.tokenizer.next.type}.")
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
        self.tokenizer.selectNext()
        args = []
        if self.tokenizer.next.type == "TT_RPAR":
          self.tokenizer.selectNext()
          return FuncCall(value, [])
        else:
          args.append(self.parseRelExpression())

          while self.tokenizer.next.type == "TT_COMMA":
            self.tokenizer.selectNext()
            args.append(self.parseRelExpression())

          if self.tokenizer.next.type == "TT_RPAR":
            self.tokenizer.selectNext()
            return FuncCall(value, args)
          else:
            raise Exception(f"Unexpected token: {self.tokenizer.next.type}.")
      else:
        return Identifier(value, [])
    else:
      raise Exception(f"Unexpected token: {self.tokenizer.next.type}.")
  
  def run(self, symbol_table, func_table):
    self.tokenizer.selectNext()
    result = self.parseBlock()
    if self.tokenizer.next.type != "EOF":
      raise Exception(f"Unexpected token: {self.tokenizer.next.type}")
    
    return result.Evaluate(symbol_table, func_table)
