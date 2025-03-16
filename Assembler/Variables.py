from Assembler.Property import PropertyInstance
from Assembler.Type import get_type_instance
from Assembler.macros import encode_string, sort_by_name_args_func

def create_var_name(content: [PropertyInstance]):
	stg = ""
	for c in content:
		stg += str(c)
	return '_' + encode_string(stg)[0:33:6]

class Variable:
	def __init__(self, properties: [PropertyInstance], name = '', type = {}):
		self.properties = properties
		self.properties.sort(key=sort_by_name_args_func)
		self.name = name if name != '' else create_var_name(self.properties)
		if type == {}:
			type = {'name':'_set'}
		self.type = get_type_instance(type.get('name'), type.get('args'))

		print(f"created variable {self.name}! Type: {self.type}; Properties:")
		print("[", end = "")
		for p in properties:
			print(p, end='; ')
		print("]")

	def __eq__(self, other):
		return self.properties == other.properties or self.name == other.name
