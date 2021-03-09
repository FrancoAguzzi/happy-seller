import PySimpleGUI as sg
from .view import View


class ViewCadastroVendedor(View):

    def __init__(self):
        self.__layout = [
            [sg.Text("Cadastro de vendedor")],
            [sg.Text("Nome", size=(20, 1)), sg.Input(key="nome")],
            [sg.Text("CPF", size=(20, 1)), sg.Input(key="cpf")],
            [sg.Text("Conta Bancaria", size=(20, 1)), sg.Input(key="acc")],
            [sg.Text("Senhas nao batem", key="pass_not_equal")],
            [sg.Text("Senha", size=(20, 1)), sg.Input(key="password", password_char="*")],
            [sg.Text("Confirmar Senha", size=(20, 1)), sg.Input(key="confirm_pass", password_char="*")],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar ao menu")]
        ]

    def rodar(self, window):
        while True:
            event, values = window.read()
            if event == "Enviar":
                if values["password"] == values["confirm_pass"]:
                    return values
                window.Element("pass_not_equal").Update(visible=True)
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                break

    def comecar(self):
        window = sg.Window("Cadastro de vendedor", layout=self.__layout, element_justification='c').Finalize()
        window.Element("pass_not_equal").Update(visible=False)
        result = self.rodar(window)
        window.close()
        result.pop("confirm_pass")
        return result
