import PySimpleGUI as sg
from .view import View


class ViewPerfilVendedor(View):

    def rodar(self, window, erro):
        if erro:
            window.Element("invalid_field").Update(f"Campo inválido: {erro}", visible=True)
        while True:
            event, values = window.read()
            if event == "Enviar" or "Apagar conta":
                window.Element("invalid_field").Update(visible=False)
                values["apagar"] = True

                return self.voltar(result=values)
                
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()


    def comecar(self, erro=None, **kwargs):
        layout = [
            [sg.Text("Perfil")],
            [sg.Text("", size=(50, 2), key="invalid_field", visible=False)],
            [sg.Text("Nome", size=(20, 1)), sg.Input(key="nome", default_text=kwargs.setdefault("nome", ""), readonly=True)],
            [sg.Text("CPF", size=(20, 1)), sg.Input(key="cpf", default_text=kwargs.setdefault("cpf", ""), readonly=True)],
            [sg.Text("Conta Bancaria", size=(20, 1)), sg.Input(key="conta_bancaria", default_text=kwargs.setdefault("conta_bancaria", ""))],
            [sg.Text("CNPJ", size=(20, 1)), sg.Input(key="cnpj", default_text=kwargs.setdefault("cnpj", ""))],
            [sg.Text("Senha antiga", size=(20, 1)), sg.Input(key="senha_antiga", password_char="*")],
            [sg.Text("Senha nova", size=(20, 1)), sg.Input(key="senha_nova", password_char="*")],
            [sg.Text("Confirmar Senha", size=(20, 1)), sg.Input(key="confirmacao", password_char="*")],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar ao menu")],
            [sg.Button("Apagar conta")]
        ]

        window = sg.Window("Cadastro de vendedor", layout=layout, element_justification='c').Finalize()
        result = self.rodar(window, erro)
        window.close()
        return result
