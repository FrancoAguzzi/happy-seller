import random

from view.tempViewSellButtom import TempViewSellButtom
from view.viewControlarPlantao import ViewControlarPlantao
from view.view import View


class ControladorPlantao():
    def __init__(self):
        self.__view_sell_buttom = TempViewSellButtom()
        self.__view_controlar_plantao = ViewControlarPlantao()

    def abrir_tela_temp(self, pausado=False):
        cliente = self.pegar_proximo_cliente()
        dados = self.__view_sell_buttom.comecar(pausado=pausado, cliente=cliente)

        return dados

    def abrir_tela_controlar_plantao(self, anuncio_atual=None, pausado=False) -> dict:
        return self.__view_controlar_plantao.comecar(anuncio_atual=anuncio_atual, pausado=pausado)

    def pegar_proximo_curso(self):
        pass

    def pegar_proximo_cliente(self):
        nomes = [
            "Miguel", "Sophia",
            "Davi", "Alice",
            "Arthur", "Julia",
            "Pedro", "Isabella",
            "Gabriel", "Manuela",
            "Bernardo", "Laura",
            "Lucas", "Luiza",
            "Matheus", "Valentina",
            "Rafael", "Giovanna",
            "Heitor", "Maria Eduarda",
            "Enzo", "Helena",
            "Guilherme", "Beatriz",
            "Nicolas", "Maria Luiza",
            "Lorenzo", "Lara",
            "Gustavo", "Mariana",
            "Felipe", "Nicole",
            "Samuel", "Rafaela",
            "João Pedro", "Heloísa",
            "Daniel", "Isadora",
            "Vitor", "Lívia",
            "Leonardo", "Maria Clara",
            "Henrique", "Ana Clara",
            "Theo", "Lorena",
            "Murilo", "Gabriela",
            "Eduardo", "Yasmin",
            "Pedro Henrique", "Isabelly",
            "Pietro", "Sarah",
            "Cauã", "Ana Julia",
            "Isaac", "Letícia",
            "Caio", "Ana Luiza",
            "Vinicius", "Melissa",
            "Benjamin", "Marina",
            "João", "Clara",
            "Lucca", "Cecília",
            "João Miguel", "Esther",
            "Bryan", "Emanuelly",
            "Joaquim", "Rebeca",
            "João Vitor", "Ana Beatriz",
            "Thiago", "Lavínia",
            "Antônio", "Vitória",
            "Davi Lucas", "Bianca",
            "Francisco", "Catarina",
            "Enzo Gabriel", "Larissa",
            "Bruno", "Fernanda",
            "Emanuel", "Fernanda",
            "João Gabriel", "Amanda",
            "Ian", "Alícia",
            "Davi Luiz", "Carolina",
            "Rodrigo", "Agatha",
            "Otávio", "Gabrielly"
        ]

        emails = ["gmail", "hotmail", "outlook"]
        nome = nomes[random.randint(0, len(nomes) - 1)]
        telefone = "".join(str(random.randint(0, 9)) for x in range(11))
        email = nome.lower() + "@" + emails[random.randint(0, len(emails) - 1)] + ".com"
        return (nome, telefone, email.replace(" ", "_"))
