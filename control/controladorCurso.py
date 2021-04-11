from model.curso import Curso
from dao.daoAnunciante import DaoAnunciante
from view.viewCadastroCurso import ViewCadastroCurso
from view.viewAnuncioCurso import ViewAnuncioCurso


class ControladorCurso():
    def __init__(self):
        self.__tela_cadastro_curso = ViewCadastroCurso()

    def cadastrar_curso(self, nome_curso, link_curso, preco_curso):
        return Curso(nome_curso, link_curso, preco_curso)

    def abrir_tela_curso(self):
        return self.__tela_cadastro_curso.comecar()

    def anunciar_curso(self, result):
        pass

    def abrir_tela_anunciar_curso(self, cursos):
        # cursos_na_frente = self.total_de_cursos_na_esteira()
        # return ViewAnuncioCurso(cursos, cursos_na_frente).comecar()
        return ViewAnuncioCurso(cursos, 5).comecar()

    def filtrar_cursos_por_cpf(self, cpf_anunciante):
        return self.__dao_curso.filtrar_cursos_por_cpf(cpf_anunciante)

    def total_de_cursos_na_esteira(self):
        return self.__dao_curso.total_de_cursos_na_esteira()
