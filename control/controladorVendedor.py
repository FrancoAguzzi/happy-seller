from model.vendedor import Vendedor
from dao.daoVendedor import DaoVendedor
from view.viewCadastroVendedor import ViewCadastroVendedor


class ControladorVendedor():
    def __init__(self):
        self.__dao_vendedor = DaoVendedor("vendedores.csv")
        self.__tela_cadastro_vendedor = ViewCadastroVendedor()

    def cadastrar_vendedor(self, nome, cpf, conta_bancaria, cnpj, senha):
        vendedor = Vendedor(nome, cpf, conta_bancaria, cnpj, senha)
        return self.__dao_vendedor.cadastrar_vendedor(vendedor)

    def abrir_tela_vendedor(self):
        verificacoes = {
            "cpf": (
                lambda cpf: len(cpf) == 11 and cpf.isdecimal() and not self.__dao_vendedor.existe_cpf(cpf),
                "CPF deve ser apenas numeros de tamanho 11 e nao pode estar sendo utilizado"
            ),
            "cnpj": (
                lambda cnpj: len(cnpj) == 14 and cnpj.isdecimal() and not self.__dao_vendedor.existe_cnpj(cnpj),
                "CNPJ deve ser apenas numeros de tamanho 14 e nao pode estar sendo utilizado"
            ),
            "conta_bancaria": (
                lambda acc: acc.isdecimal(),
                "Conta bancaria deve ter apenas digitos"
            )
        }
        return self.__tela_cadastro_vendedor.comecar(verificacoes)
