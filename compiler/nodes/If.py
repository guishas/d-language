from Node import Node

class If(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    if self.children[0].Evaluate(symbol_table, func_table)[1] == True:
      self.children[1].Evaluate(symbol_table, func_table)
    elif len(self.children) == 3:
      self.children[2].Evaluate(symbol_table, func_table)