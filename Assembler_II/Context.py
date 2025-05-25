from Assembler_II.StatementInstance import StatementInstance
from Assembler_II.Variable import Variable


# container class for context variables and  statements
# duplicate names are NOT allowed even in different contexts
class Context:
    def __init__(self):
        self.variables = []
        self.statements = []

    # accepts only StatementInstance's and Variable's
    def append(self, items : list):
        for i in items:
            if i.__class__ == StatementInstance:
                self.statements.append(i)
            else:
                raise TypeError("Not a StatementInstance or a Variable")