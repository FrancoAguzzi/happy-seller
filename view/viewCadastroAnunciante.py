import PySimpleGUI as sg
from .view import View


class ViewCadastroAnunciante(View):

    def rodar(self, window, erro):
        if erro:
            window.Element("invalid_field").Update(f"Campo inválido: {erro}", visible=True)
        while True:
            event, values = window.read()
            if event == "Enviar":
                window.Element("invalid_field").Update(visible=False)

                return self.voltar(result=values)
                
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()


    def comecar(self, erro=None, **kwargs):
        layout = [
            [sg.Text("Cadastro de anunciante")],
            [sg.Text("", size=(50, 2), key="invalid_field", visible=False)],
            [sg.Text("Nome", size=(20, 1)), sg.Input(key="nome", default_text=kwargs.setdefault("nome", ""))],
            [sg.Text("CPF", size=(20, 1)), sg.Input(key="cpf", default_text=kwargs.setdefault("cpf", ""))],
            [sg.Text("Número do Cartão de Crédito", size=(20, 1)), sg.Input(key="numero_cartao_credito", default_text=kwargs.setdefault("numero_cartao_credito", ""))],
            [sg.Text("CVV do Cartão de Crédito", size=(20, 1)), sg.Input(key="cvv_cartao_credito", default_text=kwargs.setdefault("cvv_cartao_credito", ""))],
            [sg.Text("Senha", size=(20, 1)), sg.Input(key="senha", password_char="*", default_text=kwargs.setdefault("senha", ""))],
            [sg.Text("Confirmar Senha", size=(20, 1)), sg.Input(key="confirmacao", password_char="*", default_text=kwargs.setdefault("confirmacao", ""))],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar ao menu")]
        ]

        window = sg.Window("Cadastro de vendedor", layout=layout, element_justification='c').Finalize()
        result = self.rodar(window, erro)
        window.close()
        return result
