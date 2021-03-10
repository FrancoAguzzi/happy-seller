import PySimpleGUI as sg
from .view import View


class ViewCadastroVendedor(View):

    def rodar(self, window):
        while True:
            event, values = window.read()
            valid = True
            if event == "Enviar":
                if self.tem_valores_vazios(values):
                    window.Element("empty_field").Update(visible=True)

                elif values["password"] != values["confirm_pass"]:
                    window.Element("pass_not_equal").Update(visible=True)

                else:
                    values.pop("confirm_pass")
                    return self.voltar(result=values)
                
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self):
        layout = [
            [sg.Text("Cadastro de vendedor")],
            [sg.Text("Preencha todos os campos", key="empty_field")],
            [sg.Text("Nome", size=(20, 1)), sg.Input(key="nome")],
            [sg.Text("CPF", size=(20, 1)), sg.Input(key="cpf")],
            [sg.Text("Conta Bancaria", size=(20, 1)), sg.Input(key="acc")],
            [sg.Text("Senhas nao batem", key="pass_not_equal")],
            [sg.Text("Senha", size=(20, 1)), sg.Input(key="password", password_char="*")],
            [sg.Text("Confirmar Senha", size=(20, 1)), sg.Input(key="confirm_pass", password_char="*")],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar ao menu")]
        ]

        window = sg.Window("Cadastro de vendedor", layout=layout, element_justification='c').Finalize()
        window.Element("pass_not_equal").Update(visible=False)
        window.Element("empty_field").Update(visible=False)
        result = self.rodar(window)
        window.close()
        return result
