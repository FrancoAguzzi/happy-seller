from model.anunciante import Anunciante
from dao.daoAnunciante import DaoAnunciante
from view.viewCadastroAnunciante import ViewCadastroAnunciante
# from view.viewAnuncioCurso import ViewAnuncioCurso


class ControladorAnunciante():
    def __init__(self):
        self.__dao_anunciante = DaoAnunciante("anunciantes.csv")
        self.__tela_cadastro_anunciante = ViewCadastroAnunciante()

    def cadastrar_anunciante(self, nome_anunc, cpf_anunc, ncc, cvv):
        anunciante = Anunciante(nome_anunc, cpf_anunc, ncc, cvv)
        return self.__dao_anunciante.cadastrar_anunciante(anunciante)

    def abrir_tela_anunciante(self):
        return self.__tela_cadastro_anunciante.comecar()
