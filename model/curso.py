class Curso():

    def __init__(self, nome_curso, link_curso, preco_curso):
        self.__nome_curso = nome_curso
        self.__link_curso = link_curso
        self.__preco_curso = preco_curso

    @property
    def nome_curso(self):
        return self.__nome_curso

    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso

    @property
    def link_curso(self):
        return self.__link_curso

    @link_curso.setter
    def link_curso(self, link_curso):
        self.__link_curso = link_curso

    @property
    def preco_curso(self):
        return self.__preco_curso

    @preco_curso.setter
    def preco_curso(self, preco_curso):
        self.__preco_curso = preco_curso

    def pegar_dados_como_tuplas(self):
        return (
            ("nome_curso", self.__nome_curso),
            ("link_curso", self.__link_curso),
            ("preco_curso", self.__preco_curso)
        )
