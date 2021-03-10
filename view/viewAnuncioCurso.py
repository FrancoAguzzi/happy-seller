import PySimpleGUI as sg
from .view import View


class ViewAnuncioCurso(View):

    def __init__(self, cursos, anuncios_frente):
        self.__cursos = cursos
        self.__anuncios_frente = anuncios_frente

    def rodar(self, window):
        while True:
            event, values = window.read()
            if event == "Comprar":
                if values["pular_qtd"] and int(values["pular_qtd"]) > self.__anuncios_frente:
                    window.Element("quantidade_maior").Update(visible=True)
                    window.Element("quantidade_menor").Update(visible=False)
                elif values["pular_qtd"] and int(values["pular_qtd"]) < 0:
                    window.Element("quantidade_maior").Update(visible=False)
                    window.Element("quantidade_menor").Update(visible=True)
                else:
                    return self.voltar(view=window, result=values)
            if event == "Sim":
                window.Element("comprar_tempo_extra").Update(visible=True)
                window.Element("pular_qtd").Update(visible=True)
            if event == "Voltar ao Menu" or event == sg.WIN_CLOSED:
                return self.voltar(view=window)

    def comecar(self):
        layout = [
            [sg.Text("Anunciar Curso")],
            [sg.Text("Cursos Disponíveis")],
            [sg.Column([
                *[[sg.Radio(curso["nome"], group_id="curso_radio", key="nomeCurso."+curso["nome"]), ] for curso in self.__cursos]
            ], size=(150, 150))],
            [sg.Text("Preço Base R$ 500,00 por 30 min.")],
            [sg.Text("Comprar mais Tempo", size=(20, 1))],
            [
                sg.Radio("10 min.", group_id="tempo_radio", key="extra_dez"),
                sg.Radio("20 min.", group_id="tempo_radio", key="extra_vinte"),
                sg.Radio("30 min.", group_id="tempo_radio", key="extra_trinta")
            ],
            [sg.Text(f"Anuncios na frente: {self.__anuncios_frente}")],
            [sg.Text("Pular Cursos?")],
            [sg.Button("Sim")],
            [
                sg.Text("Quantidade", size=(10, 1), key="comprar_tempo_extra"),
                sg.Input(key="pular_qtd")
            ],
            [sg.Text("Quantidade maior que total de cursos a frente!", key="quantidade_maior")],
            [sg.Text("Quantidade inválida!", key="quantidade_menor")],
            [sg.Text("Valor Final")],
            [sg.Submit("Comprar")],
            [sg.Button("Voltar ao Menu")]
        ]

        window = sg.Window("Anunciar Curso", layout=layout, element_justification='c').Finalize()
        
        window.Element("comprar_tempo_extra").Update(visible=False)
        window.Element("pular_qtd").Update(visible=False)
        window.Element("quantidade_maior").Update(visible=False)
        window.Element("quantidade_menor").Update(visible=False)

        result = self.rodar(window)
        window.close()
        print(result)
        return result
