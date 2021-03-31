from dao.daoAbstrato import DaoAbstrato
from model.vendedor import Vendedor


class DaoVendedor(DaoAbstrato):
    def __init__(self, data_source):
        self.__data_source = data_source
        self.__cache = None

    @property
    def data_source(self):
        return self.__data_source

    @data_source.setter
    def data_source(self, source):
        self.__data_source = source

    def carregar_dados(self):
        self.__cache = []
        with open(self.__data_source, "r") as src:
            for line in src.readlines():
                self.__cache.append(Vendedor(*line.split(",")))

    def cadastrar_vendedor(self, vendedor):
        with open(self.__data_source, "a") as src:
            dados = vendedor.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                linha += f"{v},"
            src.write(linha[:-1] + "\n")
        self.carregar_dados()


    def existe_cpf(self, cpf):
        if not self.__cache:
            self.carregar_dados()
        for vendedor in self.__cache:
            if vendedor.cpf == cpf:
                return True
        return False


    def existe_cnpj(self, cnpj):
        if not self.__cache:
            self.carregar_dados()
        for vendedor in self.__cache:
            if vendedor.cnpj == cnpj:
                return True
        return False
