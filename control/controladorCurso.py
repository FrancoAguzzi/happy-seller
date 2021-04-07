from model.curso import Curso
from dao.daoAnunciante import DaoAnunciante
from dao.daoCurso import DaoCurso
from view.viewCadastroCurso import ViewCadastroCurso
from view.viewAnuncioCurso import ViewAnuncioCurso

class ControladorCurso():
    def __init__(self):
        # TODO
        # PASSAR CURSOS COMO ARGUMENTO FROM CONTROLADOR ANUNCIANTE
        # P/ REMOVER DUPLO ACESSO AO DAO ANUNCIANTE
        self.__dao_anunciante = DaoAnunciante("anunciantes.csv")
        self.__dao_curso = DaoCurso("anunciantes.csv")
        self.__tela_cadastro_curso = ViewCadastroCurso()

    def cadastrar_curso(self, nome_curso, link_curso, preco_curso):
        curso = Curso(nome_curso, link_curso, preco_curso)
        return self.__dao_anunciante.cadastrar_curso(curso)

    def abrir_tela_curso(self):
        return self.__tela_cadastro_curso.comecar()

    def anunciar_curso(self, result):
        return self.__tela_anuncio_curso.comecar()

    def abrir_tela_anunciar_curso(self, cpf_anunciante):
        anunciante = self.filtrar_cursos_por_cpf(cpf_anunciante)
        cursos_na_frente = self.total_de_cursos_na_esteira()
        #return ViewAnuncioCurso(cursos, cursos_na_frente).comecar()
        # return ViewAnuncioCurso(cursos, 5).comecar()
    
    def total_de_cursos_na_esteira(self):
        return self.__dao_curso.total_de_cursos_na_esteira()
