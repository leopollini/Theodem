import json
from Assembler_II.IStatement import IStatement
from Assembler_II.Statement import Statement
from Assembler_II.Theorem import Theorem
from Assembler_II.Operation import Operation
from Assembler_II.Type import Type

class Theodem:
    content = None
    statements = {}
    theorems = {}
    operations = {}
    types = {}

    @staticmethod
    def load_file(file):
        print("Loading file content...")
        Theodem.content = json.load(file)
        print("content loaded")

        Theodem.statements = Theodem.loader(Statement, Theodem.content["statement"])
        Theodem.operations = Theodem.loader(Operation, Theodem.content["operation"])
        Theodem.types = Theodem.loader(Type, Theodem.content["type"])
        Theodem.theorems = Theodem.loader(Theorem, Theodem.content["theorem"])

    @staticmethod
    def loader(objtype, content : dict):
        res = {}
        for name, item_content in content.items():
            res[name] = objtype(name, item_content)
        return res

    @staticmethod
    def get_statement_instance(statement_name, args):
        if statement_name in Theodem.statements:
            return Theodem.statements[statement_name].get_instance(args)
        raise TypeError(f"Statement not found: {statement_name}")

    @staticmethod
    def get_operation_result(operation_name, args):
        if operation_name in Theodem.operations:
            return Theodem.operations[operation_name].operate(args)
        raise TypeError(f"Operation not found: {operation_name}")

    @staticmethod
    def elaborate_rooted(what):
        print("rooted argument creation...")
        if "statement" in what:
            return Theodem.get_statement_instance(what["statement"], what.get("args", {}))
        elif "operation" in what:
            return Theodem.get_operation_result(what["operation"], what.get("args", {}))
        else:
            raise TypeError(f"Unknown object encountered: {what}")
