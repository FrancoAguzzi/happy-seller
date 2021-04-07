class Curso():

    def __init__(self, cpf_anunciante, nome_curso, link_curso, preco_curso):
        self.__cpf_anunciante = cpf_anunciante
        self.__nome_curso = nome_curso
        self.__link_curso = link_curso
        self.__preco_curso = preco_curso
        self.__tempo_divulgacao = 0

    def pegar_dados_como_tuplas(self):
        return (
            ("cpf_anunciante", self.__cpf_anunciante),
            ("nome_curso", self.__nome_curso),
            ("link_curso", self.__link_curso),
            ("preco_curso", self.__preco_curso),
            ("tempo_divulgacao", self.__tempo_divulgacao)
        )
