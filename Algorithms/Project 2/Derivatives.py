import numpy as np

# ============================
# Three-point ENDPOINT
# ============================
def three_point_endpoint(x, f):
    n = len(x)
    h = x[1] - x[0]   # assume uniform spacing
    
    derivative = [None] * n
    
    # Forward difference at x0
    derivative[0] = (-3*f[0] + 4*f[1] - f[2]) / (2*h)
    
    # Backward difference at xn
    derivative[n-1] = (3*f[n-1] - 4*f[n-2] + f[n-3]) / (2*h)
    
    return derivative


# ============================
# Three-point MIDPOINT
# ============================
def three_point_mid(x, f):
    n = len(x)
    h = x[1] - x[0]
    
    derivative = [None] * n
    
    for i in range(1, n - 1):
        derivative[i] = (f[i+1] - f[i-1]) / (2*h)
    
    return derivative


# ============================
# Five-point MIDPOINT
# ============================
def five_point_mid(x, f):
    n = len(x)
    h = x[1] - x[0]
    
    derivative = [None] * n
    
    for i in range(2, n - 2):
        derivative[i] = (-f[i+2] + 8*f[i+1] - 8*f[i-1] + f[i-2]) / (12*h)
    
    return derivative



def print_table(x, f, endp, mid3, mid5, title="Results"):
    print(f"\n===== {title} =====")
    print(f"{'x':>7} {'f(x)':>12} {'3-pt end':>12} {'3-pt mid':>12} {'5-pt mid':>12}")
    print("-" * 63)

    for xi, fi, e, m3, m5 in zip(x, f, endp, mid3, mid5):
        e_str  = f"{e:12.6f}"  if e  is not None else f"{'--':>12}"
        m3_str = f"{m3:12.6f}" if m3 is not None else f"{'--':>12}"
        m5_str = f"{m5:12.6f}" if m5 is not None else f"{'--':>12}"

        print(f"{xi:7.2f} {fi:12.4f} {e_str} {m3_str} {m5_str}")


# ============= Example =============
x = np.array([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0])
fx1 = np.array([1, 1.6499, 2.4221, 3.3596, 4.5201, 5.9817, 7.8496, 10.266, 13.423, 17.58, 23.086])
fx3 = np.array([0.75, 0.315, 0.06, -0.015, 0.09, 0.375, 0.84, 1.485, 2.31, 3.315, 4.5])
fx4 = np.array([0.858, -1.026, -1.344, -0.8736, -0.198, 0.294, 0.408, 0.144, -0.3036, -0.546, 0])

endp1 = three_point_endpoint(x, fx1)
mid3_1 = three_point_mid(x, fx1)
mid5_1 = five_point_mid(x, fx1)

endp3 = three_point_endpoint(x, fx3)
mid3_3 = three_point_mid(x, fx3)
mid5_3 = five_point_mid(x, fx3)

endp4 = three_point_endpoint(x, fx4)
mid3_4 = three_point_mid(x, fx4)
mid5_4 = five_point_mid(x, fx4)

print_table(x, fx1, endp1, mid3_1, mid5_1, "f1 Derivatives")
print_table(x, fx3, endp3, mid3_3, mid5_3, "f3 Derivatives")
print_table(x, fx4, endp4, mid3_4, mid5_4, "f4 Derivatives")

