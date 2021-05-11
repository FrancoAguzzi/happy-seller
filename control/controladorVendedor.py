from model.vendedor import Vendedor
from dao.daoVendedor import DaoVendedor
from view.viewCadastroVendedor import ViewCadastroVendedor
from view.viewLoginVendedor import ViewLoginVendedor
from view.viewPerfilVendedor import ViewPerfilVendedor
from view.viewSaldoVendedor import ViewSaldoVendedor
from view.viewSaldoSeraDebitado import ViewSaldoSeraDebitado


class ControladorVendedor():
    def __init__(self):
        self.__dao_vendedor = DaoVendedor("vendedores.csv")
        self.__tela_cadastro_vendedor = ViewCadastroVendedor()
        self.__tela_login_vendedor = ViewLoginVendedor()
        self.__tela_perfil_vendedor = ViewPerfilVendedor()
        self.__tela_saldo_vendedor = ViewSaldoVendedor()
        self.__tela_saldo_debitado = ViewSaldoSeraDebitado()

    def cadastrar_vendedor(self, nome, cpf, conta_bancaria, cnpj, senha):
        vendedor = Vendedor(nome, cpf, conta_bancaria, cnpj, senha)
        return self.__dao_vendedor.cadastrar_vendedor(vendedor)

    def abrir_tela_vendedor(self):
        erro = None
        kwargs = {}
        while True:
            result = self.__tela_cadastro_vendedor.comecar(erro=erro, **kwargs)
            if result["result"]:
                e_valido, erro = self.validar_dados_cadastro(
                    **result["result"])
                if not e_valido:
                    kwargs = result["result"]
                    continue
                else:
                    result["result"].pop("confirmacao")
                    self.cadastrar_vendedor(**result["result"])
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

            (lambda: senha == confirmacao, "As senhas não batem"),

            (lambda: conta_bancaria.isdecimal(),
             "A conta deve conter apenas números"),

            (lambda: len(cnpj) == 14, "O CNPJ deve ter 14 dígitos"),
            (lambda: cnpj.isdecimal(), "O CNPJ deve conter apenas números"),
            (lambda: not self.__dao_vendedor.existe_cnpj(cnpj), "CNPJ já cadastrado"),

            (lambda: len(cpf) == 11, "O CPF deve ter 11 dígitos"),
            (lambda: cpf.isdecimal(), "O CPF deve conter apenas números"),
            (lambda: not self.__dao_vendedor.existe_cpf(cpf), "CPF já cadastrado")
        ]

        for e_valido, erro in verificacoes:
            if not e_valido():
                return (False, erro)
        return (True, None)

    def validar_dados_login(self, cpf, senha):
        def pegar_campo_vazio():
            campos = [
                (cpf, "cpf"),
                (senha, "senha")
            ]

            for campo, _nome in campos:
                if not campo:
                    return f"{_nome} está vazio"

        campo_vazio = pegar_campo_vazio()
        verificacoes = [
            (lambda: not campo_vazio, campo_vazio),
            (lambda: len(cpf) == 11, "Tamanho do cpf deve ser 11"),
            (lambda: cpf.isdecimal(), "CPF só pode conter números")
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
                erro = "CPF e/ou senha não encontrado(s)"
                kwargs = dados["result"]
                continue

            return {"prox_tela": "MENU", "result": vendedor}

    def abrir_tela_perfil(self, vendedor):
        erro = None
        kwargs = {}
        while True:
            dados = self.__tela_perfil_vendedor.comecar(
                erro, **{k: v for k, v in vendedor.pegar_dados_como_tuplas()}
            )
            if not dados["result"]:
                return dados

            if dados["result"].get("apagar"):
                self.__dao_vendedor.apagar_vendedor(dados["result"]["cpf"])
                return dados

            e_valido, erro = self.validar_dados_perfil(**dados["result"])
            if not e_valido:
                kwargs = dados["result"]
                continue

            if dados["result"]["senha_antiga"]:
                if not self.__dao_vendedor.pegar_vendedor(dados["result"]["cpf"], dados["result"]["senha_antiga"]):
                    erro = "Senha errada"
                    kwargs = dados["result"]
                    continue

            vendedor_atualizado = self.__dao_vendedor.atualizar_vendedor(
                vendedor.cpf,
                conta_bancaria=dados["result"]["conta_bancaria"],
                cnpj=dados["result"]["cnpj"],
                senha=dados["result"]["senha_nova"]
            )

            return {"prox_tela": "MENU", "result": vendedor_atualizado}

    def validar_dados_perfil(self, nome, cpf, conta_bancaria, cnpj, senha_antiga, senha_nova, confirmacao):
        def pegar_campo_vazio():
            campos = [
                (conta_bancaria, "conta_bancaria"),
                (cnpj, "cnpj")
            ]

            if senha_antiga or senha_nova:
                campos.extend([
                    (senha_antiga, "senha antiga"),
                    (senha_nova, "senha nova"),
                    (confirmacao, "confirmacao de senha")
                ])

            for campo, _nome in campos:
                if not campo:
                    return f"{_nome} esta vazio"

        campo_vazio = pegar_campo_vazio()

        verificacoes = [
            (lambda: not campo_vazio, campo_vazio),

            (lambda: senha_nova == confirmacao, "As senhas não batem"),

            (lambda: conta_bancaria.isdecimal(),
             "A conta deve conter apenas números"),

            (lambda: len(cnpj) == 14, "O CNPJ deve ter 14 dígitos"),
            (lambda: cnpj.isdecimal(), "O CNPJ deve conter apenas números")
        ]

        for e_valido, erro in verificacoes:
            if not e_valido():
                return (False, erro)
        return (True, None)

    def calcula_rendimentos(self, vendedor):
        bruto = vendedor.salario_bruto
        horario_cobrado = (vendedor.horas_descansadas_dia - 0.5)
        if horario_cobrado < 0:
            horario_cobrado = 0
        desconto = round(horario_cobrado * 60, 2)
        liquido = bruto - desconto
        return [bruto, liquido, desconto]

    def abrir_tela_saldo(self, vendedor):
        [bruto, liquido, desconto] = self.calcula_rendimentos(vendedor)
        return self.__tela_saldo_vendedor.comecar(bruto=bruto, liquido=liquido, descontado=desconto)

    def abrir_tela_saldo_sera_debitado(self, vendedor):
        [_bruto, liquido, _desconto] = self.calcula_rendimentos(vendedor)
        return self.__tela_saldo_debitado.comecar(liquido=liquido)

    def vender_curso(self, venda, vendedor):
        comissao_venda = vendedor.comissao_base + venda["valor"] * vendedor.comissao_atual
        if vendedor.comissao_atual + 0.005 <= 0.02:
            vendedor.comissao_atual += 0.005
        else:
            vendedor.comissao_atual = 0.02
        vendedor.salario_bruto += comissao_venda

        return vendedor

    def acrescentar_saldo_plantao(self, vendedor, saldo_plantao):
        vendedor.salario_bruto += saldo_plantao
        vendedor.salario_bruto_acumulado_plantao = 0

        return vendedor

    def descontar_tempo(self, segundos, vendedor):
        vendedor.horas_descansadas_dia += segundos / 3600

        return vendedor
