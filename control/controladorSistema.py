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

    def inicia(self, tela=None, extra=None):
        if not tela:
            acao_tela_comecar = self.__tela_inicial.comecar(
                e_vendedor=self.__vendedor)
            tela = acao_tela_comecar["prox_tela"]

        # telas anunciante
        if (tela == "LOGIN_ANUNCIANTE"):
            return self.login_anunciante()
        if (tela == "ANUNCIANTE_LOGADO"):
            return self.abrir_anunciante_logado()
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
            # and extra and extra.get("anunciante")
            # extra["anunciante"]
            return self.cadastrar_curso()
        if (tela == "ANUNCIO_DE_CURSO"):
            return self.anunciar_curso()

        if tela == "LOGOUT":
            self.__vendedor = None
            self.__anunciante = None
            self.__esta_logado = False
            return

        if tela == "SAIR":
            return "SAIR"

    # TODO
    # CONSTRUIR A TELA DE LOGIN DE ANUNCIANTE DA FORMA
    # QUE FOI FEITA A TELA DE LOGIN DO VENDEDOR, ASSIM
    # NÃO PRECISARÁ MUDAR MUITO O CÓDIGO PARA RECEBER O
    # ANUNCIANTE NAS TELAS NECESSÁRIAS

    # métodos anunciante
    def cadastrar_anunciante(self):
        acao_tela_anunciante = self.__controlador_anunciante.abrir_tela_anunciante()

    def login_anunciante(self):
        acao_tela_login = self.__controlador_anunciante.abrir_tela_login()
        print(acao_tela_login)
        if acao_tela_login["prox_tela"]:
            return acao_tela_login["prox_tela"]

    def abrir_anunciante_logado(self):
        acao_tela_anunciante = self.__controlador_anunciante.abr
        if acao_tela_anunciante["result"]:
            self.__anunciante = acao_tela_login["result"]

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

    # métodos curso
    def cadastrar_curso(self):
        acao_tela_curso = self.__controlador_anunciante.abrir_tela_cadastrar_curso()()

    def anunciar_curso(self):
        acao_tela_curso = self.__controlador_curso.abrir_anuncio_curso()
        # if (acao_tela_curso["result"]):
        #     self.__controlador_curso.cadastrar_curso(**acao_tela_curso["result"])

    def ver_perfil_vendedor(self):
        acao_tela_perfil = self.__controlador_vendedor.abrir_tela_perfil(
            self.__vendedor)
        if acao_tela_perfil["result"]:
            self.__vendedor = acao_tela_perfil["result"]

        if acao_tela_perfil["result"].get("apagar"):
            self.__vendedor = None
            self.__esta_logado = False
