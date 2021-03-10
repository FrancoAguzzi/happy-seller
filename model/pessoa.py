from abc import ABC, abstractmethod


class Pessoa(ABC):

    @property
    @abstractmethod
    def nome(self):
        pass

    @property
    @abstractmethod
    def cpf(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass

    @cpf.setter
    @abstractmethod
    def cpf(self, cpf):
        pass
