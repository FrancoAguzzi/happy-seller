import PySimpleGUI as sg
from .view import View


class TempViewSellButtom(View):

    def rodar(self, window, erro):
        while True:
            event, values = window.read()
            if event == "Vender curso":
                return self.voltar(result={"acao": "vender_curso", "venda": {"valor": 10}})
                
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self, erro=None, **kwargs):
        layout = [
            [sg.Button("Vender curso")],
            [sg.Button("Voltar ao menu")]
        ]

        window = sg.Window("Vender curso", layout=layout, element_justification='c').Finalize()
        result = self.rodar(window, erro)
        window.close()
        return result
