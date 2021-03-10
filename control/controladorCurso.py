from model.curso import Curso
from dao.daoCurso import DaoCurso
from view.viewCadastroCurso import ViewCadastroCurso


class ControladorCurso():
    def __init__(self):
        self.__dao_curso = DaoCurso("cursos.csv")
        self.__tela_cadastro_curso = ViewCadastroCurso()

    def cadastrar_curso(self, nome_anunc, cpf_anunc, ncc, cvv, nome_curso, link_curso, preco_curso):
        curso = Curso(nome_anunc, cpf_anunc, ncc, cvv, nome_curso, link_curso, preco_curso)
        return self.__dao_curso.cadastrar_curso(curso)

    def abrir_tela_curso(self):
        return self.__tela_cadastro_curso.comecar()

    def filtrar_cursos_por_cpf(self, cpf_anunciante):
        return self.__dao_curso.filtrar_cursos_por_cpf(cpf_anunciante)
    
    def total_de_cursos_na_esteira(self):
        return self.__dao_curso.total_de_cursos_na_esteira()