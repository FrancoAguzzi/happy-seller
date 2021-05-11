import datetime

from view.viewTelaInicial import ViewTelaInicial
from control.controladorCurso import ControladorCurso
from control.controladorVendedor import ControladorVendedor
from control.controladorAnunciante import ControladorAnunciante
from control.controladorPlantao import ControladorPlantao
from control.controladorAnuncio import ControladorAnuncio
from model.vendedor import Vendedor


class ControladorSistema:

    def __init__(self):
        # atributos controlador sistema
        self.__tela_inicial = ViewTelaInicial()
        self.__controlador_curso = ControladorCurso()
        self.__controlador_vendedor = ControladorVendedor()
        self.__controlador_anunciante = ControladorAnunciante()
        self.__controlador_plantao = ControladorPlantao()
        self.__controlador_anuncio = ControladorAnuncio()

        self.__vendedor = None
        self.__anunciante = None
        self.__esta_logado = False

    def inicia(self, tela=None):
        if not tela:
            acao_tela_comecar = self.__tela_inicial.comecar(
                e_vendedor=self.__vendedor, e_anunciante=self.__anunciante)
            tela = acao_tela_comecar["prox_tela"]

        if tela == "LOGOUT" and isinstance(self.__vendedor, Vendedor):
            self.ver_tela_saldo_sera_debitado(self.__vendedor)
            self.__vendedor = None

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
        if tela == "SALDO_VENDEDOR":
            return self.ver_saldo_vendedor()
        if tela == "PLANTAO":
            return self.ver_plantao()

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
        if acao_tela_curso["prox_tela"]:
            return acao_tela_curso["prox_tela"]

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

    def ver_saldo_vendedor(self):
        self.__controlador_vendedor.abrir_tela_saldo(
            self.__vendedor)

    def ver_tela_saldo_sera_debitado(self, vendedor):
        return self.__controlador_vendedor.abrir_tela_saldo_sera_debitado(vendedor)

    def ver_plantao(self):
        tempo = None
        anuncio = None
        while True:
            voltar = False
            anuncio, tempo = self.__controlador_anuncio.pegar_proximo_anuncio(
                anuncio=anuncio,
                tempo_atual=datetime.datetime.now(),
                tempo_anterior=tempo
            )

            acao_tela_controlar_plantao = self.__controlador_plantao.abrir_tela_controlar_plantao(anuncio)

            if acao_tela_controlar_plantao.get("prox_tela", False) == "vender_curso" and anuncio:
                while True and not voltar:
                    acao_tela_vender_curso = self.__controlador_plantao.abrir_tela_temp()

                    if acao_tela_vender_curso["result"].get("acao") == "vender_curso":
                        self.__vendedor = (
                            self.__controlador_vendedor
                                .vender_curso(acao_tela_vender_curso["result"]["venda"], self.__vendedor)
                        )

                    if datetime.datetime.now() > tempo + datetime.timedelta(minutes=int(anuncio.tempo_divulgacao) / 10):
                        voltar = True

                    if acao_tela_vender_curso.get("prox_tela", False) == "MENU":
                        return

            if acao_tela_controlar_plantao["result"].get("acao") == "pausar":
                inicio = datetime.datetime.now()
                self.__controlador_plantao.abrir_tela_controlar_plantao(pausado=True)
                fim = datetime.datetime.now()
                self.__vendedor = (
                    self.__controlador_vendedor
                        .descontar_tempo((fim - inicio).total_seconds(), self.__vendedor)
                )

            if acao_tela_controlar_plantao.get("prox_tela", False) == "MENU":
                return
