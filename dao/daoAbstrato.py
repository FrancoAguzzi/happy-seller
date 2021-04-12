from abc import ABC, abstractmethod
import os
import hashlib


class DaoAbstrato(ABC):

    @property
    @abstractmethod
    def data_source(self):
        pass

    @data_source.setter
    @abstractmethod
    def data_source(self, source):
        pass

    def carregar_dados(self, model, data_source):
        dados = []
        if os.path.isfile(data_source):
            with open(data_source, "r") as src:
                for line in src.read().splitlines():
                    dados.append(model(*line.split(",")))
        return dados

    def salvar_dados(self, dados):
        with open(self.data_source, "w") as src:
            for dado in dados:
                valores = dado.pegar_dados_como_tuplas()
                linha = ""
                for (k, v) in valores:
                    linha += f"{v},"
                src.write(linha[:-1] + "\n")

    def encriptar_dado(self, dado):
        return hashlib.sha256(dado.encode()).hexdigest()
