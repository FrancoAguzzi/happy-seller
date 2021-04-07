import PySimpleGUI as sg
from .view import View


class ViewCadastroAnunciante(View):

    def __init__(self):
        self.__layout = [
            [sg.Text("Cadastro de Anunciante")],
            [sg.Text("Nome do Anunciante", size=(20, 1)),
             sg.Input(key="nome_anunc")],
            [sg.Text("CPF do Anunciante", size=(20, 1)),
             sg.Input(key="cpf_anunc")],
            [sg.Text("Cartão para cobrança", size=(20, 1)),
             sg.Input(key="ncc")],
            [sg.Text("Código verificador", size=(20, 1)), sg.Input(key="cvv")],
            [sg.Text("Preencha todos os campos", key="empty_field")],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar ao menu")]
        ]

    def rodar(self, window, erro):
        while True:
            event, values = window.read()
            someEmptyField = False
            if event == "Enviar":
                for value in values:
                    if (values[value] == ""):
                        someEmptyField = True
                        window.Element("empty_field").Update(visible=True)
                        break
                if (not someEmptyField):
                    return self.voltar(result=values, view=window)
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar(view=window)

    def comecar(self):
        window = sg.Window("Cadastro de Anunciante",
                           layout=self.__layout, element_justification='c').Finalize()
        window.Element("empty_field").Update(visible=False)
        result = self.rodar(window)
        window.close()
        return result
