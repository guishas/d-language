from Node import Node

class BinOp(Node):
  
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def Evaluate(self, symbol_table, func_table):
    x_type, x = self.children[0].Evaluate(symbol_table, func_table)
    y_type, y = self.children[1].Evaluate(symbol_table, func_table)

    if self.value == "+":
      if x_type == "bool" or y_type == "bool":
        raise Exception(f"Unexpected type with \"+\" operator.")
      else:
        if x_type == "string" or y_type == "string":
          if x_type == "string":
            return ["string", x + str(y)]
          else:
            return ["string", str(x) + y]
        else:
          if x_type == "double" or y_type == "double":
            return ["double", float(x) + float(y)]
          else:
            return ["int", x+y]
    elif self.value == "-":
      if x_type not in ["int", "double"] or y_type not in ["int", "double"]:
        raise Exception(f"Expected \"int\" or \"double\" with \"-\" operator.")
      else:
        if x_type == "double" or y_type == "double":
          return ["double", float(x) - float(y)]
        else:
          return ["int", x-y]
    elif self.value == "*":
      if x_type not in ["int", "double"] or y_type not in ["int", "double"]:
        raise Exception(f"Expected \"int\" or \"double\" with \"*\" operator.")
      else:
        if x_type == "double" or y_type == "double":
          return ["double", float(x) * float(y)]
        else:
          return ["int", x * y]
    elif self.value == "/":
      if x_type not in ["int", "double"] or y_type not in ["int", "double"]:
        raise Exception(f"Expected \"int\" or \"double\" with \"/\" operator.")
      else:
        if x_type == "double" or y_type == "double":
          return ["double", float(x) / float(y)]
        else:
          if (x/y)%2 != 0:
            return ["double", x / y]
          else:
            return ["int", x / y]
    elif self.value == "^":
      if x_type not in ["int", "double"] or y_type not in ["int", "double"]:
        raise Exception(f"Expected \"int\" or \"double\" with \"^\" operator.")
      else:
        if x_type == "double" or y_type == "double":
          return ["double", float(x) ** float(y)]
        else:
          return ["int", x ** y]
    elif self.value == "%":
      if x_type not in ["int", "double"] or y_type not in ["int", "double"]:
        raise Exception(f"Expected \"int\" or \"double\" with \"^\" operator.")
      else:
        if x_type == "double" or y_type == "double":
          return ["double", float(x) % float(y)]
        else:
          return ["int", x % y]
    elif self.value == "AND":
      if (not x_type == "bool") or (not y_type == "bool"):
        raise Exception(f"Expected only \"bool\" type with \"and\" operator.")
      else:
        return ["bool", x and y]
    elif self.value == "OR":
      if (not x_type == "bool") or (not y_type == "bool"):
        raise Exception(f"Expected only \"bool\" type with \"or\" operator.")
      else:
        return ["bool", x or y]
    elif self.value == ">":
      if x_type not in ["int", "double"] or y_type not in ["int", "double"]:
        raise Exception(f"Expected \"int\" or \"double\" with \">\" operator.")
      else:
        return ["bool", x > y]
    elif self.value == ">=":
      if x_type not in ["int", "double"] or y_type not in ["int", "double"]:
        raise Exception(f"Expected \"int\" or \"double\" with \">=\" operator.")
      else:
        return ["bool", x >= y]
    elif self.value == "<":
      if x_type not in ["int", "double"] or y_type not in ["int", "double"]:
        raise Exception(f"Expected \"int\" or \"double\" with \"<\" operator.")
      else:
        return ["bool", x < y]
    elif self.value == "<=":
      if x_type not in ["int", "double"] or y_type not in ["int", "double"]:
        raise Exception(f"Expected \"int\" or \"double\" with \"<=\" operator.")
      else:
        return ["bool", x <= y]
    elif self.value == "==":
      if x_type not in ["int", "double", "bool"] or y_type not in ["int", "double", "bool"]:
        raise Exception(f"Expected \"int\", \"double\" or \"bool\" with \"==\" operator.")
      else:
        return ["bool", x == y]
    elif self.value == "!=":
      if x_type not in ["int", "double", "bool"] or y_type not in ["int", "double", "bool"]:
        raise Exception(f"Expected \"int\", \"double\" or \"bool\" with \"!=\" operator.")
      else:
        return ["bool", x != y]