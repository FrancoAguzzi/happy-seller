from control.controladorSistema import ControladorSistema

if __name__ == "__main__":
    while True:
        result = ControladorSistema().inicia()
        if result == "SAIR":
            exit()
