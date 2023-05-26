from Node import Node

class FuncDec(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    func_table.create(self.children[0].value, self)