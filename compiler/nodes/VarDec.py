from Node import Node

class VarDec(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    symbol_table.create(self.children[0].value, [self.value, self.children[1].Evaluate(symbol_table, func_table)[1]])