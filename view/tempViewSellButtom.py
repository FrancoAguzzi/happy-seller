import PySimpleGUI as sg
from .view import View


class TempViewSellButtom(View):

    def rodar(self, window, erro):
        while True:
            event, values = window.read()
            if event == "Vender curso":
                return self.voltar(prox_tela="", result={"acao": "vender_curso", "venda": {"valor": 10}})

            elif event == "Pausar vendas":
                return self.voltar(result={"acao": "pausar"})

            elif event == "Retornar":
                return self.voltar(result={"acao": "retornar"})

            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self, erro=None, **kwargs):
        layout = []

        if kwargs.get("nome_curso", False):
            layout.extend([
                [sg.Text("", size=(50, 2), key="nome_curso", visible=False)],
            ])

        if kwargs.get("pausado"):
            layout.extend([
                [sg.Button("Retornar")]
            ])
        else:
            layout.extend([
                [sg.Text("Comprador Atual")],
                [sg.Text(kwargs.get("cliente")[0])],
                [sg.Text(kwargs.get("cliente")[1])],
                [sg.Text(kwargs.get("cliente")[2])],
                [sg.Button("Pausar vendas")]
            ])
        layout.extend([
            [sg.Button("Vender curso", disabled=kwargs.get("pausado"))],
            [sg.Button("Voltar ao menu", disabled=kwargs.get("pausado"))]
        ])

        window = sg.Window("Vender curso", layout=layout, element_justification='c').Finalize()

        if kwargs.get("nome_curso", False):
            nome_curso = kwargs.get("nome_curso")
            window.Element("nome_curso").Update(f"Curso Atual: {nome_curso}", visible=True)

        result = self.rodar(window, erro)
        window.close()
        return result
