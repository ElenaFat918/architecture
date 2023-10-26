from hw_2.interfaices import IGameItem, ItemFabric


class DiamondReward(IGameItem):
    def open(self):
        print('Diamond')

        
class DiamondGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return DiamondReward()
