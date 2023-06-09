from Node import Node

class Ask(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symbol_table, func_table):
        type = self.children[0]
        string = self.children[1]
        if string == "":
            try:
                if type == "string":
                    inp = str(input("> "))
                elif type == "int":
                    inp = int(input("> "))
                else:
                    inp = float(input("> "))
            except:
                raise Exception(f"Input given doesn't match with type given.")
        else:
            try:
                if type == "string":
                    inp = str(input(string))
                elif type == "int":
                    inp = int(input(string))
                else:
                    inp = float(input(string))
            except:
                raise Exception(f"Input given doesn't match with type given.")
        return [type, inp]