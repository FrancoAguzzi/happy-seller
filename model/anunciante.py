from model.pessoa import Pessoa

class Anunciante(Pessoa):

    def __init__(self, nome, cpf, numero_cartao_credito, cvv_cartao_credito, senha, cursos_cadastrados = []):
        self.__nome = nome
        self.__cpf = cpf
        self.__numero_cartao_credito = numero_cartao_credito
        self.__cvv_cartao_credito = cvv_cartao_credito
        self.__senha = senha
        self.__cursos_cadastrados = cursos_cadastrados

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def senha(self):
        return self.__senha
        
    @property
    def cursos_cadastrados(self):
        return self.__cursos_cadastrados

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    @cursos_cadastrados.setter
    def cursos_cadastrados(self, cursos):
        self.__cursos_cadastrados = cursos

    def pegar_dados_como_tuplas(self):
        return (
            ("nome", self.__nome),
            ("cpf", self.__cpf),
            ("numero_cartao_credito", self.__numero_cartao_credito),
            ("cvv_cartao_credito", self.__cvv_cartao_credito),
            ("senha", self.__senha),
            ("cursos_cadastrados", self.__cursos_cadastrados)
        )
