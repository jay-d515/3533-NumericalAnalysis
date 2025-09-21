import math

def secant_method(f, p0, p1, tol, max_iterations):
    q0 = f(p0)
    q1 = f(p1)

    i = 2

    while i <= max_iterations:
        if (q1 - q0) == 0:
            print("Division by zero encountered in secant method.")
            return None
        
        # compute next approximation
        p = p1 - q1 * (p1 - p0) / (q1 - q0)

        # check stopping criterion
        if abs(p - p1) < tol:
            return p
        
        # update for next iteration
        i += 1
        p0, p1 = p1, p
        q0, q1, q1, f(p)

    print(f"The method failed after {max_iterations} iterations.")
    return None
        