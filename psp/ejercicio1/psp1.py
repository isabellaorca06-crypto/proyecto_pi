import math

class PSP1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

        self.sum_x = 0
        self.sum_y = 0
        self.sum_xy = 0
        self.sum_x2 = 0
        self.sum_y2 = 0

        self.B0 = 0
        self.B1 = 0
        self.r = 0
        self.r2 = 0

    def __str__(self):
        return f"B0: {self.B0}, B1: {self.B1}, r: {self.r}, r2: {self.r2}"

    def calcular_sumatorias(self):
        for i in range(self.n):
            self.sum_x += self.x[i]
            self.sum_y += self.y[i]
            self.sum_xy += self.x[i] * self.y[i]
            self.sum_x2 += self.x[i] ** 2
            self.sum_y2 += self.y[i] ** 2

    def calcular_b1(self):
        num = self.n * self.sum_xy - self.sum_x * self.sum_y
        den = self.n * self.sum_x2 - self.sum_x ** 2
        self.B1 = num / den

    def calcular_b0(self):
        self.B0 = (self.sum_y - self.B1 * self.sum_x) / self.n

    def calcular_r(self):
        num = self.n * self.sum_xy - self.sum_x * self.sum_y
        den = math.sqrt(
            (self.n * self.sum_x2 - self.sum_x ** 2) *
            (self.n * self.sum_y2 - self.sum_y ** 2)
        )
        self.r = num / den

    def calcular_r2(self):
        self.r2 = self.r ** 2

    def calcular_yk(self, xk):
        return self.B0 + self.B1 * xk

    def proceso(self):
        self.calcular_sumatorias()
        self.calcular_b1()
        self.calcular_b0()
        self.calcular_r()
        self.calcular_r2()