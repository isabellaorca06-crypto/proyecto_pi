from PyQt5 import uic, QtWidgets
from psp.ejercicio2.psp2 import PSP2

class VentanaPSP2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_psp_2.ui", self)

        self.label.setText("Valor x")
        self.label_2.setText("Grados de libertad (dof)")
        self.label_3.setText("Número de intervalos (n)")

        self.btnCalcular.clicked.connect(self.calcular)

    def calcular(self):
        try:
            x = float(self.txtA.text())
            dof = int(self.txtB.text())
            n = int(self.txtN.text())

            obj = PSP2(x, dof, n)
            r = obj.proceso()

            self.lblResultado.setText(str(r))

        except Exception:
            self.lblResultado.setText("Error")