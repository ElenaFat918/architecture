from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class DisielEngine(Engine):
    def start(self):
        print('Запущен дизельный двигатель')


class PetrolEngine(Engine):
    def start(self):
        print('Запущен бензиновый двигатель')
