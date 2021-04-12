from model.pessoa import Pessoa
from model.curso import Curso


class Anunciante(Pessoa):

    def __init__(self, nome, cpf, numero_cartao_credito, cvv_cartao_credito, senha, cursos=[]):
        self.__nome = nome
        self.__cpf = cpf
        self.__numero_cartao_credito = numero_cartao_credito
        self.__cvv_cartao_credito = cvv_cartao_credito
        self.__senha = senha
        self.__cursos = []
        if cursos:
            for curso_agg in cursos.split(";"):
                curso_split = curso_agg.split("'")
                self.__cursos.append(Curso(
                    curso_split[0],
                    curso_split[1],
                    curso_split[2]
                ))

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
    def cursos(self):
        return self.__cursos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def insere_curso(self, curso):
        self.__cursos.append(curso)
        return self

    def remove_curso(self, curso):
        for curso_anunc in self.__cursos:
            if curso_anunc == curso:
                index = self.__cursos.index(curso)
                self.__cursos = self.__cursos.pop(index)

        return self

    def pegar_dados_como_tuplas(self):
        cursos = []
        for curso in self.__cursos:
            cursos.append(curso.pegar_dados_como_tuplas())

        return (
            ("nome", self.__nome),
            ("cpf", self.__cpf),
            ("numero_cartao_credito", self.__numero_cartao_credito),
            ("cvv_cartao_credito", self.__cvv_cartao_credito),
            ("senha", self.__senha),
            ("cursos", cursos)
        )
