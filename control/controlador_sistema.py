from view.viewCadastroVendedor import ViewCadastroVendedor
from control.controladorCadastro import ControladorCadastro


class ControladorSistema:

    def __init__(self):
        # atributos controlador sistema
        self.__controlador_cadastro = ControladorCadastro()

    def inicia():
        # Inicia sistema
        pass

    def cadastrar_vendedor(self):
        dados = ViewCadastroVendedor().comecar()
        return self.__controlador_cadastro.cadastrar_vendedor(**dados)
