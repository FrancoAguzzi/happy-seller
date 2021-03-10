from view.viewAnuncioCurso import ViewAnuncioCurso
from control.controladorCurso import ControladorCurso

class ControladorAnunciarCurso():
    def __init__(self):
        self.__controlador_curso = ControladorCurso()
    
    def anunciar_curso(self, result):
        pass

    def abrir_tela_anunciar_curso(self, cpf_anunciante):
        cursos = self.__controlador_curso.filtrar_cursos_por_cpf(cpf_anunciante)
        cursos_na_frente = self.__controlador_curso.total_de_cursos_na_esteira()
        #return ViewAnuncioCurso(cursos, cursos_na_frente).comecar()
        return ViewAnuncioCurso(
                [{"nome": "abc"},{"nome":"def"}], 
                5
            ).comecar()
