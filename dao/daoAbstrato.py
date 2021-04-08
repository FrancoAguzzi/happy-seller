from abc import ABC, abstractmethod
from typing import Union
import os


from model.anunciante import Anunciante
from model.curso import Curso
from model.vendedor import Vendedor


class DaoAbstrato(ABC):

    @property
    @abstractmethod
    def data_source(self):
        pass

    @data_source.setter
    @abstractmethod
    def data_source(self, source):
        pass

    def carregar_dados(self, model: Union[Anunciante, Curso, Vendedor], data_source):
        dados = []
        if os.path.isfile(data_source):
            with open(data_source, "r") as src:
                for line in src.read().splitlines():
                    dados.append(model(*line.split(",")))
        return dados
