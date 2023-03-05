import pulp
import numpy as np

# Define the matrix A and vector b
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([10, 20, 30])

# Get the dimensions of the matrix A
m, n = A.shape

# Define the decision variables as a list of LpVariables
x = [pulp.LpVariable("x_%d" % i, lowBound=0) for i in range(n)]

# Define the problem
prob = pulp.LpProblem("Minimize Ax-b Problem", pulp.LpMinimize)

# Set the objective function to Ax-b
prob += pulp.lpSum([[A[i, j] * x[j] for j in range(n)] - b[i]
                   for i in range(m)])

# Solve the problem
prob.solve()

# Print the solution
print("Status:", pulp.LpStatus[prob.status])
print("Objective value:", pulp.value(prob.objective))
print("x =", [pulp.value(x[i]) for i in range(n)])
