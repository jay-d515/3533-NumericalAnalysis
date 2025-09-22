import math

def fixed_point_iteration(f, p0, tol, max_iterations):
    i = 1

    while i <= max_iterations:
        # compute next approximation
        p = f(p0)

        # check stopping criteria
        if abs(p - p0) < tol:
            return p, i
        
        # increment number of iterations
        i += 1
        # update for next iteration
        p0 = p

    print(f"The method failed after {max_iterations} iterations.")
    return None, max_iterations

def f(x):
    return 

root, iterations = fixed_point_iteration()

print("Approximation: ", root)
print("Total iterations: ", iterations)