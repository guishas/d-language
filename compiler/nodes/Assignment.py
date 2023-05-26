from Node import Node

class Assignment(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table):
    symbol_table.set(self.children[0].value, self.children[1].Evaluate(symbol_table))