import PySimpleGUI as sg
from .view import View


class ViewAtualizaCurso(View):

    def __init__(self):
        pass

    def rodar(self, window, erro):
        if erro:
            window.Element("invalid_field").Update(
                f"Campo inválido: {erro}", visible=True)
        while True:
            event, values = window.read()
            if event == "Enviar" or "Apagar Curso":
                window.Element("invalid_field").Update(visible=False)
                values["apagar"] = True

                return self.voltar(result=values)
            if event == "Voltar" or event == sg.WIN_CLOSED:
                return self.voltar(view=window)

    def comecar(self, erro=None, **kwargs):
        layout = [
            [sg.Text("Atualização de Curso")],
            [sg.Text("", size=(50, 2), key="invalid_field", visible=False)],
            [sg.Text("Nome do Curso", size=(20, 1)),
             sg.Input(key="nome_curso", default_text=kwargs.setdefault("nome_curso"), readonly=True)],
            [sg.Text("Link do Curso", size=(20, 1)),
             sg.Input(key="link_curso", default_text=kwargs.setdefault("link_curso"))],
            [sg.Text("Preço do Curso", size=(20, 1)),
             sg.Input(key="preco_curso", default_text=kwargs.setdefault("preco_curso"))],
            [sg.Submit("Enviar")],
            [sg.Button("Voltar")],
            [sg.Button("Apagar Curso")]
        ]
        window = sg.Window("Atualização de Curso", layout=layout,
                           element_justification='c').Finalize()
        result = self.rodar(window, erro)
        window.close()
        return result
