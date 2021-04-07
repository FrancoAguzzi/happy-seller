from model.anunciante import Anunciante
from dao.daoAnunciante import DaoAnunciante
from view.viewCadastroAnunciante import ViewCadastroAnunciante
from view.viewLoginAnunciante import ViewLoginAnunciante
from view.viewAnuncianteLogado import ViewAnuncianteLogado


class ControladorAnunciante():
    def __init__(self):
        self.__dao_anunciante = DaoAnunciante("anunciantes.csv")
        self.__tela_cadastro_anunciante = ViewCadastroAnunciante()
        self.__tela_login_anunciante = ViewLoginAnunciante()
        self.__tela_anunciante_logado = ViewAnuncianteLogado()

    def cadastrar_anunciante(self, nome, cpf, numero_cartao_credito, cvv_cartao_credito, senha, cursos_cadastrados = []):
        anunciante = Anunciante(nome, cpf, numero_cartao_credito, cvv_cartao_credito, senha, cursos_cadastrados)
        return self.__dao_anunciante.cadastrar_anunciante(anunciante)

    def abrir_tela_anunciante(self):
        erro = None
        kwargs = {}
        while True:
            result = self.__tela_cadastro_anunciante.comecar(erro=erro, **kwargs)
            if result["result"]:
                e_valido, erro = self.validar_dados_cadastro(**result["result"])
                if not e_valido:
                    kwargs = result["result"]
                    continue
                else:
                    result["result"].pop("confirmacao")
                    self.cadastrar_anunciante(**result["result"])
            return result


    def validar_dados_cadastro(self, nome, cpf, numero_cartao_credito, cvv_cartao_credito, senha, confirmacao):
        def pegar_campo_vazio():
            campos = [
                (nome, "Nome"),
                (cpf, "CPF"),
                (numero_cartao_credito, "Número do Cartão de Crédito"),
                (cvv_cartao_credito, "CVV do Cartão de Crédito"),
                (senha, "Senha"),
                (confirmacao, "Confirmação de senha")
            ]

            for campo, _nome in campos:
                if not campo:
                    return f"'{_nome}' está vazio"
        
        campo_vazio = pegar_campo_vazio()

        verificacoes = [
            (lambda: not campo_vazio, campo_vazio),
        
            (lambda: senha == confirmacao, "As senhas não batem"),

            (lambda: nome.replace(" ", "").isalpha(), "Nome deve conter apenas letras"),

            (lambda: len(cpf) == 11, "O CPF deve ter 11 dígitos"),
            (lambda: cpf.isdecimal(), "O CPF deve conter apenas números"),
            (lambda: not self.__dao_anunciante.existe_cpf(cpf), "CPF já existe"),
            
            (lambda: len(numero_cartao_credito) >= 13 and len(numero_cartao_credito) <= 16, "O número do cartão de crédito deve ter de 13 à 16 dígitos"),
            (lambda: numero_cartao_credito.isdecimal(), "O número do cartão de crédito deve conter apenas números"),

            (lambda: len(cvv_cartao_credito) >= 3 and len(cvv_cartao_credito) <= 4, "O CVV do cartão de crédito deve ter de 3 à 4 dígitos"),
            (lambda: cvv_cartao_credito.isdecimal(), "O CVV do cartão de crédito deve conter apenas números")
        ]

        for e_valido, erro in verificacoes:
            if not e_valido():
                return (False, erro)
        return (True, None)


    def validar_dados_login(self, cpf, senha):
        def pegar_campo_vazio():
            campos = [
                (cpf, "CPF"),
                (senha, "Senha")
            ]

            for campo, _nome in campos:
                if not campo:
                    return f"'{_nome}' está vazio"
        
        campo_vazio = pegar_campo_vazio()
        verificacoes = [
            (lambda: not campo_vazio, campo_vazio),
            (lambda: len(cpf) == 11, "CPF deve ter 11 dígitos"),
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
            dados = self.__tela_login_anunciante.comecar(erro, **kwargs)
            if not dados["result"]:
                return dados

            e_valido, erro = self.validar_dados_login(**dados["result"])
            if not e_valido:
                kwargs = dados["result"]
                continue

            anunciante = self.__dao_anunciante.pegar_anunciante(**dados["result"])
            if not anunciante:
                erro = "CPF e/ou senha não encontrado(s)"
                kwargs = dados["result"]
                continue

            return self.abrir_anunciante_logado()

    def abrir_anunciante_logado(self):
        erro = None
        kwargs = {}
        while True:
            dados = self.__tela_anunciante_logado.comecar(erro, **kwargs)

            if not dados["result"]:
                return dados

            e_valido, erro = self.validar_dados_login(**dados["result"])
            if not e_valido:
                kwargs = dados["result"]
                continue
            
            return dados["prox_tela"]
