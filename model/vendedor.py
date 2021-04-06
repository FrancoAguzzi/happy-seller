from model.pessoa import Pessoa

class Vendedor(Pessoa):

    def __init__(self, nome, cpf, conta_bancaria, cnpj, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__conta_bancaria = conta_bancaria
        self.__cnpj = cnpj
        self.__senha = senha
        self.__horas_descansadas_dia = 0
        self.__comissao_atual = 0.05
        self.__salario = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def senha(self):
        return self.__senha

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
            ("conta_bancaria", self.__conta_bancaria),
            ("cnpj", self.__cnpj),
            ("senha", self.__senha)
        )
