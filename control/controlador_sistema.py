from view.viewCadastroVendedor import ViewCadastroVendedor
from view.viewTelaInicial import ViewTelaInicial
from control.controladorCadastro import ControladorCadastro
from control.controladorCadastro import ControladorCadastro

class ControladorSistema:

    def __init__(self):
        # atributos controlador sistema
        self.__tela_inicial = ViewTelaInicial()
        self.__controlador_cadastro = ControladorCadastro()

    def inicia(self):
        comecar = self.__tela_inicial.comecar()
        if (comecar["prox_tela"] == "LOGIN_ANUNCIANTE"):
            pass
            # tela login anunciante
        if (comecar["prox_tela"] == "CADASTRO_DE_CURSO"):
            acao_tela_curso = self.__controlador_cadastro.abrir_tela_curso()
            if (acao_tela_curso["result"]):
                self.__controlador_cadastro.cadastrar_curso(**acao_tela_curso["result"])
        if (comecar["prox_tela"] == "LOGIN_VENDEDOR"):
            pass
            # tela login vendedor
        if (comecar["prox_tela"] == "CADASTRO_VENDEDOR"):
            pass
            # tela cadastro vendedor

    def cadastrar_vendedor(self):
        dados = ViewCadastroVendedor().comecar()
        return self.__controlador_cadastro.cadastrar_vendedor(**dados)
