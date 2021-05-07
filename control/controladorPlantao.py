from view.tempViewSellButtom import TempViewSellButtom
from view.view import View


class ControladorPlantao():
    def __init__(self):
        self.__view_sell_buttom = TempViewSellButtom()

    def abrir_tela_temp(self):
        dados = self.__view_sell_buttom.comecar()

        return dados
