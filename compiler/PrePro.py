class PrePro():
  
  @staticmethod
  def filter(source_code):
    if '#' not in source_code:
      return "".join(source_code.split('\n'))
    
    lines = source_code.split('\n')
    for i in range(len(lines)):
      for j in range(len(lines[i])):
        if lines[i][j] == '#':
          lines[i] = lines[i][:j]
          break
    
    return "".join(lines)