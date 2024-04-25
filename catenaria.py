import numpy as np
import math

def catenaria(x, B = [4,2], L = 20):
    f_a = lambda a : math.sqrt(L**2 - B[1]**2)/(2*a) - math.sinh(B[0]/(2*a)) if a > 0.01 else 0.01
    a = bisection(f_a, 0.02, 10)

    f_f = lambda f : B[1] + a + f - a*math.cosh((B[0]/a - math.acosh(1 + f/a))) if a > 0.01 else 0.01
    f = bisection(f_f, 0.02, 1000)

    x0 = a*math.acosh(1+f/a)
    y0 = -(a + f)

    f_catenaria = a*np.cosh((x-x0)/a) + y0

    return f_catenaria

def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Encuentra una aproximación de la raíz de la función f(x) en el intervalo [a, b] usando el método de bisección.

    Args:
        f: Función f(x) para la cual queremos encontrar la raíz.
        a, b: Extremos del intervalo [a, b].
        tol: Tolerancia para la convergencia (opcional, valor predeterminado: 1e-6).
        max_iter: Número máximo de iteraciones (opcional, valor predeterminado: 100).

    Returns:
        float: Aproximación de la raíz.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("La función no cambia de signo en el intervalo [a, b].")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    raise ValueError("El método no convergió después de {} iteraciones.".format(max_iter))