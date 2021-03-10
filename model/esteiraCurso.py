

class EsteiraCurso():

    def __init__(self, cursos, num_cursos, prox_curso):
        self.__cursos = cursos
        self.__num_cursos = num_cursos
        self.__prox_curso = prox_curso

    @property
    def cursos(self):
        return self.__cursos

    @property
    def num_cursos(self):
        return self.__num_cursos

    @cursos.setter
    def cursos(self, cursos):
        self.__cursos = cursos

    @num_cursos.setter
    def num_cursos(self, num_cursos):
        self.__num_cursos = num_cursos

    def pegar_dados_como_tuplas(self):
        return (
            ("cursos", self.__cursos),
            ("num_cursos", self.__num_cursos),
            ("prox_curso", self.__prox_curso)
        )
