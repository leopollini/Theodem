from Assembler.macros import DEBUG_MODE
from Assembler.utils import Initializer

class Theorem(Initializer):
	def __init__(self, content, name):
		Initializer.initialize(self, content, name)


# properties loader interface (STATIC). Sorts Theorems given the name and verifies theorem availability
class DeclaredTheorems:
	properties = {}

	@staticmethod
	def init(content):
		for name, s in content.items():
			DeclaredTheorems.properties[name] = Theorem(s, name)
			print(f"new theorem {name}")