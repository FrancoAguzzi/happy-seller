from abc import ABC, abstractmethod


class DaoAbstrato(ABC):

    @property
    @abstractmethod
    def data_source(self):
        pass

    @data_source.setter
    @abstractmethod
    def data_source(self, source):
        pass
