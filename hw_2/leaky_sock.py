from hw_2.interfaices import IGameItem, ItemFabric


class LeakySockReward(IGameItem):
    def open(self):
        print('LeakySock')


class LeakySockGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return LeakySockReward()
