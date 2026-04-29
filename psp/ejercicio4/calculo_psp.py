import math

def gamma(x):
    if x == 0.5:
        return math.sqrt(math.pi)
    elif x == 1.0:
        return 1.0
    else:
        return (x - 1) * gamma(x - 1)


def funcion_t(x, dof):
    numerador   = gamma((dof + 1) / 2)
    denominador = math.sqrt(math.pi * dof) * gamma(dof / 2)
    base        = 1 + (x ** 2) / dof
    exponente   = -((dof + 1) / 2)
    return (numerador / denominador) * (base ** exponente)


def simpson(x_superior, dof, error=0.00001):
    if x_superior == 0:
        return 0.0
    num_seg = 10

    def calcular_integral(n):
        w    = x_superior / n
        suma = funcion_t(0, dof)
        for i in range(1, n, 2):
            suma += 4 * funcion_t(i * w, dof)
        for i in range(2, n - 1, 2):
            suma += 2 * funcion_t(i * w, dof)
        suma += funcion_t(x_superior, dof)
        return (w / 3) * suma

    resultado_anterior = calcular_integral(num_seg)
    num_seg *= 2
    resultado_nuevo    = calcular_integral(num_seg)

    while abs(resultado_nuevo - resultado_anterior) > error:
        resultado_anterior = resultado_nuevo
        num_seg           *= 2
        resultado_nuevo    = calcular_integral(num_seg)

    return resultado_nuevo


def integracion_inversa(p, dof, error=0.00001):
    x_prueba = 1.0
    d        = 0.5
    resultado = simpson(x_prueba, dof, error)
    if abs(resultado - p) <= error:
        return x_prueba
    error_anterior_positivo = resultado < p

    for _ in range(10000):
        resultado = simpson(x_prueba, dof, error)
        if abs(resultado - p) <= error:
            break
        error_actual_positivo = resultado < p
        if error_actual_positivo != error_anterior_positivo:
            d /= 2
        if error_actual_positivo:
            x_prueba += d
        else:
            x_prueba -= d
        if x_prueba <= 0:
            x_prueba = d / 2
        error_anterior_positivo = error_actual_positivo

    return x_prueba

class CalculoPSP:
    """
    Agrupa todos los cálculos de la Parte IV:
    correlación, regresión, significancia, predicción e intervalo.
    """

    def __init__(self, lista_x, lista_y, xk):
        """
        lista_x : lista de floats (datos históricos x)
        lista_y : lista de floats (datos históricos y)
        xk      : float (nuevo valor de x para la predicción)
        """
        self.x   = lista_x
        self.y   = lista_y
        self.xk  = xk
        self.n   = len(lista_x)
        self.rxy      = None
        self.r2       = None
        self.tail_area = None
        self.b0       = None
        self.b1       = None
        self.yk       = None
        self.rango    = None
        self.upi      = None
        self.lpi      = None

    def _suma(self, lista):
        return sum(lista)

    def _promedio(self, lista):
        return sum(lista) / len(lista)

    def calcular_correlacion(self):
        """Calcula r_xy y r^2."""
        n = self.n
        sx  = self._suma(self.x)
        sy  = self._suma(self.y)
        sx2 = self._suma([xi ** 2 for xi in self.x])
        sy2 = self._suma([yi ** 2 for yi in self.y])
        sxy = self._suma([self.x[i] * self.y[i] for i in range(n)])

        num = n * sxy - sx * sy
        den = math.sqrt((n * sx2 - sx ** 2) * (n * sy2 - sy ** 2))

        self.rxy = num / den if den != 0 else 0
        self.r2  = self.rxy ** 2

    def calcular_regresion(self):
        """Calcula β0 y β1."""
        n    = self.n
        xavg = self._promedio(self.x)
        yavg = self._promedio(self.y)
        sx2  = self._suma([xi ** 2 for xi in self.x])
        sxy  = self._suma([self.x[i] * self.y[i] for i in range(n)])

        self.b1 = (sxy - n * xavg * yavg) / (sx2 - n * xavg ** 2)
        self.b0 = yavg - self.b1 * xavg

    def calcular_prediccion(self):
        """Calcula yk dado xk."""
        self.yk = self.b0 + self.b1 * self.xk

    def calcular_tail_area(self):
        """
        Calcula la significancia de la correlación (tail area).
        Pasos:
          1. x = |r_xy| * sqrt(n-2) / sqrt(1 - r²)
          2. p = integral de la distribución t de 0 a x con dof = n-2
          3. tail_area = 1 - 2*p
        """
        dof = self.n - 2
        den = math.sqrt(1 - self.r2)
        x   = abs(self.rxy) * math.sqrt(dof) / den if den != 0 else 0
        p   = simpson(x, dof)
        self.tail_area = 1 - 2 * p

    def calcular_intervalo(self):
        """
        Calcula Range (70%), UPI y LPI.
        Pasos:
          1. t(0.35, dof) usando integración inversa
          2. sigma
          3. término de la raíz
          4. Range
          5. UPI = yk + Range
          6. LPI = yk - Range
        """
        dof  = self.n - 2
        xavg = self._promedio(self.x)

        t_val = integracion_inversa(0.35, dof)

        suma_residuales = sum(
            (self.y[i] - self.b0 - self.b1 * self.x[i]) ** 2
            for i in range(self.n)
        )
        sigma = math.sqrt(suma_residuales / (self.n - 2))

        suma_x_diff = sum((xi - xavg) ** 2 for xi in self.x)
        termino_raiz = math.sqrt(
            1 + 1 / self.n + (self.xk - xavg) ** 2 / suma_x_diff
        )

        self.rango = t_val * sigma * termino_raiz
        self.upi   = self.yk + self.rango
        self.lpi   = self.yk - self.rango

    def calcular_todo(self):
        """Ejecuta todos los cálculos en el orden correcto."""
        self.calcular_correlacion()
        self.calcular_regresion()
        self.calcular_prediccion()
        self.calcular_tail_area()
        self.calcular_intervalo()
