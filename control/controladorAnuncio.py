from dao.daoAnuncio import DaoAnuncio
from model.anuncio import Anuncio


class ControladorAnuncio():

    def __init__(self):
        self.__dao_anuncio = DaoAnuncio("anuncios.csv")

    def anunciar_curso(self, curso, tempo_divulgacao, pular_qtd=0):
        self.__dao_anuncio.cadastrar_anuncio(
            Anuncio(curso, tempo_divulgacao), pular_qtd)

    def total_cursos(self):
        return self.__dao_anuncio.total_cursos()
