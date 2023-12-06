from Node import Node

class VarDec(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    eval = self.children[1].Evaluate(symbol_table, func_table)
    if self.value != eval[0]:
      raise Exception("Type mismatch.")
    
    symbol_table.create(self.children[0].value, [self.value, eval[1]])