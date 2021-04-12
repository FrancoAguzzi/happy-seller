import PySimpleGUI as sg
from .view import View


class ViewTelaInicial(View):

    def rodar(self, window, erro):
        while True:
            event, values = window.read()
            # Menu
            if event == "Login Anunciante":
                return self.voltar('LOGIN_ANUNCIANTE')
            if event == "Cadastro Anunciante":
                return self.voltar('CADASTRO_ANUNCIANTE')
            if event == "Login Vendedor":
                return self.voltar('LOGIN_VENDEDOR')
            # Vendedor
            if event == "Cadastro Vendedor":
                return self.voltar('CADASTRO_VENDEDOR')
            if event == "Ver perfil":
                return self.voltar("PERFIL_VENDEDOR")
            if event == "Ver saldo":
                return self.voltar("SALDO_VENDEDOR")
            # Anunciante
            if event == "Cadastrar curso":
                return self.voltar('CADASTRO_DE_CURSO')
            if event == "Anunciar curso":
                return self.voltar('ANUNCIO_DE_CURSO')
            # Controle
            if event == "Sair":
                return self.voltar("LOGOUT")
            if event == sg.WIN_CLOSED:
                return self.voltar("SAIR")

    def comecar(self, erro=None, **kwargs):
        layout = [
            [sg.Text("Happy Seller")]
        ]
        if kwargs.get("e_vendedor", True):
            layout.extend([
                [sg.Button("Ver perfil")],
                [sg.Button("Ver saldo")],
                [sg.Button("Sair")]
            ])
        elif kwargs.get("e_anunciante", True):
            layout.extend([
                [sg.Button("Cadastrar curso")],
                [sg.Button("Anunciar curso")],
                [sg.Button("Sair")]
            ])
        else:
            layout.extend([
                [sg.Button("Login Anunciante")],
                [sg.Button("Cadastro Anunciante")],
                [sg.Button("Login Vendedor")],
                [sg.Button("Cadastro Vendedor")]
            ])

        window = sg.Window("Happy Seller", layout=layout,
                           element_justification='c').Finalize()
        result = self.rodar(window, erro)
        window.close()
        return result
