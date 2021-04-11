from view.viewTelaInicial import ViewTelaInicial
from control.controladorCurso import ControladorCurso
from control.controladorVendedor import ControladorVendedor
from control.controladorAnunciante import ControladorAnunciante


class ControladorSistema:

    def __init__(self):
        # atributos controlador sistema
        self.__tela_inicial = ViewTelaInicial()
        self.__controlador_curso = ControladorCurso()
        self.__controlador_vendedor = ControladorVendedor()
        self.__controlador_anunciante = ControladorAnunciante()
        self.__vendedor = None
        self.__anunciante = None
        self.__esta_logado = False

    def inicia(self, tela=None):
        if not tela:
            acao_tela_comecar = self.__tela_inicial.comecar(
                e_vendedor=self.__vendedor, e_anunciante=self.__anunciante)
            tela = acao_tela_comecar["prox_tela"]

        if tela == "LOGOUT":
            self.__vendedor = None
            self.__anunciante = None
            self.__esta_logado = False
            return

        if tela == "SAIR":
            return "SAIR"

        # telas anunciante
        if (tela == "LOGIN_ANUNCIANTE"):
            return self.login_anunciante()
        if (tela == "CADASTRO_ANUNCIANTE"):
            return self.cadastrar_anunciante()

        # telas vendedor
        if (tela == "LOGIN_VENDEDOR"):
            return self.login_vendedor()
        if (tela == "CADASTRO_VENDEDOR"):
            return self.cadastrar_vendedor()
        if tela == "PERFIL_VENDEDOR":
            return self.ver_perfil_vendedor()

        #  telas curso
        if (tela == "CADASTRO_DE_CURSO"):
            return self.cadastrar_curso()
        if (tela == "ANUNCIO_DE_CURSO"):
            return self.anunciar_curso()

    # métodos anunciante
    def cadastrar_anunciante(self):
        acao_tela_anunciante = self.__controlador_anunciante.abrir_tela_anunciante()

    def login_anunciante(self):
        acao_tela_login = self.__controlador_anunciante.abrir_tela_login()

        if acao_tela_login["result"]:
            self.__anunciante = acao_tela_login["result"]
            self.__esta_logado = True

    # métodos curso
    def cadastrar_curso(self):
        acao_tela_curso = self.__controlador_anunciante.abrir_tela_cadastrar_curso(
            self.__anunciante)
        if acao_tela_curso["prox_tela"]:
            return acao_tela_curso["prox_tela"]

    def anunciar_curso(self):
        acao_tela_curso = self.__controlador_anunciante.abrir_tela_anunciar_curso(
            self.__anunciante)
        # if (acao_tela_curso["result"]):
        #     self.__controlador_curso.cadastrar_curso(**acao_tela_curso["result"])

    # métodos vendedor
    def cadastrar_vendedor(self):
        acao_tela_vendedor = self.__controlador_vendedor.abrir_tela_vendedor()
        if acao_tela_vendedor["prox_tela"]:
            return acao_tela_vendedor["prox_tela"]

    def login_vendedor(self):
        acao_tela_login = self.__controlador_vendedor.abrir_tela_login()
        if acao_tela_login["result"]:
            self.__vendedor = acao_tela_login["result"]
            self.__esta_logado = True

    def ver_perfil_vendedor(self):
        acao_tela_perfil = self.__controlador_vendedor.abrir_tela_perfil(
            self.__vendedor)
        if acao_tela_perfil["result"]:
            self.__vendedor = acao_tela_perfil["result"]

        if acao_tela_perfil["result"].get("apagar"):
            self.__vendedor = None
            self.__esta_logado = False
