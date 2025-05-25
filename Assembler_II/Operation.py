from Assembler_II.Theorem import Theorem

class Operation(Theorem):
    def __init__(self, name, content):
        super().__init__(name, content, True)
        print(f"Created new operation '{name}': {content}")
