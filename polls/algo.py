# import pulp

# # Define the decision variables using a dictionary and a for loop

from scipy.optimize import minimize
import numpy as np
Food = [{"Salt": 0.0, "Protein": 0.188, "Calories": 61.8, "Fat": 0.212, "Fiber": 2.04, "Carbs": 14.8, "Sugar": 12.2, "name": "Apples, red delicious, with skin, raw"}, {"Salt": 1.01, "Protein": 0.148, "Calories": 64.7, "Fat": 0.162, "Fiber": 2.08, "Carbs": 15.7, "Sugar": 13.3, "name": "Apples, fuji, with skin, raw"}, {"Salt": 0.279, "Protein": 0.133, "Calories": 61.0, "Fat": 0.15, "Fiber": 2.11, "Carbs": 14.8, "Sugar": 11.8, "name": "Apples, gala, with skin, raw"}, {"Salt": 0.0, "Protein": 0.266, "Calories": 58.9, "Fat": 0.138, "Fiber": 2.51, "Carbs": 14.1, "Sugar": 10.7, "name": "Apples, granny smith, with skin, raw"}, {"Salt": 0.138, "Protein": 0.102, "Calories": 60.0, "Fat": 0.1, "Fiber": 1.72, "Carbs": 14.7, "Sugar": 12.4, "name": "Apples, honeycrisp, with skin, raw"}, {"Salt": 0.336, "Protein": 2.5, "Calories": 42.7, "Fat": 0.256, "Fiber": 4.38, "Carbs": 7.59, "Sugar": 0, "name": "Mushroom, lion's mane"}, {"Salt": 1.13, "Protein": 2.9, "Calories": 41.0, "Fat": 0.188, "Fiber": 2.85, "Carbs": 6.94, "Sugar": 0, "name": "Mushroom, oyster"}, {"Salt": 0.936, "Protein": 2.41, "Calories": 44.1, "Fat": 0.195, "Fiber": 4.17, "Carbs": 8.17, "Sugar": 0, "name": "Mushrooms, shiitake"}, {"Salt": 6.44, "Protein": 2.89, "Calories": 31.2, "Fat": 0.371, "Fiber": 1.72, "Carbs": 4.08, "Sugar": 0, "name": "Mushrooms, white button"}, {"Salt": 34.3, "Protein": 3.55, "Calories": 38.5, "Fat": 2.12, "Fiber": 0.0, "Carbs": 1.29, "Sugar": 0.557, "name": "Soy milk, unsweetened, plain, shelf stable"}, {"Salt": 59.6, "Protein": 0.555, "Calories": 14.6, "Fat": 1.22, "Fiber": 0.0, "Carbs": 0.337, "Sugar": 0.0, "name": "Almond milk, unsweetened, plain, shelf stable"}, {"Salt": 111, "Protein": 2.85, "Calories": 26.6, "Fat": 0.619, "Fiber": 1.56, "Carbs": 2.41, "Sugar": 0, "name": "Spinach, baby"}, {"Salt": 107, "Protein": 2.91, "Calories": 27.6, "Fat": 0.604, "Fiber": 1.59, "Carbs": 2.64, "Sugar": 0, "name": "Spinach, mature"}, {"Salt": 0.0, "Protein": 0.696, "Calories": 22.0, "Fat": 0.425, "Fiber": 0.971, "Carbs": 3.84, "Sugar": 0, "name": "Tomato, roma"}, {"Salt": 0.0, "Protein": 11.4, "Calories": 357, "Fat": 1.52, "Fiber": 2.66, "Carbs": 74.4, "Sugar": 0, "name": "Flour, 00"}, {"Salt": 0.0, "Protein": 14.5, "Calories": 364, "Fat": 2.54, "Fiber": 9.34, "Carbs": 70.7, "Sugar": 0, "name": "Flour, spelt, whole grain"}, {"Salt": 0.0, "Protein": 11.7, "Calories": 357, "Fat": 1.6, "Fiber": 3.22, "Carbs": 73.8, "Sugar": 0, "name": "Flour, semolina, coarse and semi-coarse"}, {"Salt": 0.426, "Protein": 13.3, "Calories": 358, "Fat": 1.84, "Fiber": 3.68, "Carbs": 72.0, "Sugar": 0, "name": "Flour, semolina, fine"}, {"Salt": 4.87, "Protein": 0.086, "Calories": 48.4, "Fat": 0.286, "Fiber": 0, "Carbs": 11.4, "Sugar": 10.3, "name": "Apple juice, with added vitamin C, from concentrate, shelf stable"}, {"Salt": 5.23, "Protein": 0.734, "Calories": 47.2, "Fat": 0.325, "Fiber": 0, "Carbs": 10.3, "Sugar": 8.28, "name": "Orange juice, no pulp, not fortified, from concentrate, refrigerated"}, {"Salt": 4.02, "Protein": 0.258, "Calories": 66.1, "Fat": 0.288, "Fiber": 0, "Carbs": 15.6, "Sugar": 14.0, "name": "Grape juice, purple, with added vitamin C, from concentrate, shelf stable"}, {"Salt": 7.19, "Protein": 0.094, "Calories": 66.1, "Fat": 0.265, "Fiber": 0, "Carbs": 15.8, "Sugar": 14.4, "name": "Grape juice, white, with added vitamin C, from concentrate, shelf stable"}, {"Salt": 6.34, "Protein": 0.0, "Calories": 32.1, "Fat": 0.338, "Fiber": 0, "Carbs": 7.26, "Sugar": 3.41, "name": "Cranberry juice, not fortified, from concentrate, shelf stable"}, {"Salt": 1.03, "Protein": 0.57, "Calories": 41.1, "Fat": 0.267, "Fiber": 0, "Carbs": 9.1, "Sugar": 7.12, "name": "Grapefruit juice, red, not fortified, not from concentrate, refrigerated"}, {"Salt": 236, "Protein": 0.859, "Calories": 23.3, "Fat": 0.288, "Fiber": 0, "Carbs": 4.32, "Sugar": 2.57, "name": "Tomato juice, with added ingredients, from concentrate, shelf stable"}, {"Salt": 0.075, "Protein": 0.812, "Calories": 46.5, "Fat": 0.356, "Fiber": 0, "Carbs": 10.0, "Sugar": 8.08, "name": "Orange juice, no pulp, not fortified, not from concentrate, refrigerated"}, {"Salt": 5.31, "Protein": 2.75, "Calories": 32.4, "Fat": 0.312, "Fiber": 1.88, "Carbs": 4.66, "Sugar": 0, "name": "Mushroom, portabella"}, {"Salt": 0.771, "Protein": 2.41, "Calories": 46.4, "Fat": 0.308, "Fiber": 3.01, "Carbs": 8.5, "Sugar": 0, "name": "Mushroom, king oyster"}, {"Salt": 0.417, "Protein": 2.42, "Calories": 44.4, "Fat": 0.245, "Fiber": 2.94, "Carbs": 8.14, "Sugar": 0, "name": "Mushroom, enoki"}, {"Salt": 4.57, "Protein": 3.09, "Calories": 30.2, "Fat": 0.197, "Fiber": 1.78, "Carbs": 4.01, "Sugar": 0, "name": "Mushroom, crimini"}, {"Salt": 0.345, "Protein": 2.2, "Calories": 37.6, "Fat": 0.265, "Fiber": 3.07, "Carbs": 6.6, "Sugar": 0, "name": "Mushroom, maitake"}, {"Salt": 0.891, "Protein": 2.18, "Calories": 39.8, "Fat": 0.449, "Fiber": 3.14, "Carbs": 6.76, "Sugar": 0, "name": "Mushroom, beech"}, {"Salt": 0.0, "Protein": 3.5, "Calories": 39.2, "Fat": 0.24, "Fiber": 2.75, "Carbs": 5.76, "Sugar": 0, "name": "Mushroom, pioppini"}, {"Salt": 39.4, "Protein": 2.78, "Calories": 40.7, "Fat": 1.96, "Fiber": 0.0, "Carbs": 3.0, "Sugar": 0, "name": "Soy milk, unsweetened, plain, refrigerated"}, {"Salt": 59.2, "Protein": 0.656, "Calories": 19.3, "Fat": 1.56, "Fiber": 0.0, "Carbs": 0.671, "Sugar": 0, "name": "Almond milk, unsweetened, plain, refrigerated"}, {"Salt": 42.0, "Protein": 0.797, "Calories": 48.3, "Fat": 2.75, "Fiber": 0.0, "Carbs": 5.1, "Sugar": 2.32, "name": "Oat milk, unsweetened, plain, refrigerated"}, {"Salt": 86.6, "Protein": 0.941, "Calories": 48.0, "Fat": 0.351, "Fiber": 3.1, "Carbs": 10.3, "Sugar": 0, "name": "Carrots, mature, raw"}, {"Salt": 62.7, "Protein": 0.805, "Calories": 40.8, "Fat": 0.138, "Fiber": 2.69, "Carbs": 9.08, "Sugar": 0, "name": "Carrots, baby, raw"}, {"Salt": 0.0, "Protein": 0.715, "Calories": 22.9, "Fat": 0.106, "Fiber": 0.942, "Carbs": 4.78, "Sugar": 0, "name": "Peppers, bell, green, raw"}, {"Salt": 0.0, "Protein": 0.819, "Calories": 30.8, "Fat": 0.121, "Fiber": 1.07, "Carbs": 6.6, "Sugar": 0, "name": "Peppers, bell, yellow, raw"}, {"Salt": 0.0, "Protein": 0.896, "Calories": 31.3, "Fat": 0.126, "Fiber": 1.16, "Carbs": 6.65, "Sugar": 0, "name": "Peppers, bell, red, raw"},
        {"Salt": 0.0, "Protein": 0.882, "Calories": 31.7, "Fat": 0.156, "Fiber": 0.967, "Carbs": 6.7, "Sugar": 0, "name": "Peppers, bell, orange, raw"}, {"Salt": 92.5, "Protein": 3.46, "Calories": 42.8, "Fat": 1.08, "Fiber": 0, "Carbs": 4.81, "Sugar": 0, "name": "Buttermilk, low fat"}, {"Salt": 41.8, "Protein": 3.82, "Calories": 78.0, "Fat": 4.48, "Fiber": 0, "Carbs": 5.57, "Sugar": 4.09, "name": "Yogurt, plain, whole milk"}, {"Salt": 33.8, "Protein": 8.78, "Calories": 93.7, "Fat": 4.39, "Fiber": 0, "Carbs": 4.75, "Sugar": 3.25, "name": "Yogurt, Greek, plain, whole milk"}, {"Salt": 1050.0, "Protein": 30.1, "Calories": 403, "Fat": 29.5, "Fiber": 0, "Carbs": 4.33, "Sugar": 0.638, "name": "Cheese, parmesan, grated, refrigerated"}, {"Salt": 1030.0, "Protein": 19.7, "Calories": 273, "Fat": 19.1, "Fiber": 0, "Carbs": 5.58, "Sugar": 1.63, "name": "Cheese, feta, whole milk, crumbled"}, {"Salt": 0.894, "Protein": 26.2, "Calories": 622, "Fat": 50.2, "Fiber": 9.27, "Carbs": 16.2, "Sugar": 0, "name": "Flour, almond"}, {"Salt": 3.62, "Protein": 13.2, "Calories": 389, "Fat": 6.31, "Fiber": 10.5, "Carbs": 69.9, "Sugar": 0, "name": "Flour, oat, whole grain"}, {"Salt": 47.7, "Protein": 8.11, "Calories": 361, "Fat": 0.951, "Fiber": 5.4, "Carbs": 79.9, "Sugar": 0, "name": "Flour, potato"}, {"Salt": 221, "Protein": 24.0, "Calories": 632, "Fat": 49.4, "Fiber": 6.32, "Carbs": 22.7, "Sugar": 0, "name": "Peanut butter, creamy"}, {"Salt": 63.6, "Protein": 19.7, "Calories": 697, "Fat": 62.4, "Fiber": 8.37, "Carbs": 14.2, "Sugar": 0, "name": "Sesame butter, creamy"}, {"Salt": 0.996, "Protein": 20.8, "Calories": 645, "Fat": 53.0, "Fiber": 9.72, "Carbs": 21.2, "Sugar": 0, "name": "Almond butter, creamy"}, {"Salt": 36.7, "Protein": 18.0, "Calories": 545, "Fat": 37.3, "Fiber": 23.1, "Carbs": 34.4, "Sugar": 0, "name": "Flaxseed, ground"}, {"Salt": 350, "Protein": 11.6, "Calories": 103, "Fat": 4.22, "Fiber": 0, "Carbs": 4.6, "Sugar": 0, "name": "Cottage cheese, full fat, large or small curd"}, {"Salt": 368, "Protein": 5.79, "Calories": 343, "Fat": 33.5, "Fiber": 0, "Carbs": 4.56, "Sugar": 0, "name": "Cream cheese, full fat, block"}, {"Salt": 20.6, "Protein": 2.02, "Calories": 343, "Fat": 35.6, "Fiber": 0, "Carbs": 3.8, "Sugar": 0, "name": "Cream, heavy"}, {"Salt": 50.0, "Protein": 3.07, "Calories": 196, "Fat": 18.0, "Fiber": 0, "Carbs": 5.56, "Sugar": 0, "name": "Cream, sour, full fat"}, {"Salt": 16.1, "Protein": 0.742, "Calories": 17.1, "Fat": 0.074, "Fiber": 0, "Carbs": 3.37, "Sugar": 0, "name": "Lettuce, iceberg, raw"}, {"Salt": 23.0, "Protein": 0.977, "Calories": 20.8, "Fat": 0.071, "Fiber": 0, "Carbs": 4.06, "Sugar": 0, "name": "Lettuce, romaine, green, raw"}, {"Salt": 24.9, "Protein": 0.883, "Calories": 17.5, "Fat": 0.106, "Fiber": 0, "Carbs": 3.26, "Sugar": 0, "name": "Lettuce, leaf, red, raw"}, {"Salt": 28.9, "Protein": 1.09, "Calories": 22.0, "Fat": 0.156, "Fiber": 0, "Carbs": 4.07, "Sugar": 0, "name": "Lettuce, leaf, green, raw"}, {"Salt": 0.0, "Protein": 15.7, "Calories": 689, "Fat": 61.3, "Fiber": 3.94, "Carbs": 18.6, "Sugar": 0, "name": "Nuts, pine nuts, raw"}, {"Salt": 0.0, "Protein": 21.5, "Calories": 626, "Fat": 51.1, "Fiber": 10.8, "Carbs": 20.0, "Sugar": 0, "name": "Nuts, almonds, whole, raw"}, {"Salt": 0.0, "Protein": 14.6, "Calories": 730, "Fat": 69.7, "Fiber": 5.21, "Carbs": 10.9, "Sugar": 0, "name": "Nuts, walnuts, English, halves, raw"}, {"Salt": 0.0, "Protein": 9.96, "Calories": 750, "Fat": 73.3, "Fiber": 5.79, "Carbs": 12.7, "Sugar": 0, "name": "Nuts, pecans, halves, raw"}, {"Salt": 0.668, "Protein": 13.5, "Calories": 382, "Fat": 5.89, "Fiber": 0, "Carbs": 68.7, "Sugar": 0, "name": "Oats, whole grain, rolled, old fashioned"}, {"Salt": 0.311, "Protein": 12.5, "Calories": 381, "Fat": 5.8, "Fiber": 0, "Carbs": 69.8, "Sugar": 0, "name": "Oats, whole grain, steel cut"}, {"Salt": 0.0, "Protein": 0.461, "Calories": 60.1, "Fat": 0.211, "Fiber": 0.935, "Carbs": 14.1, "Sugar": 11.4, "name": "Pineapple, raw"}, {"Salt": 0.0, "Protein": 1.04, "Calories": 70.5, "Fat": 0.192, "Fiber": 0, "Carbs": 16.2, "Sugar": 13.9, "name": "Cherries, sweet, dark red, raw"}, {"Salt": 0.0, "Protein": 1.97, "Calories": 40.0, "Fat": 0.275, "Fiber": 3.01, "Carbs": 7.41, "Sugar": 2.33, "name": "Beans, snap, green, raw"}, {"Salt": 2.74, "Protein": 2.27, "Calories": 83.4, "Fat": 0.36, "Fiber": 0, "Carbs": 17.8, "Sugar": 0.526, "name": "Potatoes, russet, without skin, raw"}, {"Salt": 2.86, "Protein": 2.06, "Calories": 75.6, "Fat": 0.248, "Fiber": 0, "Carbs": 16.3, "Sugar": 0.664, "name": "Potatoes, red, without skin, raw"}, {"Salt": 2.24, "Protein": 1.81, "Calories": 73.5, "Fat": 0.264, "Fiber": 0, "Carbs": 16.0, "Sugar": 0.645, "name": "Potatoes, gold, without skin, raw"}, {"Salt": 0.0, "Protein": 1.58, "Calories": 79.0, "Fat": 0.375, "Fiber": 0, "Carbs": 17.3, "Sugar": 6.06, "name": "Sweet potatoes, orange flesh, without skin, raw"}, {"Salt": 97.2, "Protein": 0.492, "Calories": 16.7, "Fat": 0.162, "Fiber": 0, "Carbs": 3.32, "Sugar": 0, "name": "Celery, raw"}, {"Salt": 1.52, "Protein": 0.625, "Calories": 15.9, "Fat": 0.178, "Fiber": 0, "Carbs": 2.95, "Sugar": 0, "name": "Cucumber, with peel, raw"}, {"Salt": 16.1, "Protein": 0.961, "Calories": 31.4, "Fat": 0.228, "Fiber": 0, "Carbs": 6.38, "Sugar": 0, "name": "Cabbage, green, raw"}, {"Salt": 11.7, "Protein": 1.24, "Calories": 34.1, "Fat": 0.214, "Fiber": 0, "Carbs": 6.79, "Sugar": 0, "name": "Cabbage, red, raw"}, {"Salt": 0.0, "Protein": 0.641, "Calories": 36.4, "Fat": 0.22, "Fiber": 0, "Carbs": 7.96, "Sugar": 4.86, "name": "Strawberries, raw"}, {"Salt": 0.0, "Protein": 1.01, "Calories": 57.3, "Fat": 0.188, "Fiber": 0, "Carbs": 12.9, "Sugar": 2.68, "name": "Raspberries, raw"}, {"Salt": 0.0, "Protein": 0.703, "Calories": 63.9, "Fat": 0.306, "Fiber": 0, "Carbs": 14.6, "Sugar": 9.36, "name": "Blueberries, raw"}, {"Salt": 7.0, "Protein": 0.914, "Calories": 85.9, "Fat": 0.164, "Fiber": 0, "Carbs": 20.2, "Sugar": 17.3, "name": "Grapes, red, seedless, raw"}, {"Salt": 3.17, "Protein": 0.899, "Calories": 80.1, "Fat": 0.232, "Fiber": 0, "Carbs": 18.6, "Sugar": 16.1, "name": "Grapes, green, seedless, raw"}, {"Salt": 0.504, "Protein": 0.273, "Calories": 51.6, "Fat": 0.162, "Fiber": 0, "Carbs": 12.3, "Sugar": 9.66, "name": "Applesauce, unsweetened, with added vitamin C"}]
