from Node import Node

class Print(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    type, content = self.children[0].Evaluate(symbol_table, func_table)
    if type == "void":
      raise Exception("Can't print a \"void\".")
    
    print(content)