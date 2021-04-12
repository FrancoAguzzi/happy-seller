from dao.daoAbstrato import DaoAbstrato


class DaoAnuncio(DaoAbstrato):

    def __init__(self, data_source):
        self.__data_source = data_source

    @property
    def data_source(self):
        return self.__data_source

    @data_source.setter
    def data_source(self, source):
        self.__data_source = source
