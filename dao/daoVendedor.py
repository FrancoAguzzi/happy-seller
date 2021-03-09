class DaoVendedor():
    def __init__(self, data_source):
        self.__data_source = data_source

    def cadastrar_vendedor(self, vendedor):
        with open(self.__data_source, "a") as src:
            dados = vendedor.pegar_dados_como_tuplas()
            linha = ""
            for (k, v) in dados:
                linha += f"{v},"
            src.write(linha[:-1] + "\n")
