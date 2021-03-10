import PySimpleGUI as sg
from .view import View


class ViewCadastroCurso(View):

    def __init__(self):
        self.__layout = [
            [sg.Text("Cadastro de Curso")],
            [sg.Text("Nome do Anunciante", size=(20, 1)), sg.Input(key="nome_anunc")],
            [sg.Text("CPF do Anunciante", size=(20, 1)), sg.Input(key="cpf_anunc")],
            [sg.Text("Cartão para cobrança", size=(20, 1)), sg.Input(key="ncc")],
            [sg.Text("Código verificador", size=(20, 1)), sg.Input(key="cvv")],
            [sg.Text("Nome do Curso", size=(20, 1)), sg.Input(key="nome_curso")],
            [sg.Text("Link do Curso", size=(20, 1)), sg.Input(key="link_curso")],
            [sg.Text("Preço do Curso", size=(20, 1)), sg.Input(key="preco_curso")],
            [sg.Text("Preencha todos os campos", key="empty_field")],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar ao menu")]
        ]

    def rodar(self, window):
        while True:
            event, values = window.read()
            if event == "Enviar":
                for value in values:
                    if (values[value] != ""):
                        return self.voltar(result = values, view=window)
                    else:
                        window.Element("empty_field").Update(visible=True)
                        break
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar(view=window)

    def comecar(self):
        window = sg.Window("Cadastro de Curso", layout=self.__layout, element_justification='c').Finalize()
        window.Element("empty_field").Update(visible=False)
        result = self.rodar(window)
        window.close()
        return result