class IObject:
    ids = 0
    def __init__(self, name, content : dict, is_instance : bool = False):
        self.name = name
        self.type = content.get("type", "")
        self.description = content.get("description", "")
        self.content = content
        if not is_instance:
            self.id =IObject.ids
            IObject.ids = IObject.ids + 1

