
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

    def pegar_vendedor(self, cpf, senha):
        if not self.__cache:
            self.__cache = self.carregar_dados(Vendedor, self.__data_source)
        for vendedor in self.__cache:
            if vendedor.cpf == cpf and vendedor.senha == senha:
                return vendedor


    def atualizar_vendedor(self, cpf, conta_bancaria, cnpj, senha):
        vendedor_atualizado = None
        for i, vendedor in enumerate(self.__cache):
            if vendedor.cpf == cpf:
                vendedor_atualizado = Vendedor(vendedor.nome, cpf, conta_bancaria, cnpj, senha)
                self.__cache[i] = vendedor_atualizado
                break

        else:
            return

        self.salvar_dados(self.__cache)
        self.__cache = self.carregar_dados(Vendedor, self.__data_source)
        return vendedor_atualizado

    def apagar_vendedor(self, cpf):
        for i, vendedor in enumerate(self.__cache):
            if vendedor.cpf == cpf:
                del self.__cache[i]
                break

        else:
            return

        self.salvar_dados(self.__cache)
        self.__cache = self.carregar_dados(Vendedor, self.__data_source)
