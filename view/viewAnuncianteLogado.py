import PySimpleGUI as sg
from .view import View


class ViewAnuncianteLogado(View):

    def rodar(self, window, erro):
        if erro:
            window.Element("invalid_field").Update(f"{erro}", visible=True)

        while True:
            event, values = window.read()
            if event == "Cadastrar curso":
                return self.voltar('CADASTRO_DE_CURSO')

            if event == "Anunciar curso":
                return self.voltar('ANUNCIO_DE_CURSO')

            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self, erro=None, **kwargs):
        layout = [
            [sg.Button("Cadastrar curso")],
            [sg.Button("Anunciar curso")],
            [sg.Button("Voltar ao menu")]
        ]

        window = sg.Window("Login de anunciante", layout=layout,
                           element_justification='c').Finalize()
        result = self.rodar(window, erro)
        window.close()
        return result
