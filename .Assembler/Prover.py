from Assembler.Property import get_property_instance
from Assembler.Variables import Variable


class Prover:
	theorem = None
	statements = []
	variables = []
	@staticmethod
	def prove(theorem):
		Prover.theorem = theorem
		print(f"### Proving {theorem.name}")
		print(f"Description: {theorem.description}")
		Prover.loadRequirements()

	@staticmethod
	def loadVars():
		tvars = Prover.theorem.hypothesis.get("args", {})
		for name, what in tvars.items():
			props = []
			for prop in what:
				if not prop.get('property') is None:
					props.append(get_property_instance(prop.get('property'), prop.get('args')))
			Prover.variables.append(Variable(props, name))

	def loadStatements():
		return

	@staticmethod
	def loadRequirements():
		print(Prover.theorem.hypothesis)
		stats = Prover.theorem.hypothesis.get("requires")
		print("### Loading vars!")
		Prover.loadVars()
		print("### Vars loaded!")
		print("### Loading statements!")
		Prover.loadStatements()
		print("### Statements loaded!")


