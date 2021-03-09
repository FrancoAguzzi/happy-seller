from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def comecar(self):
        pass

    @abstractmethod
    def rodar(self, window):
        pass

    def voltar(self, prox_tela = "MENU", result = None, view = None):
        if (not result):
            result = {}
        if (view):
            view.close()
        return { "prox_tela": prox_tela, "result": result }