NutriList = ["Calories", "Protein", "Carbs", "Fat",
             "Fiber", "Salt", "Sugar"]

FoodList = []
FoodNames = []
for i in range(len(Food)):

    FoodNutri = []
    for j in range(7):
        FoodNutri.append(Food[i][NutriList[j]])
    FoodList.append(FoodNutri)
    FoodNames.append(Food[i]["name"])


def retrieveFood(request):

    n = len(FoodList)
    H = []
    for i in range(7):
        H.append(request["{}".format(NutriList[i])])
    H = np.array(H)
    x0 = np.zeros(n)

    def objective(x):
        return np.linalg.norm(H - np.dot(x, np.array(FoodList)), ord=2)

    # def constraint1(x):
    #     return bucket_capacity - np.sum(x)

    # def constraint2(x):
    #     return bucket_capacity * rocks.T - np.dot(x, rocks.T)

    # cons = [{'type': 'ineq', 'fun': constraint1},
    #         {'type': 'ineq', 'fun': constraint2}]
    bounds = [(0, 2)] * n
    for foodName in range(len(FoodNames)):
        for food in range(len(request["foods"])):

            if FoodNames[foodName] == request["foods"][food]["name"]:
                bounds[foodName] = (-request["foods"][food]["weight"] /
                                    200, min([request["foods"][food]["weight"]/200, 2]))

    res = minimize(objective, x0, bounds=bounds)
    results = {}
    for i in range(len(res.x)):
        if res.x[i] < 0 or res.x[i] > 0.5:
            results[FoodNames[i]] = (res.x)[i]*100
    return results


result = retrieveFood({
    "Calories": -6508,
    "Protein": 105.8,
    "Carbs": -1995,
    "Fat": 35.7,
    "Fiber": -267,
    "Salt": -145.5,
    "Sugar": -1959,
    "foods": [
        {
            "name": "Apples, fuji, with skin, raw",
            "weight": 15000
        }
    ]
})
print(result)
# print(result.success)  # Whether the optimization was successful
# print(result.x[0])  # Binary variables indicating which rocks were used
# Cumulated characteristics of the rocks in
# print(np.dot(result.x,  np.array(FoodList)))
# print(result)
