from Assembler_II.IStatement import IStatement
from Assembler_II.Variable import Variable

class Theorem(IStatement):
    def __init__(self, name, content, silent = False):
        super().__init__(name, content)
        self.proof = content.get("proof", {})
        self.returns = content.get("returns", [])
        self.hypothesis = content.get("suppose", [])
        if not silent:
            print(f"Created new theorem '{name}': {content}")

    def vars_init(self):
        res = {}
        for varname, kind in self.variables.items():
            res[varname] = Variable(varname, kind)

    def statements_init(self):
        from Assembler_II.Theodem import Theodem
        res = []
        for what in self.hypothesis :
            print(what)
            if what.get("statement", False):
                res.append(Theodem.get_statement_instance(what["statement"], what["args"]))
            elif what.get("theorem", False):
                if not Theodem.theorems.get(what["theorem"], False):
                    print(Theodem.theorems[what["theorem"]])
                    raise TypeError(f"Theorem '{what["theorem"]}' not found while proving {self.theorem.name}")
                print(f"Theorem '{what["theorem"]}' required and found")
            else:
                raise TypeError("requiring something else...")

    def operate(self, args):
        from Assembler_II.Theodem import Theodem
        res = []
        for r in self.returns:
            if isinstance(r, str):
                if r not in self.variables:
                    raise TypeError(f"Return variable not found: {r} in a {self.name} operation")
                res.append(r)
            else:
                res.append(Theodem.elaborate_rooted(r))
