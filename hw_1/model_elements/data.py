from hw_1.model_elements.camera import Camera
from hw_1.model_elements.flash import Flash
from hw_1.model_elements.poligonal_model import PoligonalModel


class Point3D:
    pass


class Power:
    pass


class Color:
    pass


class Angel3D:
    pass


point_3d = Point3D()
angel_3d = Angel3D()
color = Color()
power = Power()
poligonal_model = PoligonalModel()
camera = Camera(point_3d, angel_3d)
flash = Flash(point_3d, angel_3d, color, power)
