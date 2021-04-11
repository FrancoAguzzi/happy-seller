from dao.daoAbstrato import DaoAbstrato
from dao.daoEsteiraCurso import DaoEsteiraCurso


class DaoCurso(DaoAbstrato):
    def __init__(self, data_source):
        self.__data_source = data_source

    @property
    def data_source(self):
        return self.__data_source

    @data_source.setter
    def data_source(self, source):
        self.__data_source = source

    def cadastrar_curso(self, curso):
        with open(self.__data_source, "a") as src:
            dados = curso.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                linha += f"{v},"
            src.write(linha[:-1] + "\n")

    def filtrar_cursos_por_cpf(self, cpf_anunciante):
        cursos = []
        with open(self.__data_source, "r") as src:
            lines = src.readlines()
        for line in lines:
            curso = line.split(",")
            if curso[1] == str(cpf_anunciante):
                cursos.append(curso)
        if cursos:
            cursos_filtrados = []
            for curso in cursos:
                cursos_filtrados.append({
                    "nome_curso": curso[0],
                    "link_curso": curso[1],
                    "preco_curso": curso[2]
                })
            return cursos_filtrados
        return []

    def total_de_cursos_na_esteira(self):
        pass
        # return DaoEsteiraCurso("esteira_cursos.csv").quantidade_cursos_na_frente()
