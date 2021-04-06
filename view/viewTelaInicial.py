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
            if event == "Ver perfil":
                return self.voltar("PERFIL_VENDEDOR")
            if event == "Sair":
                return self.voltar("LOGOUT")
            if event == sg.WIN_CLOSED:
                return self.voltar("SAIR")

    def comecar(self, e_vendedor=False):
        layout = [
            [sg.Text("Happy Seller")]
        ]
        if not e_vendedor:
            layout.extend([
                [sg.Button("Login Anunciante")],
                [sg.Button("Cadastro de Curso")],
                [sg.Button("Login Vendedor")],
                [sg.Button("Cadastro Vendedor")]
            ])
        else:
            layout.extend([
                [sg.Button("Ver perfil")],
                [sg.Button("Sair")]
            ])

        window = sg.Window("Happy Seller", layout=layout, element_justification='c').Finalize()
        result = self.rodar(window)
        window.close()
        return result
