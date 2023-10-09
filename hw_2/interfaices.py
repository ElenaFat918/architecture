from abc import ABC, abstractmethod


#   Абстрактный класс Фабрика
class ItemFabric(ABC):
    # Абстрактный метод создания объекта в Фабрике
    @abstractmethod
    def create_item(self):
        pass

    # Метод, создаёт и открывает объект
    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


# Абстрактный класс объекта ItemFabric
class IGameItem(ABC):
    # Абстрактный метод 'открытия'
    @abstractmethod
    def open(self):
        pass
