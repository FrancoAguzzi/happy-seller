from model.vendedor import Vendedor
from model.curso import Curso
from dao.daoVendedor import DaoVendedor
from dao.daoCurso import DaoCurso
from view.viewCadastroCurso import ViewCadastroCurso


class ControladorCadastro():
    def __init__(self):
        self.__dao_vendedor = DaoVendedor("vendedores.csv")
        self.__dao_curso = DaoCurso("cursos.csv")
        self.__tela_cadastro_curso = ViewCadastroCurso()

    def cadastrar_vendedor(self, nome, cpf, acc, password):
        vendedor = Vendedor(nome, cpf, acc, password)
        return self.__dao_vendedor.cadastrar_vendedor(vendedor)

    def cadastrar_curso(self, nome_anunc, cpf_anunc, ncc, cvv, nome_curso, link_curso, preco_curso):
        curso = Curso(nome_anunc, cpf_anunc, ncc, cvv, nome_curso, link_curso, preco_curso)
        return self.__dao_curso.cadastrar_curso(curso)

    def abrir_tela_curso(self):
        return self.__tela_cadastro_curso.comecar()
    