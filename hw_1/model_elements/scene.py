class Scene:
    @classmethod
    def create(cls, poligonal_model, camera, flash=None):
        if poligonal_model is not None and camera is not None:
            return Scene(poligonal_model, camera, flash)
        else:
            raise 'ValueError'

    def __init__(self, poligonal_model, camera, flash=None):
        self.id = 'генерация id'
        self.models = [poligonal_model]
        self.cameras = [camera]
        self.flashes = [flash]

    def metod_1(self, type_):
        return type_

    def metod_2(self, type_1, type_2):
        type_ = None
        return type_
