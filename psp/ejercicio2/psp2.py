import scipy.special as sc
import numpy as np

class PSP2:

    def __init__(self, x, dof, n):
        self.x = x
        self.dof = dof
        self.n = n
        self.resultado = 0

    def fx(self, t):
        return sc.gamma((self.dof + 1) / 2) / ((self.dof * np.pi) ** 0.5 * sc.gamma(self.dof / 2)) * (1 + t**2 / self.dof) ** (-(self.dof + 1) / 2)

    def proceso(self):
        if self.n % 2 != 0:
            raise ValueError("n debe ser un número par")

        a = min(0, self.x)
        b = max(0, self.x)
        h = (b - a) / self.n

        suma = 0
        for i in range(1, self.n):
            x_i = a + i * h
            coef = 4 if i % 2 != 0 else 2
            suma += coef * self.fx(x_i)

        fx0 = self.fx(a)
        fxn = self.fx(b)
        self.resultado = (h / 3) * (fx0 + suma + fxn)

        return self.resultado

if __name__ == "__main__":
    x = float(input("x = "))
    dof = int(input("dof = "))
    n = int(input("n = "))

    obj = PSP2(x, dof, n)
    resultado = obj.proceso()
    print("p =", resultado)