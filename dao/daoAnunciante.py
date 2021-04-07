import os
import csv

from dao.daoAbstrato import DaoAbstrato
from model.anunciante import Anunciante

class DaoAnunciante(DaoAbstrato):
    def __init__(self, data_source):
        self.__data_source = data_source
        self.__cache = None

    @property
    def data_source(self):
        return self.__data_source

    @data_source.setter
    def data_source(self, source):
        self.__data_source = source

    def carregar_dados(self):
        self.__cache = []
        if os.path.isfile(self.__data_source):
            with open(self.__data_source, "r") as src:
                for line in src.read().splitlines():
                    self.__cache.append(Anunciante(*line.split(",")))

    def cadastrar_anunciante(self, anunciante):
        with open(self.__data_source, "a") as src:
            dados = anunciante.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                linha += f"{v},"
            src.write(linha[:-1] + "\n")
        self.carregar_dados()


    def existe_cpf(self, cpf):
        if not self.__cache:
            self.carregar_dados()
        for anunciante in self.__cache:
            if anunciante.cpf == cpf:
                return True
        return False
    
    def pegar_anunciante(self, cpf, senha):
        if not self.__cache:
            self.carregar_dados()
        for anunciante in self.__cache:
            if anunciante.cpf == cpf and anunciante.senha == senha:
                return anunciante