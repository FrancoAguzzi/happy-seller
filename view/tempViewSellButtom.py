import PySimpleGUI as sg
from .view import View


class TempViewSellButtom(View):

    def rodar(self, window, erro):
        while True:
            event, values = window.read()
            if event == "Vender curso":
                return self.voltar(result={"acao": "vender_curso", "venda": {"valor": 10}})

            elif event == "Pausar vendas":
                return self.voltar(result={"acao": "pausar"})

            elif event == "Retornar":
                return self.voltar(result={"acao": "retornar"})
                
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self, erro=None, **kwargs):
        layout = []
        if kwargs.get("pausado"):
            layout.extend([
                [sg.Button("Retornar")]
            ])
        else:
            layout.extend([
                [sg.Button("Pausar vendas")]
                
            ])
        layout.extend([
            [sg.Button("Vender curso", disabled=kwargs.get("pausado"))],
            [sg.Button("Voltar ao menu", disabled=kwargs.get("pausado"))]
        ])

        window = sg.Window("Vender curso", layout=layout, element_justification='c').Finalize()
        result = self.rodar(window, erro)
        window.close()
        return result
