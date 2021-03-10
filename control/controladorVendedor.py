from model.vendedor import Vendedor
from dao.daoVendedor import DaoVendedor
from view.viewCadastroVendedor import ViewCadastroVendedor


class ControladorVendedor():
    def __init__(self):
        self.__dao_vendedor = DaoVendedor("vendedores.csv")
        self.__tela_cadastro_vendedor = ViewCadastroVendedor()

    def cadastrar_vendedor(self, nome, cpf, acc, password):
        vendedor = Vendedor(nome, cpf, acc, password)
        return self.__dao_vendedor.cadastrar_vendedor(vendedor)

    def abrir_tela_vendedor(self):
        return self.__tela_cadastro_vendedor.comecar()
