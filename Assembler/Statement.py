from Assembler.macros import DEBUG_MODE
from Assembler.utils import Initializer

# the actual statement that will be considered in the proof process
class StatementInstance:
	def __init__(self,vals,args,name):
		self.name = name
		self.args = {}
		for a in args:
			self.args[a] = vals[a]
			if DEBUG_MODE:
				print(f"assigned {vals[a]} to {a}")

	# overload comparison. Statement comparison will only check for matching variable names
	def __eq__(self, other):
		return self.args == other.args

	# in case attribute is not found
	def __getattr__(self, item):
		return None

# statement info container interface
class Statement(Initializer):
	def __init__(self, content, name):
		Initializer.initialize(self, content, name)

	def getInstance(self, args):
		return StatementInstance(args, self.args, self.name)

# statements loader interface (STATIC). Will create a StatementInstance instance with requested name and args
class DeclaredStatements:
	statements = {}

	@staticmethod
	def init(content):
		for name, s in content.items():
			DeclaredStatements.statements[name] = Statement(s, name)
			print(f"new statement {name}")

	@staticmethod
	def getInstance(name, args):
		print(f"looking for statement {name} to instance...")
		return DeclaredStatements.statements.get(name).getInstance(args)
