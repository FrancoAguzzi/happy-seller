import PySimpleGUI as sg
from .view import View


class ViewAnuncioCurso(View):

    def __init__(self, cursos, anuncios_frente):
        self.__cursos = cursos
        self.__anuncios_frente = anuncios_frente

    def rodar(self, window):
        while True:
            event, values = window.read()

            duracao = 10
            valor = 500
            if values["extra_dez"]:
                valor = valor + 500
                duracao = 20
            elif values["extra_vinte"]:
                valor = valor + 1000
                duracao = 30

            if values["pular_qtd"]:
               valor = valor + int(values["pular_qtd"]) * 100

            curso_selecionado = ""
            for curso in self.__cursos:
                if values["nomeCurso."+curso["nome_curso"]]:
                    curso_selecionado = curso["nome_curso"]

            if event == "Comprar":
                if values["pular_qtd"] and int(values["pular_qtd"]) > self.__anuncios_frente:
                    window.Element("quantidade_maior").Update(visible=True)
                    window.Element("quantidade_menor").Update(visible=False)
                elif values["pular_qtd"] and int(values["pular_qtd"]) < 0:
                    window.Element("quantidade_maior").Update(visible=False)
                    window.Element("quantidade_menor").Update(visible=True)
                elif not curso_selecionado:
                    window.Element("empty_field").Update(visible=True)
                else:
                    return self.voltar(view=window, result={"curso_selecionado": curso_selecionado, "duracao": duracao})
            if event == "Sim":
                window.Element("comprar_tempo_extra").Update(visible=True)
                window.Element("pular_qtd").Update(visible=True)
            if event == "Calcular Valor Final":
                window.Element("valor_final").Update(visible=True, values=[f"R$ {valor},00"])
            if event == "Voltar ao Menu" or event == sg.WIN_CLOSED:
                return self.voltar(view=window)

    def comecar(self):
        layout = [
            [sg.Text("Anunciar Curso")],
            [sg.Text("Cursos Disponíveis")],
            [sg.Column([
                *[[sg.Radio(curso["nome_curso"], group_id="curso_radio", key="nomeCurso."+curso["nome_curso"]), ] for curso in self.__cursos]
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
                sg.Text("Quantidade", size=(10, 1), key="comprar_tempo_extra"),
                sg.Input(key="pular_qtd")
            ],
            [sg.Text("Quantidade maior que total de cursos a frente!", key="quantidade_maior")],
            [sg.Text("Quantidade inválida!", key="quantidade_menor")],
            [sg.Button("Calcular Valor Final")],
            [sg.Listbox(values=[], key="valor_final", size=(20,1))],
            [sg.Text("Você deve selecionar um curso!", key="empty_field")],
            [sg.Submit("Comprar")],
            [sg.Button("Voltar ao Menu")]
        ]

        window = sg.Window("Anunciar Curso", layout=layout, element_justification='c').Finalize()
        
        window.Element("empty_field").Update(visible=False)
        window.Element("comprar_tempo_extra").Update(visible=False)
        window.Element("pular_qtd").Update(visible=False)
        window.Element("quantidade_maior").Update(visible=False)
        window.Element("quantidade_menor").Update(visible=False)
        window.Element("valor_final").Update(visible=False)

        result = self.rodar(window)
        window.close()
        return result
