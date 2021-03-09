from .pessoa import Pessoa

class Vendedor(Pessoa):

    def __init__(self, acc, senha):
        self.__acc = acc
        self.__senha = senha

    def pegar_dados_como_tuplas(self):
        return (
            ("nome", self.__nome),
            ("cpf", self.__cpf),
            ("acc", self.__acc),
            ("senha", self.__senha)
        )
