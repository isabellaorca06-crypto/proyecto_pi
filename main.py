import sys
from PyQt5 import QtWidgets
from load.load_menu_principal import MenuPrincipal

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()