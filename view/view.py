from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def comecar(self):
        pass

    @abstractmethod
    def rodar(self, window):
        pass
