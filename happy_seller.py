from control.controladorSistema import ControladorSistema

if __name__ == "__main__":
    tela = None
    controlador = ControladorSistema()
    while True:
        tela = controlador.inicia(tela)
        if tela == "SAIR":
            exit()
