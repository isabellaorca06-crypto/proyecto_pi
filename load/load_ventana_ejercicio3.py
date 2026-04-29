from PyQt5 import QtWidgets, uic
from psp.ejercicio3.integracion_inversa import integracion_inversa


class VentanaEjercicio3(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_ejercicio3.ui", self)
        self.show()

        self.boton_calcular.clicked.connect(self.boton_calcular_click)

    def boton_calcular_click(self):
        try:
            p   = float(self.edit_p.text())
            dof = int(self.edit_dof.text())

            if not (0 < p < 0.5):
                self.label_resultado.setText("p debe estar entre 0 y 0.5")
                return
            if dof < 1:
                self.label_resultado.setText("dof debe ser >= 1")
                return

            x = integracion_inversa(p, dof)
            self.label_resultado.setText(f"{x:.5f}")

        except ValueError:
            self.label_resultado.setText("Ingresa valores numéricos válidos")
