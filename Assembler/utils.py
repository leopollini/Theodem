class Initializer:
	def initialize(self, content, name = ""):
		self.name = name
		self.args = content.get("args", {})
		self.description = content.get("description", "")
		self.kind = content.get("kind", "")
		self.equiv = content.get("equiv", [])
		self.content = content