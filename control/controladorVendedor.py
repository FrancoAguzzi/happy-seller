from model.vendedor import Vendedor
from dao.daoVendedor import DaoVendedor
from view.viewCadastroVendedor import ViewCadastroVendedor
from view.viewLoginVendedor import ViewLoginVendedor


class ControladorVendedor():
    def __init__(self):
        self.__dao_vendedor = DaoVendedor("vendedores.csv")
        self.__tela_cadastro_vendedor = ViewCadastroVendedor()
        self.__tela_login_vendedor = ViewLoginVendedor()

    def cadastrar_vendedor(self, nome, cpf, conta_bancaria, cnpj, senha):
        vendedor = Vendedor(nome, cpf, conta_bancaria, cnpj, senha)
        return self.__dao_vendedor.cadastrar_vendedor(vendedor)

    def abrir_tela_vendedor(self):
        erro = None
        kwargs = {}
        while True:
            result = self.__tela_cadastro_vendedor.comecar(erro=erro, **kwargs)
            if result["result"]:
                e_valido, erro = self.validar_dados_cadastro(**result["result"])
                if not e_valido:
                    kwargs = result["result"]
                    continue
                else:
                    result["result"].pop("confirmacao")
            return result


    def validar_dados_cadastro(self, nome, cpf, conta_bancaria, cnpj, senha, confirmacao):
        def pegar_campo_vazio():
            campos = [
                (nome, "nome"),
                (cpf, "cpf"),
                (conta_bancaria, "conta_bancaria"),
                (cnpj, "cnpj"),
                (senha, "senha"),
                (confirmacao, "confirmacao de senha")
            ]

            for campo, _nome in campos:
                if not campo:
                    return f"{_nome} esta vazio"
        
        campo_vazio = pegar_campo_vazio()

        verificacoes = [
            (lambda: not campo_vazio, campo_vazio),
        
            (lambda: senha == confirmacao, "As senhas nao batem"),

            (lambda: conta_bancaria.isdecimal(), "A conta deve conter apenas numeros"),

            (lambda: len(cnpj) == 14, "O CNPJ deve ter 11 digitos"),
            (lambda: cnpj.isdecimal(), "O CNPJ deve conter apenas numeros"),
            (lambda: not self.__dao_vendedor.existe_cnpj(cnpj), "CNPJ ja existe"),

            (lambda: len(cpf) == 11, "O CPF deve ter 11 digitos"),
            (lambda: cpf.isdecimal(), "O CPF deve conter apenas numeros"),
            (lambda: not self.__dao_vendedor.existe_cpf(cpf), "CPF ja existe")
        ]

        for e_valido, erro in verificacoes:
            if not e_valido():
                return (False, erro)
        return (True, None)


    def validar_dados_login(self, cnpj, senha):
        def pegar_campo_vazio():
            campos = [
                (cnpj, "cnpj"),
                (senha, "senha")
            ]

            for campo, _nome in campos:
                if not campo:
                    return f"{_nome} esta vazio"
        
        campo_vazio = pegar_campo_vazio()
        verificacoes = [
            (lambda: not campo_vazio, campo_vazio),
            (lambda: len(cnpj) == 14, "Tamanho do cnpj deve ser 14"),
            (lambda: cnpj.isdecimal(), "CNPJ so pode conter numeros")
        ]

        for e_valido, erro in verificacoes:
            if not e_valido():
                return (False, erro)
        
        return (True, None)


    def abrir_tela_login(self):
        erro = None
        kwargs = {}
        while True:
            dados = self.__tela_login_vendedor.comecar(erro, **kwargs)
            if not dados["result"]:
                return dados

            e_valido, erro = self.validar_dados_login(**dados["result"])
            if not e_valido:
                kwargs = dados["result"]
                continue

            vendedor = self.__dao_vendedor.pegar_vendedor(**dados["result"])
            if not vendedor:
                erro = "CNPJ ou senha nao encontrados"
                kwargs = dados["result"]
                continue

            return { "prox_tela": "MENU", "result": vendedor }
