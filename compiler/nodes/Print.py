from Node import Node

class Print(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table):
    print(self.children[0].Evaluate(symbol_table)[1])