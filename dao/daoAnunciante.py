import os
import csv
import json

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

    def cadastrar_anunciante(self, anunciante, overwrite_password=True):
        with open(self.__data_source, "a") as src:
            dados = anunciante.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                if k == "cursos":
                    for curso in v:
                        for (k1, v1) in curso:
                            linha += f"{v1}'"
                        linha = linha[:-1] + ";"
                    linha = linha[:-1] + ","
                elif k == "senha" and overwrite_password:
                    linha += f"{self.encriptar_dado(v)},"
                else:
                    linha += f"{v},"
            src.write(linha[:-1] + "\n")
        self.__cache = self.carregar_dados(Anunciante, self.__data_source)

    def atualiza_anunciante(self, anunciante):
        self.apagar_anunciante(anunciante.cpf)
        self.cadastrar_anunciante(anunciante, False)

    def apagar_anunciante(self, cpf):
        for i, anunciante in enumerate(self.__cache):
            if anunciante.cpf == cpf:
                del self.__cache[i]
                break

        else:
            return

        self.salvar_dados(self.__cache)
        self.__cache = self.carregar_dados(Anunciante, self.__data_source)

    def existe_cpf(self, cpf):
        if not self.__cache:
            self.__cache = self.carregar_dados(Anunciante, self.__data_source)
        for anunciante in self.__cache:
            if anunciante.cpf == cpf:
                return True
        return False

    def pegar_anunciante(self, cpf, senha):
        if not self.__cache:
            self.__cache = self.carregar_dados(Anunciante, self.__data_source)
        for anunciante in self.__cache:
            if anunciante.cpf == cpf and anunciante.senha == self.encriptar_dado(senha):
                return anunciante

    def cadastrar_curso(self, anunciante: Anunciante, curso):
        self.atualiza_anunciante(anunciante.insere_curso(curso))

        self.__cache = self.carregar_dados(Anunciante, self.__data_source)

    def existe_curso(self, nome):
        self.__cache = self.carregar_dados(Anunciante, self.__data_source)
        for anunciante in self.__cache:
            for curso in anunciante.cursos:
                if curso.nome_curso == nome:
                    return True
        return False
