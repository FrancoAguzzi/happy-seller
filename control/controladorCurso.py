from model.curso import Curso
from view.viewCadastroCurso import ViewCadastroCurso
from view.viewAnuncioCurso import ViewAnuncioCurso


class ControladorCurso():
    def __init__(self):
        self.__tela_cadastro_curso = ViewCadastroCurso()

    def cadastrar_curso(self, nome_curso, link_curso, preco_curso):
        return Curso(nome_curso, link_curso, preco_curso)

    def abrir_tela_curso(self):
        return self.__tela_cadastro_curso.comecar()

    def anunciar_curso(self, result):
        pass

    def abrir_tela_anunciar_curso(self, cursos):
        erro = None
        valor_final = None
        curso_selecionado = None
        duracao = None
        pular_qtd = None
        # cursos_na_frente = self.total_de_cursos_na_esteira()
        cursos_na_frente = 5
        kwargs = {}
        while True:
            result = ViewAnuncioCurso(cursos, cursos_na_frente).comecar(
                erro=erro, valor_final=valor_final, **kwargs)
            if result["result"]:

                curso_selecionado = self.selecionar_curso(
                    cursos, **result["result"])
                duracao = self.selecionar_duracao(**result["result"])
                pular_qtd = self.selecionar_pular_qtd(**result["result"])
                valor_final = self.calcular_valor_final(
                    duracao=duracao, pular_qtd=pular_qtd)

                e_valido, erro = self.validar_dados_anuncio(
                    valid_params={"cursos_na_frente": cursos_na_frente},
                    curso_selecionado=curso_selecionado, duracao=duracao, pular_qtd=pular_qtd)
                if not e_valido:
                    kwargs = result["result"]
                    continue
                if result["result"].get("calcular", False):
                    continue
            return {"result": {"curso": curso_selecionado, "tempo_divulgacao": duracao, "pular_qtd": pular_qtd}}

    def selecionar_pular_qtd(self, **kwargs):
        pular = 0
        if kwargs.get("pular_qtd", False):
            pular = kwargs.get("pular_qtd")
        return int(pular)

    def selecionar_duracao(self, **kwargs):
        duracao = 10
        if kwargs.get("extra_dez", False):
            duracao = 20
        elif kwargs.get("extra_vinte", False):
            duracao = 30
        return duracao

    def selecionar_curso(self, cursos, **kwargs):
        curso_selecionado = None
        for curso in cursos:
            if kwargs.get("nomeCurso." + curso.nome_curso, False):
                curso_selecionado = curso
        return curso_selecionado

    def calcular_valor_final(self, duracao, pular_qtd):
        return (duracao * 50) + (pular_qtd * 100)

    def validar_dados_anuncio(self, valid_params, curso_selecionado, duracao, pular_qtd):
        def pegar_campo_vazio():
            campos = [
                (curso_selecionado, "Cursos Disponíveis"),
                (duracao, "Duração")
            ]

            for campo, nome in campos:
                if not campo:
                    return f"'{nome}' está vazio"

        campo_vazio = pegar_campo_vazio()

        verificacoes = [
            (lambda: not campo_vazio, campo_vazio),
            (lambda: not pular_qtd > valid_params.get("cursos_na_frente"),
             "Quantidade maior que total de cursos a frente!"),
            (lambda: not pular_qtd < 0, "Quantidade inválida!")
        ]

        for e_valido, erro in verificacoes:
            if not e_valido():
                return (False, erro)
        return (True, None)
