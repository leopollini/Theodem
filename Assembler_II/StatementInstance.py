

class StatementInstance:
    ids = 0
    def __init__(self, statement_ref, args : dict):
        self.statement_ref = statement_ref
        self.args = self.__init_args(args)
        self.name = self.statement_ref.name
        self.statement_id = StatementInstance.ids
        StatementInstance.ids = StatementInstance.ids + 1
        print(f"Instantiated a new '{self.name}': {args}; id: {self.statement_id}")

    def __init_args(self, args : dict) -> dict:
        from Assembler_II.Theodem import Theodem
        res = {}
        if args.keys() != self.statement_ref.variables.keys():
            raise TypeError(f"Invalid args while instancing a '{self.statement_ref.name}'; args: {args.keys()}, vars: {self.statement_ref.variables}")
        for name, val in args.items() :
            if isinstance(val, dict) :
                res[name] = Theodem.elaborate_rooted(val)
            else:
                res[name] = val
        return res
