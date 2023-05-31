from Node import Node
from SymbolTable import SymbolTable

class FuncCall(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    func = func_table.get(self.value)

    if (len(func.children) - 2) != len(self.children):
      raise Exception("Number of arguments don't match.")
    
    symb = SymbolTable()

    if len(func.children) > 2:
      for arg in func.children:
        symb.create(arg.children[0].value, [arg.value, arg.children[1].Evaluate(symb, func_table)[1]])

    if len(func.children) > 2:
      for i in range(len(self.children)):
        arg = self.children[i]
        var_dec = func.children[i+1]

        if arg.Evaluate(symbol_table)[0] != var_dec.children[0].Evaluate(symb, func_table)[0]:
          raise Exception("Type mismatch.")
        else:
          symb.set(var_dec.children[0].value, arg.Evaluate(symbol_table, func_table))

    func_return = func.children[len(func.children)-1].Evaluate(symb, func_table)
    if (func_return[0] != func.value):
      raise Exception("Type mismatch.")
    
    return [func_return[0], func_return[1]]