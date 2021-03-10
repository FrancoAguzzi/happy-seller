from view.viewCadastroVendedor import ViewCadastroVendedor
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

    def inicia(self):
        comecar = self.__tela_inicial.comecar()
        if (comecar["prox_tela"] == "LOGIN_ANUNCIANTE"):
            pass
            # tela login anunciante
        if (comecar["prox_tela"] == "CADASTRO_DE_CURSO"):
            return self.cadastrar_curso()

        if (comecar["prox_tela"] == "ANUNCIAR_CURSO"):
            # cpf_anunciante = comecar["result"]["cpf_anunciante"]
            cpf_anunciante = 12345678909
            return self.anunciar_curso(cpf_anunciante)

        if (comecar["prox_tela"] == "LOGIN_VENDEDOR"):
            pass
            # tela login vendedor
        if (comecar["prox_tela"] == "CADASTRO_VENDEDOR"):
            return self.cadastrar_vendedor()
            # tela cadastro vendedor

        if comecar["prox_tela"] == "SAIR":
            return "SAIR"

    def cadastrar_curso(self):
        acao_tela_curso = self.__controlador_curso.abrir_tela_curso()
        if (acao_tela_curso["result"]):
            self.__controlador_curso.cadastrar_curso(**acao_tela_curso["result"])

    def cadastrar_vendedor(self):
        acao_tela_vendedor = self.__controlador_vendedor.abrir_tela_vendedor()
        if acao_tela_vendedor["result"]:
            self.__controlador_vendedor.cadastrar_vendedor(**acao_tela_vendedor["result"])
    
    def anunciar_curso(self, cpf_anunciante):
        acao_tela_anunciar_curso = self \
            .__controlador_curso \
            .abrir_tela_anunciar_curso(cpf_anunciante)
        if acao_tela_anunciar_curso["result"]:
            self.__controlador_curso.anunciar_curso(acao_tela_anunciar_curso["result"])
