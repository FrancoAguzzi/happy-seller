import PySimpleGUI as sg
from .view import View


class ViewSaldoVendedor(View):

    def rodar(self, window, erro):
        while True:
            event, values = window.read()
            if event == "Voltar ao menu" or event == sg.WIN_CLOSED:
                return self.voltar()

    def comecar(self, erro=None, **kwargs):
        layout = [
            [sg.Text("Saldo do Vendedor")],
            [sg.Text("Recebidos Bruto", size=(20, 1)), sg.Input(
                key="bruto", default_text=kwargs.setdefault("bruto", ""), readonly=True)],
            [sg.Text("Recebitos Líquido", size=(20, 1)), sg.Input(
                key="liquido", default_text=kwargs.setdefault("liquido", ""), readonly=True)],
            [sg.Text("Descontado", size=(20, 1)), sg.Input(
                key="descontado", default_text=kwargs.setdefault("descontado", ""), readonly=True)],
            [sg.Button("Voltar ao menu")],
        ]

        window = sg.Window("Saldo do Vendedor", layout=layout,
                           element_justification='c').Finalize()
        result = self.rodar(window, erro)
        window.close()

        return result
