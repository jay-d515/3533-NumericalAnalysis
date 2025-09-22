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
    return x**2 - 2*x*math.exp(-x) + math.exp(-2*x)
def fprime(x):
    return 2*x + 2*x*math.exp(-x) - 2*math.exp(-x) - 2*math.exp(-2*x)

root, iterations = newtons_method(f, fprime, 0.5, 1e-5, 50)

print("Approximation: ", root)
print("Total iterations: ", iterations)