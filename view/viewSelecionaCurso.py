import PySimpleGUI as sg
from .view import View


class ViewSelecionaCurso(View):

    def __init__(self, cursos):
        self.__cursos = cursos

    def rodar(self, window, erro):
        if erro:
            window.Element("invalid_field").Update(
                f"Campo inválido: {erro}", visible=True)
        while True:
            event, values = window.read()

            if event == "Selecionar":
                return self.voltar(result=values)

            if event == "Voltar ao Menu" or event == sg.WIN_CLOSED:
                return self.voltar(view=window)

    def comecar(self, erro=None, **kwargs):
        layout = [
            [sg.Text("Anunciar Curso")],
            [sg.Text("", size=(50, 2), key="invalid_field", visible=False)],
            [sg.Text("Cursos Disponíveis")],
            [sg.Column([
                *[[sg.Radio(curso.nome_curso, group_id="curso_radio", key="nomeCurso." + curso.nome_curso), ] for curso in self.__cursos]
            ], size=(150, 150), scrollable=True)],
            [sg.Text("Preço Base R$ 500,00 por 10 min.")],
            [sg.Text("Comprar mais Tempo", size=(20, 1))],
            [
                sg.Radio("10 min.", group_id="tempo_radio", key="extra_dez"),
                sg.Radio("20 min.", group_id="tempo_radio", key="extra_vinte")
            ],
            [sg.Text(f"Anuncios na frente: {self.__anuncios_frente}")],
            [sg.Text("Pular Cursos?")],
            [sg.Button("Sim")],
            [
                sg.Text("Quantidade", size=(10, 1), key="pular_cursos"),
                sg.Input(key="pular_qtd")
            ],
            [sg.Button("Calcular Valor Final")],
            [sg.Listbox(values=[], key="valor_final_list", size=(20, 1))],
            [sg.Submit("Comprar")],
            [sg.Button("Voltar ao Menu")]
        ]

        window = sg.Window("Anunciar Curso", layout=layout,
                           element_justification='c').Finalize()

        window.Element("pular_cursos").Update(visible=False)
        window.Element("pular_qtd").Update(visible=False)
        window.Element("valor_final_list").Update(visible=False)

        result = self.rodar(window, erro, valor_final)
        window.close()
        return result
