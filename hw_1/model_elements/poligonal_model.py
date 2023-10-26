from hw_1.model_elements.poligon import Poligon


class PoligonalModel:
    def __init__(self, texture=None):
        self.poligons = [Poligon()]
        self.textures = [texture]
