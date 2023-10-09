from hw_2.interfaices import IGameItem, ItemFabric


# Класс 'Сундук золота', наследуется от модели
class GoldReward(IGameItem):
    def open(self):
        print('Gold')


# Класс основанный на модели класса Фабрика
class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()
