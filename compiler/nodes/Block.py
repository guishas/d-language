from Node import Node

class Block(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    for node in self.children:
      if node.value == "RETURN":
        return node.Evaluate(symbol_table, func_table)
      else:
        node.Evaluate(symbol_table, func_table)