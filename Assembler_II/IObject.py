class IObject:
    def __init__(self, name, content : dict):
        self.name = name
        self.type = content.get("type", "")
        self.description = content.get("description", "")
        self.content = content

