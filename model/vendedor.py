from model.pessoa import Pessoa


class Vendedor(Pessoa):

    def __init__(self, nome, cpf, conta_bancaria, cnpj, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__conta_bancaria = conta_bancaria
        self.__cnpj = cnpj
        self.__senha = senha
        self.__horas_descansadas_dia = 0
        self.__comissao_atual = 0.0005
        self.__salario_bruto_acumulado_plantao = 0
        self.__salario_bruto = 0
        self.__comissao_base = 0.1

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

    @property
    def horas_descansadas_dia(self):
        return self.__horas_descansadas_dia

    @property
    def comissao_atual(self):
        return self.__comissao_atual

    @property
    def salario_bruto_acumulado_plantao(self):
        return self.__salario_bruto_acumulado_plantao

    @property
    def salario_bruto(self):
        return self.__salario_bruto

    @property
    def comissao_base(self):
        return self.__comissao_base

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @horas_descansadas_dia.setter
    def horas_descansadas_dia(self, horas_descansadas_dia):
        self.__horas_descansadas_dia = horas_descansadas_dia

    @comissao_atual.setter
    def comissao_atual(self, comissao_atual):
        self.__comissao_atual = comissao_atual

    @salario_bruto_acumulado_plantao.setter
    def salario_bruto_acumulado_plantao(self, salario_bruto_acumulado_plantao):
        self.__salario_bruto_acumulado_plantao = salario_bruto_acumulado_plantao

    @salario_bruto.setter
    def salario_bruto(self, salario_bruto):
        self.__salario_bruto = salario_bruto

    def pegar_dados_como_tuplas(self):
        return (
            ("nome", self.__nome),
            ("cpf", self.__cpf),
            ("conta_bancaria", self.__conta_bancaria),
            ("cnpj", self.__cnpj),
            ("senha", self.__senha)
        )
