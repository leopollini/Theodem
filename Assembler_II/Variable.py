from Assembler_II.IObject import IObject

class Variable(IObject):
    ids = 0
    def __init__(self, name : str, kind : str):
        super().__init__(name, {"type": f"variable ({kind})"}, True)
        self.statement_refs = []
        self.var_id = Variable.ids
        Variable.ids = Variable.ids + 1
        print(f"New variable instantiated: {name}, a {kind}; id: {self.var_id}")