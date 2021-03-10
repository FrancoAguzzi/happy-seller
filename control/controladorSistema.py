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


    def inicia(self):
        comecar = self.__tela_inicial.comecar()
        if (comecar["prox_tela"] == "LOGIN_ANUNCIANTE"):
            pass
            # tela login anunciante
        if (comecar["prox_tela"] == "CADASTRO_DE_CURSO"):
            return self.cadastrar_curso()

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
