
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

    # def carregar_dados(self):
    #    self.__cache = []
    #    if os.path.isfile(self.__data_source):
    #        with open(self.__data_source, "r") as src:
    #            for line in src.read().splitlines():
    #                self.__cache.append(Vendedor(*line.split(",")))

    def cadastrar_vendedor(self, vendedor):
        with open(self.__data_source, "a") as src:
            dados = vendedor.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                linha += f"{v},"
            src.write(linha[:-1] + "\n")
        self.__cache = self.carregar_dados(Vendedor, self.__data_source)

    def existe_cpf(self, cpf):
        if not self.__cache:
            self.__cache = self.carregar_dados(Vendedor, self.__data_source)
        for vendedor in self.__cache:
            if vendedor.cpf == cpf:
                return True
        return False

    def existe_cnpj(self, cnpj):
        if not self.__cache:
            self.__cache = self.carregar_dados(Vendedor, self.__data_source)
        for vendedor in self.__cache:
            if vendedor.cnpj == cnpj:
                return True
        return False

    def pegar_vendedor(self, cnpj, senha):
        if not self.__cache:
            self.__cache = self.carregar_dados(Vendedor, self.__data_source)
        for vendedor in self.__cache:
            if vendedor.cnpj == cnpj and vendedor.senha == senha:
                return vendedor
