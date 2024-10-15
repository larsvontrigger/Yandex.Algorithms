import numpy as np

# Input values
a1 = int(input())  # a1
b1 = int(input())  # b1
a2 = int(input())  # a2
b2 = int(input())  # b2
e1 = int(input())  # e1
e2 = int(input())  # e2

# Define the coefficient matrix and the vector of right-hand sides
matrix = np.array([[a1, b1], [a2, b2]])
vector = np.array([e1, e2])

# Check for singularity (determinant check)
det = np.linalg.det(matrix)

# If the determinant is not zero, the system has a unique solution
if det != 0:
    solution = np.linalg.solve(matrix, vector)
    print(2)
    print(f"{solution[0]:.5f} {solution[1]:.5f}")

# Determinant is zero, check special cases
else:
    # Both equations are proportional
    if a1 * b2 == a2 * b1 and a1 * e2 == a2 * e1 and b1 * e2 == b2 * e1:
        # All coefficients are zero => any (x, y) is a solution
        if a1 == a2 == b1 == b2 == e1 == e2 == 0:
            print(5)
        # System is of the form x = x0, y is arbitrary
        elif a1 != 0 and a2 != 0:
            x0 = e1 / a1
            print(3)
            print(f"{x0:.5f}")
        # System is of the form y = y0, x is arbitrary
        elif b1 != 0 and b2 != 0:
            y0 = e1 / b1
            print(4)
            print(f"{y0:.5f}")
        # Infinite number of solutions in the form y = kx + b
        else:
            k = -a1 / b1
            b = e1 / b1
            print(1)
            print(f"{k:.5f} {b:.5f}")
    # The system has no solutions
    else:
        print(0)
