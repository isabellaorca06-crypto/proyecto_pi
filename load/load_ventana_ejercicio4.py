from PyQt5 import QtWidgets, uic
from psp.ejercicio4.calculo_psp import CalculoPSP


class VentanaEjercicio4(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_ejercicio4.ui", self)
        self.show()

        self.boton_calcular.clicked.connect(self.boton_calcular_click)
        self.boton_limpiar.clicked.connect(self.boton_limpiar_click)

    def _leer_lista(self, texto):
        """Convierte una cadena 'v1, v2, v3' en lista de floats."""
        partes = texto.replace("\n", ",").split(",")
        return [float(p.strip()) for p in partes if p.strip() != ""]

    def boton_calcular_click(self):
        try:
            lista_x = self._leer_lista(self.edit_x.text())
            lista_y = self._leer_lista(self.edit_y.text())
            xk      = float(self.edit_xk.text())

            if len(lista_x) != len(lista_y):
                self.label_rxy.setText("Error: X e Y deben tener el mismo número de datos")
                return
            if len(lista_x) < 3:
                self.label_rxy.setText("Se necesitan al menos 3 datos")
                return

            calculo = CalculoPSP(lista_x, lista_y, xk)
            calculo.calcular_todo()
            self.label_rxy.setText(f"{calculo.rxy:.9f}")
            self.label_r2.setText(f"{calculo.r2:.8f}")
            self.label_tail.setText(f"{calculo.tail_area:.8E}")
            self.label_b0.setText(f"{calculo.b0:.8f}")
            self.label_b1.setText(f"{calculo.b1:.9f}")
            self.label_yk.setText(f"{calculo.yk:.7f}")
            self.label_rango.setText(f"{calculo.rango:.7f}")
            self.label_upi.setText(f"{calculo.upi:.7f}")
            self.label_lpi.setText(f"{calculo.lpi:.6f}")

        except ValueError:
            self.label_rxy.setText("Ingresa valores numéricos separados por comas")

    def boton_limpiar_click(self):
        self.edit_x.clear()
        self.edit_y.clear()
        self.edit_xk.clear()
        self.label_rxy.setText("-")
        self.label_r2.setText("-")
        self.label_tail.setText("-")
        self.label_b0.setText("-")
        self.label_b1.setText("-")
        self.label_yk.setText("-")
        self.label_rango.setText("-")
        self.label_upi.setText("-")
        self.label_lpi.setText("-")
