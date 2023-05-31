from Node import Node

class UnOp(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    result = self.children[0].Evaluate(symbol_table, func_table)
    if self.value == "-":
      return [result[0], -result[1]]
    elif self.value == "!":
      return [result[0], not result[1]]
    else:
      return [result[0], result[1]]