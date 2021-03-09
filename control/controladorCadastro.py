from model.vendedor import Vendedor
from dao.daoVendedor import DaoVendedor


class ControladorCadastro():
    def __init__(self):
        self.__dao_vendedor = DaoVendedor("vendedores.csv")

    def cadastrar_vendedor(self, nome, cpf, acc, password):
        vendedor = Vendedor(nome, cpf, acc, password)
        return self.__dao_vendedor.cadastrar_vendedor(vendedor)
    