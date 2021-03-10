import PySimpleGUI as sg
from .view import View

class ViewTelaInicial(View):
    
    def rodar(self, window):
        while True:
            event, values = window.read()
            if event == "Login Anunciante":
                return self.voltar('LOGIN_ANUNCIANTE')
            if event == "Cadastro de Curso":
                return self.voltar('CADASTRO_DE_CURSO')
            if event == "Login Vendedor":
                return self.voltar('LOGIN_VENDEDOR')
            if event == "Cadastro Vendedor":
                return self.voltar('CADASTRO_VENDEDOR')
            if event == sg.WIN_CLOSED:
                return self.voltar("SAIR")

    def comecar(self):
        layout = [
            [sg.Text("Happy Seller")],
            [sg.Button("Login Anunciante")],
            [sg.Button("Cadastro de Curso")],
            [sg.Button("Login Vendedor")],
            [sg.Button("Cadastro Vendedor")]
        ]
        window = sg.Window("Happy Seller", layout=layout, element_justification='c').Finalize()
        result = self.rodar(window)
        window.close()
        return result