class Curso():

    def __init__(self, nome_anunc, cpf_anunc, ncc, cvv, nome_curso, link_curso, preco_curso):
        self.__nome_anunc = nome_anunc
        self.__cpf_anunc = cpf_anunc
        self.__ncc = ncc
        self.__cvv = cvv
        self.__nome_curso = nome_curso
        self.__link_curso = link_curso
        self.__preco_curso = preco_curso
        self.__tempo_divulgacao = 0

    def pegar_dados_como_tuplas(self):
        return (
            ("nome_anunc", self.__nome_anunc),
            ("cpf_anunc", self.__cpf_anunc),
            ("ncc", self.__ncc),
            ("cvv", self.__cvv),
            ("nome_curso", self.__nome_curso),
            ("link_curso", self.__link_curso),
            ("preco_curso", self.__preco_curso),
            ("tempo_divulgacao", self.__tempo_divulgacao)
        )
