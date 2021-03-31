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

    def tem_valores_vazios(self, valores):
        for (k, v) in valores.items():
            if v == "":
                return True
        return False

    def identificar_campos_invalidos(self, verificacoes, campos):
        default = (lambda x: True, "Campo valido")

        for k, v in campos.items():
            f = verificacoes.setdefault(k, default)
            if not f[0](v):
                return k, f[1]
