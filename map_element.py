class Tile:
    def __init__(self):
        self.actor = None
        self.item = None


class Floor(Tile):
    def __init__(self):
        super().__init__()
        self.type = "floor"
        self.character = " "
        self.placeable = True


class Wall(Tile):
    def __init__(self):
        super().__init__()
        self.type = "wall"
        self.character = "#"
        self.placeable = False
