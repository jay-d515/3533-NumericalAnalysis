import math
from sympy import symbols, diff

def newtons_method(func, func_prime, p0, tol, max_iterations):
    iteration = 0

    while iteration <= max_iterations:
        p = p0 - func(p0) / func_prime(p0)

        if abs(p - p0) < tol:
            return p, iteration


        iteration += 1
        p0 = p

    print("The procedure was unsuccessful.")
    print("The method failed after ", max_iterations)

q1 = lambda x: x**3 + 3*x**2 - 1
prime = lambda x: 3*x**2 + 6*x

root, iterations = newtons_method(q1, prime, -3, 10e-4, 50)

print("Approximation: ", root)
print("Total iterations: ", iterations)
