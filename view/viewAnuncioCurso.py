import PySimpleGUI as sg
from .view import View


class ViewAnuncioCurso(View):

    def __init__(self):
        self.__layout = [
            [sg.Text("Anúncio de Curso")],
            [sg.Button("Voltar ao menu")]
        ]

    def rodar(self, window):
        while True:
            event, values = window.read()
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar(view=window)

    def comecar(self):
        window = sg.Window("Anúncio de Curso", layout=self.__layout, element_justification='c').Finalize()
        window.Element("empty_field").Update(visible=False)
        result = self.rodar(window)
        window.close()
        return result
