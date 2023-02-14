import cvxpy as cp
from cvxopt import matrix, solvers
from foodData import Food


def Algo(Nutri):
    FoodNutri = []
    for food in Food:
        zero_list = [0]*len(Food)
        zero_list[Food.index(food)] = -1
        listFood = [-food["Calories"], -food["Protein"], -food["Carbs"],
                    -food["Fat"], -food["Fiber"], -food["Sugar"], -food["Salt"]]
        FoodNutri.append(listFood)
    # # Define the constraints
    # constraints = [[10, 5]*FoodNames[0] + [2, 12]*FoodNames[1] + [4, 8]*FoodNames[2] >= [12, 588],
    #                FoodNames[0] >= 0,
    #                FoodNames[1] >= 0,
    #                FoodNames[2] >= 0]

    # # Define the objective function
    # obj = cp.Minimize(2*FoodNames[0] + 3*FoodNames[1] + FoodNames[2])

    # # Define the problem
    # prob = cp.Problem(obj, constraints)

    # # Solve the problem using the Interior Point Method
    # prob.solve(solver=cp.CVXOPT)
    A = matrix(FoodNutri)
    b = matrix([-Nutri["Calories"], -Nutri["Protein"], -Nutri["Carbs"],
                -Nutri["Fat"], -Nutri["Fiber"], -Nutri["Sugar"], -Nutri["Salt"]])
    c = matrix([1.0]*len(Food))
    # A = matrix([[-1.0e+01, -1.0, 0.0, 1.0, 1, -2, 3],
    #            [1.0, -1.0, -0.0, -2.0, 2, -4, 5], [1.0, -1.0, -0.0, -2.0, 1, -1,5]])
    # b = matrix([-1.0e+01, -1.0, 0.0, 0.0, 1, 1,2])
    # c = matrix([2.0, 1.0, 3])
    sol = solvers.lp(c, A, b)


# # Print the results
#     print("Optimal values: x = {}, y = {}, z = {}".format(
#         FoodNames[0].value, FoodNames[1].value, FoodNames[2].value))
    print(sol["x"])
    return "Optimal values: x = {}, y = {}, z = {}"


Algo({
    "name": "Hummus, commercial",
    "Protein": 7.35,
    "Calories": 0.0,
    "Fat": 1152.1,
    "Fiber": 5.4,
    "Carbs": 14.9,
    "Salt": 438.0,
    "Sugar": 0.34
})
