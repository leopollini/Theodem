from Assembler_II.IObject import IObject

class Variable(IObject):
    def __init__(self, name : str, kind : str):
        super().__init__(name, {"type": f"variable ({kind})"})
        self.statement_refs = []
        print(f"New variable instantiated: {name}, a {kind}")