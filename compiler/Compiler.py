import sys
from PrePro import PrePro
from Parser import Parser
from SymbolTable import SymbolTable
from FuncTable import FuncTable

def main():
  filename = sys.argv[1]
  
  with open(filename, "r") as f:
    code = f.read()

  source = PrePro.filter(code)
  parser = Parser(source)
  symbol_table = SymbolTable()
  func_table = FuncTable()
  parser.run(symbol_table, func_table)

if __name__ == "__main__":
  main()