class MapElement:
    def __init__(self,type,character):
        self.type = type
        self.character = character

class Floor(MapElement):
    def __init__(self, type, character):
        super().__init__(type, character)
        self.placeable = True

class Wall(MapElement):
    def __init__(self, type, character):
        super().__init__(type, character)
        self.placeable = False

