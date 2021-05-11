from dao.daoAnuncio import DaoAnuncio
from model.anuncio import Anuncio

from datetime import datetime, timedelta


class ControladorAnuncio():

    def __init__(self):
        self.__dao_anuncio = DaoAnuncio("anuncios.csv")

    def anunciar_curso(self, curso, tempo_divulgacao, pular_qtd=0):
        self.__dao_anuncio.cadastrar_anuncio(
            Anuncio(curso, tempo_divulgacao), pular_qtd)

    def pegar_proximo_anuncio(self, anuncio: Anuncio = None, tempo_atual: datetime = None, tempo_anterior: datetime = None):
        anuncios = self.__dao_anuncio.carregar_dados()
        if not tempo_atual:
            tempo_atual = datetime.now()
        if not tempo_anterior:
            tempo_anterior = datetime.now()

        if not anuncio:
            if len(anuncios) > 0:
                return anuncios[0], tempo_atual
            else:
                return None, tempo_atual

        if tempo_anterior + timedelta(minutes=int(anuncio.tempo_divulgacao) / 10) > tempo_atual:
            return anuncio, tempo_atual

        anuncios = anuncios[1:]

        self.__dao_anuncio.salvar_dados(anuncios)

        if len(anuncios) > 0:
            return anuncios[0], tempo_atual
        else:
            return None, tempo_atual

    def total_cursos(self):
        return self.__dao_anuncio.total_cursos()
