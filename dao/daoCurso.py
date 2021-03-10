from dao.daoAbstrato import DaoAbstrato


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
