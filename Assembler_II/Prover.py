from Assembler_II.StatementInstance import StatementInstance
from Assembler_II.Theodem import Theodem
from Assembler_II.Variable import Variable

class Checker:
    @staticmethod
    def verify(theorem_name : str, statements : [StatementInstance], args : dict):
        required = Theodem.theorems[theorem_name].hypothesis
        required_instanced = []
        for r in required:
            required_instanced.append(r.get_instance(args))


class Prover:
    def __init__(self, theorem_to_prove : str):
        self.theorem = Theodem.theorems[theorem_to_prove]
        self.proof = self.theorem.proof
        self.variables = self.theorem.vars_init()
        print("loaded variables!")
        self.statements = self.theorem.statements_init()
        print("loaded hypothesis!")

