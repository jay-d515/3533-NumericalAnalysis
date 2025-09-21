import math

def bisection_method(f, a, b, tol, max_iterations):

    if f(a) * f(b) >= 0:
        print("f(a) and f(b) must have opposite signs.")
        return None

    i = 1
    fa = f(a)

    while i <+ max_iterations:
        # calculate the midpoint
        p = a + (b - a) / 2
        fp = f(p)

        # check the stopping criteria
        if fp == 0 or (b - a) / 2 < tol:
            return p
        
        i += 1

        # update the interval
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p
    print(f"Method failed after {max_iterations} iterations.")
    return None

def func(x):
    pass
