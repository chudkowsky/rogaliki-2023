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


class Anvil(Tile):
    def __init__(self):
        super().__init__()
        self.type = "anvil"
        self.character = "v"
        self.placeable = False
    def use_anvil(self, item, book):
        item.quality = item.quality.value[1] + 1

class Stairs(Tile):
    def __init__(self):
        super().__init__()
        self.type = "stairs"
        self.character = "x"
        self.placeable = True
