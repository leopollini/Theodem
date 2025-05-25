from Assembler_II.IStatement import IStatement
from Assembler_II.StatementInstance import StatementInstance

class Statement(IStatement):
    def __init__(self, name, content : dict):
        super().__init__(name, content)
        print(f"Created new statement '{name}': {content}")

    def get_instance(self, args : dict):
        return StatementInstance(self, args)
