import numpy as np

def newton_divided_differences(x, y):
    """
    Builds the divided differences table for Newton's interpolation.
    Returns: coefficients of the Newton polynomial.
    """

    n = len(x)
    coef = np.copy(y).astype(float)

    # Build table (in-place)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef


def newton_evaluate(x_data, coef, x):
    """
    Evaluates Newton's interpolation polynoial at point x.
    """

    n = len(coef)
    result = coef[-1]

    for i in range(n - 2, -1, -1):
        result = result * (x - x_data[i]) + coef[i]

    return result


def neville(x_data, y_data, x):
    """
    Neville's Interpolation method.
    Computes P(x) using a triangular table.
    """

    n = len(x_data)
    Q = np.zeros((n, n))
    Q[:, 0] = y_data

    for j in range(1, n):
        for i in range(n - j):
            Q[i][j] = ((x - x_data[i + j]) * Q[i][j - 1] +
                       (x_data[i] - x) * Q[i + 1][j - 1]) / \
                       (x_data[i] - x_data[i + j])
            
    return Q[0][n - 1]


# Load the data
x = np.array([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0])

f1 = np.array([1, 1.6499, 2.4221, 3.3596, 4.5201, 5.9817,
               7.8496, 10.266, 13.423, 17.58, 23.086])

f3 = np.array([0.75, 0.315, 0.06, -0.015, 0.09, 0.375,
               0.84, 1.485, 2.31, 3.315, 4.5])

f4 = np.array([0.858, -1.026, -1.344, -0.8736, -0.198,
               0.294, 0.408, 0.144, -0.3036, -0.546, 0])

eval_point = 1

# Evalution for column f1
coef_f1 = newton_divided_differences(x, f1)
p_f1 = newton_evaluate(x, coef_f1, eval_point)
print("Newton f1(", eval_point, ") =", p_f1)

p_f1_nev = neville(x, f1, eval_point)
print("Neville f1(", eval_point, ") =", p_f1_nev)


# Evalution for column f3
coef_f3 = newton_divided_differences(x, f3)
p_f3 = newton_evaluate(x, coef_f1, eval_point)
print("Newton f3(", eval_point, ") =", p_f3)

p_f3_nev = neville(x, f3, eval_point)
print("Neville f3(", eval_point, ") =", p_f3_nev)


# Evalution for column f4
coef_f4 = newton_divided_differences(x, f4)
p_f4 = newton_evaluate(x, coef_f4, eval_point)
print("Newton f4(", eval_point, ") =", p_f4)

p_f4_nev = neville(x, f4, eval_point)
print("Neville f4(", eval_point, ") =", p_f4_nev)