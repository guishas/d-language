from Node import Node

class DoubleVal(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    return ["double", self.value]