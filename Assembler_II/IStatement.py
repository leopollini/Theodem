from Assembler_II.IObject import IObject
from Assembler_II.Variable import Variable


class IStatement(IObject):
    def __init__(self, name, content):
        super().__init__(name, content)
        self.variables = content.get("variables", {})
        self.equivalent = content.get("equivalent", [])

