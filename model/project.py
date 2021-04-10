class Project:
    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return "%s: %s, %s" % (self.id, self.name, self.description)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __lt__(self, other):
        return int(self.id) < int(other.id)
