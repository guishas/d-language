from Node import Node

class Return(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table):
    if len(self.children) == 0:
      return ["void", ""]
    
    return self.children[0].Evaluate(symbol_table)