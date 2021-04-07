from dao.daoAbstrato import DaoAbstrato
from model.esteiraCurso import EsteiraCurso


class DaoEsteiraCurso(DaoAbstrato):
    def __init__(self, data_source):
        self.__data_source = data_source

    @property
    def data_source(self):
        return self.__data_source

    @data_source.setter
    def data_source(self, source):
        self.__data_source = source

    def cadastrar_esteira_curso(self, esteira_curso):
        with open(self.__data_source, "a") as src:
            dados = esteira_curso.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                linha += f"{v},"
            src.write(linha[:-1] + "\n")
    
    def carregar_esteira_curso(self):
        with open(self.__data_source, "r") as src:
            line = src.readline()
            esteira = line.split(",")
        if not esteira:
            return None
        else:
            return EsteiraCurso(esteira[0], esteira[1], esteira[2])

    def mudar_posicao_curso(self, curso, esteira_curso, quantidade=0, posicao_inicial=0):
        if not esteira:
            esteira = EsteiraCurso([curso], 1, curso)
    
    def quantidade_cursos_na_frente(self):
        esteira = self.carregar_esteira_curso()
        if not esteira:
            return 0
        else:
            pass
