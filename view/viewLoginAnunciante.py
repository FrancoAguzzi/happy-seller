import PySimpleGUI as sg
from .view import View


class ViewLoginAnunciante(View):

    def rodar(self, window, erro):
        if erro:
            window.Element("invalid_field").Update(f"{erro}", visible=True)

        while True:
            event, values = window.read()
            if event == "Enviar":
                window.Element("invalid_field").Update(visible=False)

                return self.voltar(result=values)

            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self, erro=None, **kwargs):
        layout = [
            [sg.Text("", size=(50, 2), key="invalid_field", visible=False)],
            [sg.Text("CPF", size=(20, 1)), sg.Input(key="cpf", default_text=kwargs.setdefault("cpf", ""))],
            [sg.Text("Senha", size=(20, 1)), sg.Input(key="senha", password_char="*", default_text=kwargs.setdefault("senha", ""))],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar ao menu")]
        ]

        window = sg.Window("Login de anunciante", layout=layout, element_justification='c').Finalize()
        result = self.rodar(window, erro)
        window.close()
        return result
