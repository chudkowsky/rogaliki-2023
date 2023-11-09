class MapElement:
    def __init__(self,type,character):
        self.type = type
        self.character = character

class Floor(MapElement):
    def __init__(self, type, character):
        super().__init__(type, character)

class Wall(MapElement):
    def __init__(self, type, character):
        super().__init__(type, character)

