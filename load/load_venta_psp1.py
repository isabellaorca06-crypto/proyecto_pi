from PyQt5 import uic, QtWidgets
from psp.ejercicio1.psp1 import PSP1

class VentanaPSP1(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_1.ui", self)

        self.boton_caso1.clicked.connect(self.caso1)
        self.boton_caso2.clicked.connect(self.caso2)
        self.boton_caso3.clicked.connect(self.caso3)
        self.boton_caso4.clicked.connect(self.caso4)

        self.boton_calcular.clicked.connect(self.calcular)

        self.x = []
        self.y = []

    def caso1(self):
        self.x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        self.y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

    def caso2(self):
        self.x = [1,2,3,4,5]
        self.y = [2,4,5,4,5]

    def caso3(self):
        self.x = [10,20,30,40]
        self.y = [15,25,35,45]

    def caso4(self):
        self.x = [5,10,15,20]
        self.y = [7,12,18,25]

    def calcular(self):
        try:
            xk = float(self.edit_xk.text())

            obj = PSP1(self.x, self.y)
            obj.proceso()

            yk = obj.calcular_yk(xk)

            self.label_B1.setText(str(obj.B1))
            self.label_B0.setText(str(obj.B0))
            self.label_r.setText(str(obj.r))
            self.label_r2.setText(str(obj.r2))
            self.label_yk.setText(str(yk))

        except:
            QtWidgets.QMessageBox.warning(self, "Error", "Datos incorrectos")