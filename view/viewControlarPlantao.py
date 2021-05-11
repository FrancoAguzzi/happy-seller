import PySimpleGUI as sg
from .view import View


class ViewControlarPlantao(View):

    def rodar(self, window, erro):
        while True:
            event, values = window.read()
            if event == "Vender Curso":
                return self.voltar(prox_tela="vender_curso")

            elif event == "Pausar vendas":
                return self.voltar(result={"acao": "pausar"})

            elif event == "Retornar":
                return self.voltar(result={"acao": "retornar"})

            if event == "Voltar" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self, erro=None, **kwargs):
        layout = []

        if kwargs.get("pausado"):
            layout.extend([
                [sg.Button("Retornar")]
            ])
        else:
            layout.extend([
                [sg.Text("Curso Atual")],
                [sg.Text("", size=(50, 2), key="curso_atual", visible=False)],
                [sg.Button("Vender Curso", disabled=kwargs.get("pausado"))],
                [sg.Button("Pausar vendas")],
                [sg.Button("Voltar", disabled=kwargs.get("pausado"))]
            ])

        window = sg.Window("Controlar Plantão", layout=layout, element_justification='c').Finalize()

        if not kwargs.get("pausado"):
            layout.extend([
                [sg.Button("Retornar")]
            ])
            if kwargs.get("anuncio_atual", False):
                anuncio: dict = kwargs.get("anuncio_atual")
                nome_curso = anuncio.curso.nome_curso
                window.Element("curso_atual").Update(f"Curso Atual: {nome_curso}", visible=True)
            else:
                window.Element("curso_atual").Update(f"Nenhum Curso Para Vender", visible=True)

        result = self.rodar(window, erro)
        window.close()

        return result
