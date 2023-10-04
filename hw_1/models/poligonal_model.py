from hw_1.models.poligon import Poligon


class PoligonalModel:
    def __init__(self, texture=None):
        self.poligons = [Poligon()]
        self.textures = [texture]
