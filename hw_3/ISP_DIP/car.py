# В данной работе реализованы оба приципа (ISP, DIP)
# DIP: класс Car принимает сущности от абстрактных классов
# ISP: интерфейсы разделены на "подзадачи" и нереализованы в одном интерфейсе

from drive import SportDrive
from engine import PetrolEngine


class Car:
    def __init__(self, engine, drive):
        self.__engine = engine
        self.__drive = drive

    def start_car(self):
        self.__engine.start()

    def drive_car(self):
        self.__drive.speed()
        self.__drive.stopped()


if __name__ == '__main__':
    eng = PetrolEngine()
    drv = SportDrive()
    tesla = Car(eng, drv)
    tesla.start_car()
    tesla.drive_car()

"""
 ISP: Interface Segregation Principle. Принцип разделения интерфейсов.

Cлишком большие интерфейсы требуется разделять на более маленькие, чтобы программные
сущности маленьких интерфейсов знали только о методах, которые требуются им в работе.

DIP: Dependency Inversion Principle. Принцип инверсии зависимости.

зависимости в исходном коде направлены на абстракции, а не на конкретные реализации.
высокоуровневые и низкоуровневые классы зависимы от абстракций, а не друг от друга.
Зависимости строятся относительно абстракций, а не деталей.
"""
