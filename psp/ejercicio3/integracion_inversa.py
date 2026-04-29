import math

def gamma(x):
    """Calcula la función gamma de forma recursiva."""
    if x == 0.5:
        return math.sqrt(math.pi)
    elif x == 1.0:
        return 1.0
    else:
        return (x - 1) * gamma(x - 1)

def funcion_t(x, dof):
    """Calcula el valor de la función de densidad de la distribución t en x."""
    numerador   = gamma((dof + 1) / 2)
    denominador = math.sqrt(math.pi * dof) * gamma(dof / 2)
    base        = 1 + (x ** 2) / dof
    exponente   = -((dof + 1) / 2)
    return (numerador / denominador) * (base ** exponente)

def simpson(x_superior, dof, error=0.00001):
    """
    Integra la distribución t de 0 a x_superior con dof grados de libertad.
    Usa la regla de Simpson duplicando segmentos hasta alcanzar el error deseado.
    """
    if x_superior == 0:
        return 0.0

    num_seg = 10  

    def calcular_integral(n):
        w = x_superior / n
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
    """
    Encuentra el valor de x tal que integrar la distribución t de 0 a x
    produce el valor p.
    Algoritmo de búsqueda binaria adaptativa (método del documento).
    """
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
