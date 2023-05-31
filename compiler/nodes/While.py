from Node import Node

class While(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    while self.children[0].Evaluate(symbol_table, func_table)[1] == True:
      self.children[1].Evaluate(symbol_table, func_table)