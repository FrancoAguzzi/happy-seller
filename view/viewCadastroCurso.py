import PySimpleGUI as sg
from .view import View


class ViewCadastroCurso(View):

    def __init__(self):
        pass

    def rodar(self, window):
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
                    return self.voltar(result=values)
            if event == "Voltar" or event == sg.WIN_CLOSED:
                return self.voltar(view=window)

    def comecar(self):
        layout = [
            [sg.Text("Cadastro de Curso")],
            [sg.Text("Nome do Curso", size=(20, 1)),
             sg.Input(key="nome_curso")],
            [sg.Text("Link do Curso", size=(20, 1)),
             sg.Input(key="link_curso")],
            [sg.Text("Preço do Curso", size=(20, 1)),
             sg.Input(key="preco_curso")],
            [sg.Text("Preencha todos os campos", key="empty_field")],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar")]
        ]
        window = sg.Window("Cadastro de Curso", layout=layout,
                           element_justification='c').Finalize()
        window.Element("empty_field").Update(visible=False)
        result = self.rodar(window)
        window.close()
        return result
