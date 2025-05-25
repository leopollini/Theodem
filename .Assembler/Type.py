from Assembler.macros import DEBUG_MODE
from Assembler.utils import Initializer

# the actual type that will be considered in the proof process
class TypeInstance:
	def __init__(self,vals,args,name):
		self.name = name
		self.args = {}
		for a in args:
			self.args[a] = vals[a]
			if DEBUG_MODE:
				print(f"assigned {vals[a]} to {a}")

	# overload comparison. Type comparison will only check for matching variable names
	def __eq__(self, other):
		return self.args == other.args

	# in case attribute is not found
	def __getattr__(self, item):
		return None

	def __str__(self):
		return self.name

# type info container interface
class Type(Initializer):
	def __init__(self, content, name):
		Initializer.initialize(self, content, name)

	def getInstance(self, args):
		return TypeInstance(args, self.args, self.name)

# types loader interface (STATIC). Will create a TypeInstance instance with requested name and args
class DeclaredTypes:
	types = {}

	@staticmethod
	def init(content):
		for name, s in content.items():
			DeclaredTypes.types[name] = Type(s, name)
			print(f"new type {name}")

	@staticmethod
	def getInstance(name, args):
		print(f"looking for type {name} to instance...")
		return DeclaredTypes.types.get(name).getInstance(args)

def get_type_instance(name, args):
	return DeclaredTypes.getInstance(name, args)
