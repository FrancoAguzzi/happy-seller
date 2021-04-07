from model.pessoa import Pessoa


class Anunciante(Pessoa):

    def __init__(self, nome, cpf, ncc, cvv):
        self.__nome = nome
        self.__cpf = cpf
        self.__ncc = ncc
        self.__cvv = cvv

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def ncc(self):
        return self.__ncc

    @property
    def cvv(self):
        return self.__cvv

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @ncc.setter
    def ncc(self, ncc):
        self.__ncc = ncc

    @cvv.setter
    def cvv(self, cvv):
        self.__cvv = cvv

    def pegar_dados_como_tuplas(self):
        return (
            ("nome", self.__nome),
            ("cpf", self.__cpf),
            ("ncc", self.__ncc),
            ("cvv", self.__cvv),
        )
