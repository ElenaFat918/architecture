from hw_1.models.data import *
from hw_1.models.flash import Flash
from hw_1.models.poligonal_model import PoligonalModel
from hw_1.models.scene import Scene
from hw_1.service.i_model_changer import IModelChanger


class ModelStore:
    def __init__(self, intermediate_imco):
        self.models = [PoligonalModel()]
        self.scenes = [Scene(poligonal_model, camera, flash)]
        self.flashes = Flash(point_3d, angel_3d, color, power)
        self.cameras = Camera(point_3d, angel_3d)
        self.__change_observers = [intermediate_imco]

    def get_scena(self, num):
        return self.scenes[num]

    def notify_change(self):
        class IModelChangerSender(IModelChanger):
            def notify_change(self):
                pass
        return IModelChangerSender()
