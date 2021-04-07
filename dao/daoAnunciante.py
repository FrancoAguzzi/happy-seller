from dao.daoAbstrato import DaoAbstrato
from model.anunciante import Anunciante


class DaoAnunciante(DaoAbstrato):
    def __init__(self, data_source):
        self.__data_source = data_source
        self.__cache = None

    @property
    def data_source(self):
        return self.__data_source

    @data_source.setter
    def data_source(self, source):
        self.__data_source = source

    def cadastrar_anunciante(self, anunciante: Anunciante):
        with open(self.__data_source, "a") as src:
            dados = anunciante.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                linha += f"{v},"
            src.write(linha[:-1] + "\n")
        self.__cache = self.carregar_dados(Anunciante, self.__data_source)

    def existe_cpf(self, cpf):
        if not self.__cache:
            self.__cache = self.carregar_dados(Anunciante, self.__data_source)
        for vendedor in self.__cache:
            if vendedor.cpf == cpf:
                return True
        return False
