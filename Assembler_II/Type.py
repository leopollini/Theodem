from Assembler_II.IStatement import IStatement

class Type(IStatement):
    def __init__(self, name, content):
        super().__init__(name, content)
        print(f"Created new type '{name}': {content}")