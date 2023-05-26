from Node import Node

class BoolVal(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table):
    return ["bool", self.value]