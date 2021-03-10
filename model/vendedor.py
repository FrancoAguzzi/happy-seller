from .pessoa import Pessoa

class Vendedor(Pessoa):

    def __init__(self, nome, cpf, acc, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__acc = acc
        self.__senha = senha

    def pegar_dados_como_tuplas(self):
        return (
            ("nome", self.__nome),
            ("cpf", self.__cpf),
            ("acc", self.__acc),
            ("senha", self.__senha)
        )
