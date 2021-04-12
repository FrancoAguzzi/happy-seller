from dao.daoAnuncio import DaoAnuncio


class ControladorAnuncio():

    def __init__(self):
        self.__dao_anuncio = DaoAnuncio("anuncios.csv")

    def anunciar_curso(self, curso, tempo_divulgacao, pular_qtd):
        pass
