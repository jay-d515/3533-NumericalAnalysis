import math
from sympy import symbols, diff

def newtons_method(func, func_prime, p0, tol, max_iterations):
    i = 1

    while i < max_iterations:
        
        p = p0 - func(p0) / func_prime(p0)

        if abs(p - p0) < tol:
            return p, i

        i += 1
        p0 = p

    print("The method failed after ", max_iterations, " iterations.")
    return None, max_iterations

def f(x):
    return math.cos(x + math.sqrt(2)) + x*((x / 2) + math.sqrt(2))
def fprime(x):
    return -(math.sin(x + math.sqrt(2))) + x + math.sqrt(2)

root, iterations = newtons_method(f, fprime, -1.5, 1e-5, 50)

print("Approximation: ", root)
print("Total iterations: ", iterations)