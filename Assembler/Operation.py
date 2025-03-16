from Assembler.macros import DEBUG_MODE
from Assembler.utils import Initializer

# the actual operation that will be considered in the proof process
class OperationInstance:
	def __init__(self,vals,args,name):
		self.name = name
		self.args = {}
		for a in args:
			self.args[a] = vals[a]
			if DEBUG_MODE:
				print(f"assigned {vals[a]} to {a}")

	# overload comparison. Operation comparison will only check for matching variable names
	def __eq__(self, other):
		return self.args == other.args

	# in case attribute is not found
	def __getattr__(self, item):
		return None

	def __str__(self):
		return self.name

# operation info container interface
class Operation(Initializer):
	def __init__(self, content, name):
		Initializer.initialize(self, content, name)

	def getInstance(self, args):
		return OperationInstance(args, self.args, self.name)

# operations loader interface (STATIC). Will create a OperationInstance instance with requested name and args
class DeclaredOperations:
	operations = {}

	@staticmethod
	def init(content):
		for name, s in content.items():
			DeclaredOperations.operations[name] = Operation(s, name)
			print(f"new operation {name}")

	@staticmethod
	def getInstance(name, args):
		print(f"looking for operation {name} to instance...")
		return DeclaredOperations.operations.get(name).getInstance(args)
