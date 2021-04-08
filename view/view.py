from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def comecar(self, erro=None, **kwargs):
        pass

    @abstractmethod
    def rodar(self, window, erro):
        pass

    def voltar(self, prox_tela="MENU", result=None, view=None):
        if (not result):
            result = {}
        if (view):
            view.close()
        return {"prox_tela": prox_tela, "result": result}

    def tem_valores_vazios(self, valores):
        for (k, v) in valores.items():
            if v == "":
                return True
        return False