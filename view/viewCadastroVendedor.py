import PySimpleGUI as sg
from .view import View


class ViewCadastroVendedor(View):

    def rodar(self, window, verificacoes):
        while True:
            event, values = window.read()
            if event == "Enviar":
                window.Element("invalid_field").Update(visible=False)
                window.Element("pass_not_equal").Update(visible=False)
                window.Element("empty_field").Update(visible=False)

                if self.tem_valores_vazios(values):
                    window.Element("empty_field").Update(visible=True)
                    continue

                if values["senha"] != values["confirm_pass"]:
                    window.Element("pass_not_equal").Update(visible=True)
                    continue

                campo_invalido = self.identificar_campos_invalidos(verificacoes, values)
                if campo_invalido:
                    window.Element("invalid_field").Update(f"{campo_invalido[0]} invalido: {campo_invalido[1]}", visible=True)
                    continue

                values.pop("confirm_pass")
                return self.voltar(result=values)
                
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self, verificacoes=None):
        layout = [
            [sg.Text("Cadastro de vendedor")],
            [sg.Text("", size=(50, 2), key="invalid_field", visible=False)],
            [sg.Text("Preencha todos os campos", key="empty_field", visible=False)],
            [sg.Text("Nome", size=(20, 1)), sg.Input(key="nome")],
            [sg.Text("CPF", size=(20, 1)), sg.Input(key="cpf")],
            [sg.Text("Conta Bancaria", size=(20, 1)), sg.Input(key="conta_bancaria")],
            [sg.Text("CNPJ", size=(20, 1)), sg.Input(key="cnpj")],
            [sg.Text("Senhas nao batem", key="pass_not_equal", visible=False)],
            [sg.Text("Senha", size=(20, 1)), sg.Input(key="senha", password_char="*")],
            [sg.Text("Confirmar Senha", size=(20, 1)), sg.Input(key="confirm_pass", password_char="*")],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar ao menu")]
        ]

        window = sg.Window("Cadastro de vendedor", layout=layout, element_justification='c').Finalize()
        result = self.rodar(window, verificacoes or {})
        window.close()
        return result
