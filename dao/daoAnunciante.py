from dao.daoAbstrato import DaoAbstrato
from model.anunciante import Anunciante


class DaoAnunciante(DaoAbstrato):
    def __init__(self, data_source):
        self.__data_source = data_source

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

    def existe_cpf(self, cpf):
        if not self.__cache:
            self.carregar_dados()
        for vendedor in self.__cache:
            if vendedor.cpf == cpf:
                return True
        return False
