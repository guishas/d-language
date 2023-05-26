from Node import Node

class IntVal(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table):
    return ["int", self.value]