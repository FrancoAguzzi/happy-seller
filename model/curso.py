class Curso():

    def __init__(self, nome_curso, link_curso, preco_curso):
        self.__nome_curso = nome_curso
        self.__link_curso = link_curso
        self.__preco_curso = preco_curso

    def pegar_dados_como_tuplas(self):
        return (
            ("nome_curso", self.__nome_curso),
            ("link_curso", self.__link_curso),
            ("preco_curso", self.__preco_curso)
        )
