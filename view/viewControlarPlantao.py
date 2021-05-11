import PySimpleGUI as sg
from .view import View


class ViewControlarPlantao(View):

    def rodar(self, window, erro):
        while True:
            event, values = window.read()
            if event == "Vender Curso":
                return self.voltar(prox_tela="vender_curso")

            if event == "Voltar" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self, erro=None, **kwargs):
        layout = []
        layout.extend([
            [sg.Text("Curso Atual")],
            [sg.Text("", size=(50, 2), key="curso_atual", visible=False)],
            [sg.Button("Vender Curso", disabled=kwargs.get("anuncio_atual"))],
            [sg.Button("Voltar")]
        ])

        window = sg.Window("Controlar Plantão", layout=layout, element_justification='c').Finalize()

        if kwargs.get("anuncio_atual", False):
            anuncio: dict = kwargs.get("anuncio_atual")
            nome_curso = anuncio.curso.nome_curso
            window.Element("curso_atual").Update(f"Curso Atual: {nome_curso}", visible=True)
        else:
            window.Element("curso_atual").Update(f"Nenhum Curso Para Vender", visible=True)

        result = self.rodar(window, erro)
        window.close()

        return result
