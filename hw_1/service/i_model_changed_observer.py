from abc import ABC, abstractmethod


class IModelChangedObserver(ABC):
    @abstractmethod
    def apply_update_model(self):
        pass


class IntermediateIMCO(IModelChangedObserver):
    def apply_update_model(self):
        pass
