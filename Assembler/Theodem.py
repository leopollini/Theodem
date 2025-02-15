import json

from Assembler.Operation import DeclaredOperations
from Assembler.Property import DeclaredProperties
from Assembler.Statement import DeclaredStatements
from Assembler.Theorem import DeclaredTheorems
from Assembler.Type import DeclaredTypes


class Theodem:
	content = None

	@staticmethod
	def init(open_file = None):
		print("Loading file content...")
		content = json.load(open_file)
		print("content loaded")

		DeclaredStatements.init(content.get("statement"))
		DeclaredProperties.init(content.get("statement"))
		DeclaredOperations.init(content.get("operation"))
		DeclaredTypes.init(content.get("type"))
		DeclaredTheorems.init(content.get("theorem"))
