from view.viewCadastroVendedor import ViewCadastroVendedor
from view.viewTelaInicial import ViewTelaInicial
from control.controladorCurso import ControladorCurso
from control.controladorVendedor import ControladorVendedor


class ControladorSistema:

    def __init__(self):
        # atributos controlador sistema
        self.__tela_inicial = ViewTelaInicial()
        self.__controlador_curso = ControladorCurso()
        self.__controlador_vendedor = ControladorVendedor()
        self.__vendedor = None
        self.__anunciante = None
        self.__esta_logado = False


    def inicia(self, tela=None):
        if not tela:
            acao_tela_comecar = self.__tela_inicial.comecar(e_vendedor=self.__vendedor)
            tela = acao_tela_comecar["prox_tela"]

        if (tela == "LOGIN_ANUNCIANTE"):
            pass
            # tela login anunciante
        if (tela == "CADASTRO_DE_CURSO"):
            return self.cadastrar_curso()

        if (tela == "LOGIN_VENDEDOR"):
            return self.login_vendedor()
            # tela login vendedor
        if (tela == "CADASTRO_VENDEDOR"):
            return self.cadastrar_vendedor()
            # tela cadastro vendedor

        if tela == "PERFIL_VENDEDOR":
            return self.ver_perfil_vendedor()

        if tela == "LOGOUT":
            self.__vendedor = None
            self.__anunciante = None
            self.__esta_logado = False
            return

        if tela == "SAIR":
            return "SAIR"

    def cadastrar_curso(self):
        acao_tela_curso = self.__controlador_curso.abrir_tela_curso()
        if (acao_tela_curso["result"]):
            self.__controlador_curso.cadastrar_curso(**acao_tela_curso["result"])

    def cadastrar_vendedor(self):
        acao_tela_vendedor = self.__controlador_vendedor.abrir_tela_vendedor()
        if acao_tela_vendedor["result"]:
            self.__controlador_vendedor.cadastrar_vendedor(**acao_tela_vendedor["result"])

    def login_vendedor(self):
        acao_tela_login = self.__controlador_vendedor.abrir_tela_login()
        if acao_tela_login["result"]:
            self.__vendedor = acao_tela_login["result"]
            self.__esta_logado = True
