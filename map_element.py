class Floor():
    def __init__(self):
        self.type = "floor"
        self.character = "_"
        self.placeable = True

class Wall():
    def __init__(self):
        self.type = "wall"
        self.character = "#"
        self.placeable = False

