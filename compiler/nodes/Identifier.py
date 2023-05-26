from Node import Node

class Identifier(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table):
    return symbol_table.get(self.value)