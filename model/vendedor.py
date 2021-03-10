from model.pessoa import Pessoa

class Vendedor(Pessoa):

    def __init__(self, nome, cpf, acc, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__acc = acc
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def pegar_dados_como_tuplas(self):
        return (
            ("nome", self.__nome),
            ("cpf", self.__cpf),
            ("acc", self.__acc),
            ("senha", self.__senha)
        )
