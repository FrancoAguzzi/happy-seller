from model.curso import Curso
from dao.daoAnunciante import DaoAnunciante
from view.viewCadastroCurso import ViewCadastroCurso
from view.viewAnuncioCurso import ViewAnuncioCurso

class ControladorCurso():
    def __init__(self):
        self.__dao_anunciante = DaoAnunciante("anunciantes.csv")
        self.__tela_cadastro_curso = ViewCadastroCurso()
        self.__tela_anuncio_curso = ViewAnuncioCurso()

    def cadastrar_curso(self, nome_curso, link_curso, preco_curso):
        curso = Curso(nome_curso, link_curso, preco_curso)
        return self.__dao_anunciante.cadastrar_curso(curso)

    def abrir_tela_curso(self):
        return self.__tela_cadastro_curso.comecar()

    def abrir_anuncio_curso(self):
        return self.__tela_anuncio_curso.comecar()
