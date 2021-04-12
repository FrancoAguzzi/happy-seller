class Anuncio():

    def __init__(self, curso, tempo_divulgacao, posicao=0):
        self.__curso = curso
        self.__tempo_divulgacao = tempo_divulgacao
        self.__posicao = posicao

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def tempo_divulgacao(self):
        return self.__tempo_divulgacao

    @tempo_divulgacao.setter
    def tempo_divulgacao(self, tempo_divulgacao):
        self.__tempo_divulgacao = tempo_divulgacao

    @property
    def posicao(self):
        return int(self.__posicao)

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = int(posicao)

    def pegar_dados_como_tuplas(self):
        return (
            ("curso", self.__curso.pegar_dados_como_tuplas()),
            ("tempo_divulgacao", self.__tempo_divulgacao),
            ("posicao", self.__posicao)
        )
