class SymbolTable():
    
  def __init__(self):
    self.table = {}

  def create(self, key, value):
    if self.table.get(key) != None:
      raise Exception(f"A variable with the name {key} already exists.")
    else:
      if value[0] == "double" and str(value[1]).count(".") == 0:
        raise Exception("Expected a \".\" when trying to declare a double variable. Example: double d = 1.0;.")
      
      self.table[key] = value

  def get(self, key):
    if self.table.get(key) != None:
      return self.table[key]
    else:
      raise Exception(f"A variable with the name {key} doesn't exists.")
    
  def set(self, key, value):
    if self.table.get(key) != None:
      if value[0] == "double" and str(value[1]).count(".") == 0:
        raise Exception("Expected a \".\" when trying to declare a double variable. Example: double d = 1.0;.")
      
      if self.table[key][0] == value[0]:
        self.table[key] = value
      else:
        raise Exception(f"The type \"{self.table[key][0]}\" doesn't match with type \"{value[0]}\"")
    else:
      raise Exception(f"A variable with the name {key} doesn't exists.")