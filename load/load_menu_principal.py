from PyQt5 import uic, QtWidgets

class MenuPrincipal(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_menu.ui", self)

        # 🔹 Conectar botones
        self.btnPSP1.clicked.connect(self.abrir_psp1)
        self.btnPSP2.clicked.connect(self.abrir_psp2)
        self.btnPSP3.clicked.connect(self.abrir_psp3)
        self.btnPSP4.clicked.connect(self.abrir_psp4)
        self.btnSalir.clicked.connect(self.close)

    def abrir_psp1(self):
        from load.load_venta_psp1 import VentanaPSP1
        self.ventana = VentanaPSP1()   
        self.ventana.show()

    def abrir_psp2(self):
        from load.load_venta_psp2 import VentanaPSP2
        self.ventana = VentanaPSP2()  
        self.ventana.show()

    def abrir_psp3(self):
        from load.load_ventana_ejercicio3 import VentanaEjercicio3
        self.ventana = VentanaEjercicio3()
        self.ventana.show()

    def abrir_psp4(self):
        from load.load_ventana_ejercicio4 import VentanaEjercicio4
        self.ventana = VentanaEjercicio4()
        self.ventana.show()