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

    def cadastrar_anunciante(self, anunciante):
        with open(self.__data_source, "a") as src:
            dados = anunciante.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                linha += f"{v},"
            src.write(linha[:-1] + "\n")
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
            if anunciante.cpf == cpf and anunciante.senha == senha:
                return anunciante

    def cadastrar_curso(self, curso):
        pass
        if not self.__cache:
            self.__cache = self.carregar_dados(Anunciante, self.__data_source)
        lines = list()
        dono_curso = {}
        obj_curso = json.dumps(
            {"nome_curso": curso.nome_curso, "link_curso": curso.link_curso, "preco_curso": curso.preco_curso})
        with open(self.__data_source, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                if row[1] == '10891990909':
                    dono_curso = row
                    dono_curso[-1] = dono_curso[-1].split(']')[
                        1].join(obj_curso)
                    lines.remove(row)
                    print(dono_curso)
                    lines.append(dono_curso)
                print(lines)
        with open(self.__data_source, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        with open(self.__data_source, "r") as src:
            for row in src:
                cpf_atual = row.split(',')[1]
                if cpf_atual == "10891990909":
                    with open(self.__data_source, "w") as writer:
                        row.split(",")[5] = row.split(",")[
                            5].split("]")[1].join('aaaa')
            dados = anunciante.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                linha += f"{v},"
            src.write(linha[:-1] + "\n")
        self.__cache = self.carregar_dados(Anunciante, self.__data_source)
