from Assembler.macros import DEBUG_MODE
from Assembler.utils import Initializer

# the actual property that will be considered in the proof process
class PropertyInstance:
	def __init__(self,vals,args,name):
		self.name = name
		self.args = {}
		for a in args:
			self.args[a] = vals[a]
			if DEBUG_MODE:
				print(f"assigned {vals[a]} to {a}")

	# overload comparison. Property comparison will only check for matching variable names
	def __eq__(self, other):
		return self.args == other.args

	# in case attribute is not found
	def __getattr__(self, item):
		return None

# property info container interface
class Property(Initializer):
	def __init__(self, content, name):
		Initializer.initialize(self, content, name)

	def getInstance(self, args):
		return PropertyInstance(args, self.args, self.name)

# properties loader interface (STATIC). Will create a PropertyInstance instance with requested name and args
class DeclaredProperties:
	properties = {}

	@staticmethod
	def init(content):
		for name, s in content.items():
			DeclaredProperties.properties[name] = Property(s, name)
			print(f"new property {name}")

	@staticmethod
	def getInstance(name, args):
		print(f"looking for property {name} to instance...")
		return DeclaredProperties.properties.get(name).getInstance(args)
