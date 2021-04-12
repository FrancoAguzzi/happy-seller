import os

from dao.daoAbstrato import DaoAbstrato
from model.anuncio import Anuncio
from model.curso import Curso


class DaoAnuncio(DaoAbstrato):

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
        dados = []
        if os.path.isfile(self.__data_source):
            with open(self.__data_source, "r") as src:
                for line in src.read().splitlines():
                    splitted = line.split(",")
                    dados.append(Anuncio(
                        curso=Curso(
                            nome_curso=splitted[0],
                            link_curso=splitted[1],
                            preco_curso=splitted[2]
                        ),
                        tempo_divulgacao=splitted[3],
                        posicao=splitted[4]
                    ))
        return dados

    def ordena_dados(self, dados):
        dados_ordenados = []
        for i in range(len(dados)):
            for dado in dados:
                if dado.posicao == i:
                    dados_ordenados.append(dado)
        return dados_ordenados

    def cadastrar_anuncio(self, anuncio, pular_qtd):
        if not self.__cache:
            self.__cache = self.carregar_dados()

        posicao_final = 0
        if isinstance(self.__cache, list) and len(self.__cache) > 0:
            dados = self.ordena_dados(self.__cache)
            posicao_final = len(self.__cache)
            for i in range(pular_qtd):
                atual = dados[i]
                dados[i] = Anuncio(
                    atual.curso, atual.tempo_divulgacao, atual.posicao + 1)
            self.salvar_dados(dados)

        anuncio = Anuncio(anuncio.curso, anuncio.tempo_divulgacao,
                          posicao_final - pular_qtd)
        with open(self.__data_source, "a") as src:
            dados = anuncio.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                if k == "curso":
                    for k1, v1 in v:
                        linha += f"{v1},"
                    continue
                linha += f"{v},"
            src.write(linha[:-1] + "\n")
        self.__cache = self.carregar_dados()

    def salvar_dados(self, dados):
        with open(self.data_source, "w") as src:
            for dado in dados:
                valores = dado.pegar_dados_como_tuplas()
                linha = ""
                for (k, v) in valores:
                    if k == "curso":
                        for k1, v1 in v:
                            linha += f"{v1},"
                        continue
                    linha += f"{v},"
                src.write(linha[:-1] + "\n")

    def total_cursos(self):
        if not self.__cache:
            self.__cache = self.carregar_dados()

        return len(self.__cache)
