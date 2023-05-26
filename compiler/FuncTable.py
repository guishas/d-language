class FuncTable():
    
  def __init__(self):
    self.table = {}

  def create(self, key, reference):
    if self.table.get(key) != None:
      raise Exception(f"A function with the name {key} already exists.")
    else:
      self.table[key] = reference

  def get(self, key):
    if self.table.get(key) != None:
      return self.table[key]
    else:
      raise Exception(f"A function with the name {key} doesn't exists.")