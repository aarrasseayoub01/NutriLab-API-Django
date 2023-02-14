import cvxpy as cp


def Algo():
    FoodNames = []
    for food in [0, 1, 2]:
        FoodNames.append(cp.Variable())

    # Define the constraints
    constraints = [[10, 5]*FoodNames[0] + [2, 12]*FoodNames[1] + [4, 8]*FoodNames[2] >= [12, 588],
                   FoodNames[0] >= 0,
                   FoodNames[1] >= 0,
                   FoodNames[2] >= 0]

    # Define the objective function
    obj = cp.Minimize(2*FoodNames[0] + 3*FoodNames[1] + FoodNames[2])

    # Define the problem
    prob = cp.Problem(obj, constraints)

    # Solve the problem using the Interior Point Method
    prob.solve(solver=cp.CVXOPT)

    # Print the results
    print("Optimal values: x = {}, y = {}, z = {}".format(
        FoodNames[0].value, FoodNames[1].value, FoodNames[2].value))
    return ("Optimal values: x = {}, y = {}, z = {}".format(
        FoodNames[0].value, FoodNames[1].value, FoodNames[2].value))


Algo()

Food = [{
        "name": "Hummus, commercial",
        "Protein": 7.35,
        "Calories": 0.0,
        "Fat": 17.1,
        "Fiber": 5.4,
        "Carbs": 14.9,
        "Salt": 438.0,
        "Sugar": 0.34
        },
        {
        "name": "Tomatoes, grape, raw",
        "Protein": 0.83,
        "Calories": 0.0,
        "Fat": 0.63,
        "Fiber": 2.1,
        "Carbs": 5.51,
        "Salt": 6.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, snap, green, canned, regular pack, drained solids",
        "Protein": 1.04,
        "Calories": 0.0,
        "Fat": 0.39,
        "Fiber": 0.0,
        "Carbs": 4.11,
        "Salt": 282.0,
        "Sugar": 1.29
        },
        {
        "name": "Frankfurter, beef, unheated",
        "Protein": 11.7,
        "Calories": 0.0,
        "Fat": 28.0,
        "Fiber": 0.0,
        "Carbs": 2.89,
        "Salt": 872.0,
        "Sugar": 1.26
        },
        {
        "name": "Nuts, almonds, dry roasted, with salt added",
        "Protein": 20.4,
        "Calories": 0.0,
        "Fat": 57.8,
        "Fiber": 11.0,
        "Carbs": 16.2,
        "Salt": 256.0,
        "Sugar": 4.17
        },
        {
        "name": "Kale, raw",
        "Protein": 2.92,
        "Calories": 0.0,
        "Fat": 1.49,
        "Fiber": 4.1,
        "Carbs": 4.42,
        "Salt": 53.0,
        "Sugar": 0.8
        },
        {
        "name": "Egg, whole, raw, frozen, pasteurized",
        "Protein": 12.3,
        "Calories": 0.0,
        "Fat": 10.3,
        "Fiber": 0.0,
        "Carbs": 0.91,
        "Salt": 121.0,
        "Sugar": 0.0
        },
        {
        "name": "Egg, white, raw, frozen, pasteurized",
        "Protein": 10.1,
        "Calories": 0.0,
        "Fat": 0.16,
        "Fiber": 0.0,
        "Carbs": 0.74,
        "Salt": 144.0,
        "Sugar": 0.0
        },
        {
        "name": "Egg, white, dried",
        "Protein": 79.9,
        "Calories": 0.0,
        "Fat": 0.65,
        "Fiber": 0.0,
        "Carbs": 6.02,
        "Salt": 1250.0,
        "Sugar": 0.0
        },
        {
        "name": "Onion rings, breaded, par fried, frozen, prepared, heated in oven",
        "Protein": 4.52,
        "Calories": 0.0,
        "Fat": 14.4,
        "Fiber": 2.4,
        "Carbs": 36.3,
        "Salt": 374.0,
        "Sugar": 4.5
        },
        {
        "name": "Pickles, cucumber, dill or kosher dill",
        "Protein": 0.48,
        "Calories": 0.0,
        "Fat": 0.43,
        "Fiber": 1.0,
        "Carbs": 1.99,
        "Salt": 808.0,
        "Sugar": 1.28
        },
        {
        "name": "Cheese, parmesan, grated",
        "Protein": 29.6,
        "Calories": 0.0,
        "Fat": 28.0,
        "Fiber": 0.0,
        "Carbs": 12.4,
        "Salt": 1750.0,
        "Sugar": 0.07
        },
        {
        "name": "Cheese, pasteurized process, American, vitamin D fortified",
        "Protein": 18.0,
        "Calories": 0.0,
        "Fat": 30.6,
        "Fiber": 0.0,
        "Carbs": 5.27,
        "Salt": 1660.0,
        "Sugar": 2.63
        },
        {
        "name": "Grapefruit juice, white, canned or bottled, unsweetened",
        "Protein": 0.55,
        "Calories": 0.0,
        "Fat": 0.7,
        "Fiber": 0.2,
        "Carbs": 7.59,
        "Salt": 1.0,
        "Sugar": 7.72
        },
        {
        "name": "Peaches, yellow, raw",
        "Protein": 0.91,
        "Calories": 0.0,
        "Fat": 0.27,
        "Fiber": 1.5,
        "Carbs": 10.1,
        "Salt": 13.0,
        "Sugar": 8.39
        },
        {
        "name": "Seeds, sunflower seed kernels, dry roasted, with salt added",
        "Protein": 21.0,
        "Calories": 0.0,
        "Fat": 56.1,
        "Fiber": 10.3,
        "Carbs": 17.1,
        "Salt": 532.0,
        "Sugar": 3.14
        },
        {
        "name": "Bread, white, commercially prepared",
        "Protein": 9.43,
        "Calories": 0.0,
        "Fat": 3.59,
        "Fiber": 2.3,
        "Carbs": 49.2,
        "Salt": 477.0,
        "Sugar": 5.34
        },
        {
        "name": "Kale, frozen, cooked, boiled, drained, without salt",
        "Protein": 2.94,
        "Calories": 0.0,
        "Fat": 1.21,
        "Fiber": 0.0,
        "Carbs": 5.3,
        "Salt": 16.0,
        "Sugar": 1.12
        },
        {
        "name": "Mustard, prepared, yellow",
        "Protein": 4.25,
        "Calories": 0.0,
        "Fat": 3.38,
        "Fiber": 4.3,
        "Carbs": 5.3,
        "Salt": 1100.0,
        "Sugar": 1.42
        },
        {
        "name": "Kiwifruit, green, raw",
        "Protein": 1.06,
        "Calories": 0.0,
        "Fat": 0.44,
        "Fiber": 3.0,
        "Carbs": 14.0,
        "Salt": 5.0,
        "Sugar": 8.99
        },
        {
        "name": "Nectarines, raw",
        "Protein": 1.06,
        "Calories": 0.0,
        "Fat": 0.28,
        "Fiber": 1.5,
        "Carbs": 9.18,
        "Salt": 13.0,
        "Sugar": 7.89
        },
        {
        "name": "Cheese, cheddar",
        "Protein": 23.3,
        "Calories": 0.0,
        "Fat": 34.0,
        "Fiber": 0.0,
        "Carbs": 2.44,
        "Salt": 654.0,
        "Sugar": 0.33
        },
        {
        "name": "Cheese, cottage, lowfat, 2% milkfat",
        "Protein": 11.0,
        "Calories": 0.0,
        "Fat": 2.3,
        "Fiber": 0.0,
        "Carbs": 4.31,
        "Salt": 321.0,
        "Sugar": 4.1
        },
        {
        "name": "Cheese, mozzarella, low moisture, part-skim",
        "Protein": 23.7,
        "Calories": 0.0,
        "Fat": 20.4,
        "Fiber": 0.0,
        "Carbs": 4.44,
        "Salt": 699.0,
        "Sugar": 1.81
        },
        {
        "name": "Egg, whole, dried",
        "Protein": 48.1,
        "Calories": 0.0,
        "Fat": 39.8,
        "Fiber": 0.0,
        "Carbs": 1.87,
        "Salt": 485.0,
        "Sugar": 0.0
        },
        {
        "name": "Egg, yolk, raw, frozen, pasteurized",
        "Protein": 15.6,
        "Calories": 0.0,
        "Fat": 25.1,
        "Fiber": 0.0,
        "Carbs": 0.59,
        "Salt": 66.0,
        "Sugar": 0.0
        },
        {
        "name": "Egg, yolk, dried",
        "Protein": 34.2,
        "Calories": 0.0,
        "Fat": 55.5,
        "Fiber": 0.0,
        "Carbs": 1.07,
        "Salt": 149.0,
        "Sugar": 0.0
        },
        {
        "name": "Yogurt, Greek, plain, nonfat",
        "Protein": 10.3,
        "Calories": 0.0,
        "Fat": 0.37,
        "Fiber": 0.0,
        "Carbs": 3.64,
        "Salt": 36.0,
        "Sugar": 3.27
        },
        {
        "name": "Yogurt, Greek, strawberry, nonfat",
        "Protein": 8.06,
        "Calories": 0.0,
        "Fat": 0.15,
        "Fiber": 0.6,
        "Carbs": 12.2,
        "Salt": 32.0,
        "Sugar": 11.5
        },
        {
        "name": "Oil, coconut",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 99.1,
        "Fiber": 0.0,
        "Carbs": 0.84,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Chicken, broilers or fryers, drumstick, meat only, cooked, braised",
        "Protein": 23.9,
        "Calories": 0.0,
        "Fat": 5.95,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 117.0,
        "Sugar": 0.0
        },
        {
        "name": "Chicken, broiler or fryers, breast, skinless, boneless, meat only, cooked, braised",
        "Protein": 32.1,
        "Calories": 0.0,
        "Fat": 3.24,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 47.0,
        "Sugar": 0.0
        },
        {
        "name": "Sauce, pasta, spaghetti/marinara, ready-to-serve",
        "Protein": 1.41,
        "Calories": 0.0,
        "Fat": 1.48,
        "Fiber": 1.8,
        "Carbs": 8.05,
        "Salt": 419.0,
        "Sugar": 5.5
        },
        {
        "name": "Ham, sliced, pre-packaged, deli meat (96%fat free, water added)",
        "Protein": 16.7,
        "Calories": 0.0,
        "Fat": 3.73,
        "Fiber": 0.0,
        "Carbs": 0.27,
        "Salt": 1040.0,
        "Sugar": 0.0
        },
        {
        "name": "Olives, green, Manzanilla, stuffed with pimiento",
        "Protein": 1.15,
        "Calories": 0.0,
        "Fat": 12.9,
        "Fiber": 4.0,
        "Carbs": 4.96,
        "Salt": 1620.0,
        "Sugar": 0.0
        },
        {
        "name": "Cookies, oatmeal, soft, with raisins",
        "Protein": 5.79,
        "Calories": 0.0,
        "Fat": 14.3,
        "Fiber": 3.3,
        "Carbs": 69.6,
        "Salt": 314.0,
        "Sugar": 34.8
        },
        {
        "name": "Tomatoes, canned, red, ripe, diced",
        "Protein": 0.84,
        "Calories": 0.0,
        "Fat": 0.5,
        "Fiber": 0.0,
        "Carbs": 3.32,
        "Salt": 125.0,
        "Sugar": 2.99
        },
        {
        "name": "Fish, haddock, raw",
        "Protein": 16.3,
        "Calories": 0.0,
        "Fat": 0.45,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 213.0,
        "Sugar": 0.0
        },
        {
        "name": "Fish, pollock, raw",
        "Protein": 12.3,
        "Calories": 0.0,
        "Fat": 0.41,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 333.0,
        "Sugar": 0.0
        },
        {
        "name": "Fish, tuna, light, canned in water, drained solids",
        "Protein": 19.0,
        "Calories": 0.0,
        "Fat": 0.94,
        "Fiber": 0.0,
        "Carbs": 0.08,
        "Salt": 219.0,
        "Sugar": 0.0
        },
        {
        "name": "Restaurant, Chinese, fried rice, without meat",
        "Protein": 3.84,
        "Calories": 0.0,
        "Fat": 3.19,
        "Fiber": 0.0,
        "Carbs": 32.5,
        "Salt": 361.0,
        "Sugar": 0.62
        },
        {
        "name": "Restaurant, Latino, tamale, pork",
        "Protein": 7.38,
        "Calories": 0.0,
        "Fat": 9.04,
        "Fiber": 2.4,
        "Carbs": 15.8,
        "Salt": 473.0,
        "Sugar": 0.46
        },
        {
        "name": "Restaurant, Latino, pupusas con frijoles (pupusas, bean)",
        "Protein": 5.59,
        "Calories": 0.0,
        "Fat": 9.01,
        "Fiber": 5.8,
        "Carbs": 31.5,
        "Salt": 305.0,
        "Sugar": 1.3
        },
        {
        "name": "Bread, whole-wheat, commercially prepared",
        "Protein": 12.3,
        "Calories": 0.0,
        "Fat": 3.55,
        "Fiber": 6.0,
        "Carbs": 43.1,
        "Salt": 450.0,
        "Sugar": 4.41
        },
        {
        "name": "Beef, loin, tenderloin roast, separable lean only, boneless, trimmed to 0\" fat, select, cooked, roasted",
        "Protein": 27.7,
        "Calories": 0.0,
        "Fat": 6.36,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 54.0,
        "Sugar": 0.0
        },
        {
        "name": "Beef, loin, top loin steak, boneless, lip-on, separable lean only, trimmed to 1/8\" fat, choice, raw",
        "Protein": 22.8,
        "Calories": 0.0,
        "Fat": 6.39,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 45.0,
        "Sugar": 0.0
        },
        {
        "name": "Beef, round, eye of round roast, boneless, separable lean only, trimmed to 0\" fat, select, raw",
        "Protein": 23.4,
        "Calories": 0.0,
        "Fat": 2.48,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 50.0,
        "Sugar": 0.0
        },
        {
        "name": "Beef, round, top round roast, boneless, separable lean only, trimmed to 0\" fat, select, raw",
        "Protein": 23.7,
        "Calories": 0.0,
        "Fat": 2.41,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 55.0,
        "Sugar": 0.0
        },
        {
        "name": "Beef, short loin, porterhouse steak, separable lean only, trimmed to 1/8\" fat, select, raw",
        "Protein": 22.7,
        "Calories": 0.0,
        "Fat": 5.32,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 43.0,
        "Sugar": 0.0
        },
        {
        "name": "Beef, short loin, t-bone steak, bone-in, separable lean only, trimmed to 1/8\" fat, choice, cooked, grilled",
        "Protein": 27.3,
        "Calories": 0.0,
        "Fat": 11.4,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 67.0,
        "Sugar": 0.0
        },
        {
        "name": "Carrots, frozen, unprepared",
        "Protein": 0.81,
        "Calories": 0.0,
        "Fat": 0.47,
        "Fiber": 3.2,
        "Carbs": 7.92,
        "Salt": 66.0,
        "Sugar": 4.2
        },
        {
        "name": "Cheese, dry white, queso seco",
        "Protein": 24.5,
        "Calories": 0.0,
        "Fat": 24.3,
        "Fiber": 0.0,
        "Carbs": 2.07,
        "Salt": 1810.0,
        "Sugar": 0.43
        },
        {
        "name": "Cheese, ricotta, whole milk",
        "Protein": 7.81,
        "Calories": 0.0,
        "Fat": 11.0,
        "Fiber": 0.0,
        "Carbs": 6.86,
        "Salt": 105.0,
        "Sugar": 0.0
        },
        {
        "name": "Cheese, swiss",
        "Protein": 27.0,
        "Calories": 0.0,
        "Fat": 31.0,
        "Fiber": 0.0,
        "Carbs": 1.44,
        "Salt": 185.0,
        "Sugar": 0.0
        },
        {
        "name": "Figs, dried, uncooked",
        "Protein": 3.3,
        "Calories": 0.0,
        "Fat": 0.92,
        "Fiber": 9.8,
        "Carbs": 63.9,
        "Salt": 10.0,
        "Sugar": 47.9
        },
        {
        "name": "Lettuce, cos or romaine, raw",
        "Protein": 1.24,
        "Calories": 0.0,
        "Fat": 0.26,
        "Fiber": 1.8,
        "Carbs": 3.24,
        "Salt": 0.0,
        "Sugar": 1.19
        },
        {
        "name": "Melons, cantaloupe, raw",
        "Protein": 0.82,
        "Calories": 0.0,
        "Fat": 0.18,
        "Fiber": 0.8,
        "Carbs": 8.16,
        "Salt": 30.0,
        "Sugar": 7.88
        },
        {
        "name": "Oranges, raw, navels",
        "Protein": 0.91,
        "Calories": 0.0,
        "Fat": 0.15,
        "Fiber": 2.0,
        "Carbs": 11.8,
        "Salt": 9.0,
        "Sugar": 8.57
        },
        {
        "name": "Milk, lowfat, fluid, 1% milkfat, with added vitamin A and vitamin D",
        "Protein": 3.38,
        "Calories": 0.0,
        "Fat": 0.95,
        "Fiber": 0.0,
        "Carbs": 5.18,
        "Salt": 39.0,
        "Sugar": 4.96
        },
        {
        "name": "Pears, raw, bartlett",
        "Protein": 0.38,
        "Calories": 0.0,
        "Fat": 0.16,
        "Fiber": 3.1,
        "Carbs": 15.1,
        "Salt": 7.0,
        "Sugar": 9.69
        },
        {
        "name": "Restaurant, Chinese, sweet and sour pork",
        "Protein": 8.88,
        "Calories": 0.0,
        "Fat": 13.6,
        "Fiber": 1.0,
        "Carbs": 25.5,
        "Salt": 304.0,
        "Sugar": 10.3
        },
        {
        "name": "Salt, table, iodized",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 38700.0,
        "Sugar": 0.0
        },
        {
        "name": "Milk, nonfat, fluid, with added vitamin A and vitamin D (fat free or skim)",
        "Protein": 3.43,
        "Calories": 0.0,
        "Fat": 0.08,
        "Fiber": 0.0,
        "Carbs": 4.92,
        "Salt": 41.0,
        "Sugar": 5.05
        },
        {
        "name": "Sauce, salsa, ready-to-serve",
        "Protein": 1.44,
        "Calories": 0.0,
        "Fat": 0.19,
        "Fiber": 1.8,
        "Carbs": 6.74,
        "Salt": 656.0,
        "Sugar": 3.81
        },
        {
        "name": "Milk, reduced fat, fluid, 2% milkfat, with added vitamin A and vitamin D",
        "Protein": 3.36,
        "Calories": 0.0,
        "Fat": 1.9,
        "Fiber": 0.0,
        "Carbs": 4.9,
        "Salt": 39.0,
        "Sugar": 4.89
        },
        {
        "name": "Sausage, breakfast sausage, beef, pre-cooked, unprepared",
        "Protein": 13.3,
        "Calories": 0.0,
        "Fat": 28.7,
        "Fiber": 0.0,
        "Carbs": 3.37,
        "Salt": 866.0,
        "Sugar": 1.0
        },
        {
        "name": "Sausage, Italian, pork, mild, cooked, pan-fried",
        "Protein": 18.2,
        "Calories": 0.0,
        "Fat": 26.2,
        "Fiber": 0.0,
        "Carbs": 2.15,
        "Salt": 766.0,
        "Sugar": 1.46
        },
        {
        "name": "Sausage, pork, chorizo, link or ground, cooked, pan-fried",
        "Protein": 19.3,
        "Calories": 0.0,
        "Fat": 28.1,
        "Fiber": 0.0,
        "Carbs": 2.63,
        "Salt": 983.0,
        "Sugar": 0.0
        },
        {
        "name": "Milk, whole, 3.25% milkfat, with added vitamin D",
        "Protein": 3.27,
        "Calories": 0.0,
        "Fat": 3.2,
        "Fiber": 0.0,
        "Carbs": 4.63,
        "Salt": 38.0,
        "Sugar": 4.81
        },
        {
        "name": "Sausage, turkey, breakfast links, mild, raw",
        "Protein": 16.7,
        "Calories": 0.0,
        "Fat": 10.4,
        "Fiber": 0.0,
        "Carbs": 0.93,
        "Salt": 599.0,
        "Sugar": 0.0
        },
        {
        "name": "Sugars, granulated",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.32,
        "Fiber": 0.0,
        "Carbs": 99.6,
        "Salt": 1.0,
        "Sugar": 99.8
        },
        {
        "name": "Turkey, ground, 93% lean, 7% fat, pan-broiled crumbles",
        "Protein": 27.1,
        "Calories": 0.0,
        "Fat": 11.6,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 90.0,
        "Sugar": 0.0
        },
        {
        "name": "Ham, sliced, restaurant",
        "Protein": 19.6,
        "Calories": 0.0,
        "Fat": 3.68,
        "Fiber": 0.0,
        "Carbs": 2.36,
        "Salt": 1030.0,
        "Sugar": 2.2
        },
        {
        "name": "Cheese, American, restaurant",
        "Protein": 17.5,
        "Calories": 0.0,
        "Fat": 31.1,
        "Fiber": 0.0,
        "Carbs": 6.35,
        "Salt": 1600.0,
        "Sugar": 3.76
        },
        {
        "name": "Beans, Dry, Medium Red (0% moisture)",
        "Protein": 25.5,
        "Calories": 0.0,
        "Fat": 1.04,
        "Fiber": 4.3,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Red (0% moisture)",
        "Protein": 21.3,
        "Calories": 0.0,
        "Fat": 1.16,
        "Fiber": 4.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Flor de Mayo (0% moisture)",
        "Protein": 23.3,
        "Calories": 0.0,
        "Fat": 0.86,
        "Fiber": 4.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Brown (0% moisture)",
        "Protein": 25.6,
        "Calories": 0.0,
        "Fat": 1.12,
        "Fiber": 4.1,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Tan (0% moisture)",
        "Protein": 26.8,
        "Calories": 0.0,
        "Fat": 1.14,
        "Fiber": 4.4,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Light Tan (0% moisture)",
        "Protein": 24.6,
        "Calories": 0.0,
        "Fat": 1.28,
        "Fiber": 4.3,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Carioca (0% moisture)",
        "Protein": 25.2,
        "Calories": 0.0,
        "Fat": 1.44,
        "Fiber": 4.5,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Cranberry (0% moisture)",
        "Protein": 24.4,
        "Calories": 0.0,
        "Fat": 1.23,
        "Fiber": 4.3,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Light Red Kidney (0% moisture)",
        "Protein": 25.0,
        "Calories": 0.0,
        "Fat": 1.03,
        "Fiber": 4.5,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Pink (0% moisture)",
        "Protein": 23.4,
        "Calories": 0.0,
        "Fat": 1.2,
        "Fiber": 4.1,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Dark Red Kidney (0% moisture)",
        "Protein": 25.9,
        "Calories": 0.0,
        "Fat": 1.31,
        "Fiber": 4.3,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Navy (0% moisture)",
        "Protein": 24.1,
        "Calories": 0.0,
        "Fat": 1.51,
        "Fiber": 4.3,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Small White (0% moisture)",
        "Protein": 24.5,
        "Calories": 0.0,
        "Fat": 1.32,
        "Fiber": 4.3,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Small Red (0% moisture)",
        "Protein": 23.5,
        "Calories": 0.0,
        "Fat": 1.28,
        "Fiber": 4.1,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Black (0% moisture)",
        "Protein": 24.4,
        "Calories": 0.0,
        "Fat": 1.45,
        "Fiber": 4.2,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Pinto (0% moisture)",
        "Protein": 23.7,
        "Calories": 0.0,
        "Fat": 1.24,
        "Fiber": 4.1,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Beans, Dry, Great Northern (0% moisture)",
        "Protein": 24.7,
        "Calories": 0.0,
        "Fat": 1.24,
        "Fiber": 4.3,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Broccoli, raw",
        "Protein": 2.57,
        "Calories": 0.0,
        "Fat": 0.34,
        "Fiber": 2.4,
        "Carbs": 6.27,
        "Salt": 36.0,
        "Sugar": 1.4
        },
        {
        "name": "Ketchup, restaurant",
        "Protein": 1.11,
        "Calories": 0.0,
        "Fat": 0.55,
        "Fiber": 0.0,
        "Carbs": 26.8,
        "Salt": 949.0,
        "Sugar": 21.8
        },
        {
        "name": "Eggs, Grade A, Large, egg white",
        "Protein": 10.7,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 2.36,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Eggs, Grade A, Large, egg yolk",
        "Protein": 16.2,
        "Calories": 0.0,
        "Fat": 28.8,
        "Fiber": 0.0,
        "Carbs": 1.02,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Oil, canola",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Oil, corn",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Oil, soybean",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Oil, olive, extra virgin",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Eggs, Grade A, Large, egg whole",
        "Protein": 12.4,
        "Calories": 0.0,
        "Fat": 9.96,
        "Fiber": 0.0,
        "Carbs": 0.96,
        "Salt": 129.0,
        "Sugar": 0.2
        },
        {
        "name": "Pork, cured, bacon, cooked, restaurant",
        "Protein": 40.9,
        "Calories": 0.0,
        "Fat": 36.5,
        "Fiber": 0.0,
        "Carbs": 2.1,
        "Salt": 1830.0,
        "Sugar": 3.14
        },
        {
        "name": "Butter, stick, unsalted",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 81.5,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 10.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, wheat, all-purpose, enriched, bleached",
        "Protein": 10.9,
        "Calories": 0.0,
        "Fat": 1.48,
        "Fiber": 0.0,
        "Carbs": 77.3,
        "Salt": 2.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, wheat, all-purpose, enriched, unbleached",
        "Protein": 13.1,
        "Calories": 0.0,
        "Fat": 1.48,
        "Fiber": 0.0,
        "Carbs": 73.2,
        "Salt": 4.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, wheat, all-purpose, unenriched, unbleached",
        "Protein": 12.0,
        "Calories": 0.0,
        "Fat": 1.7,
        "Fiber": 3.0,
        "Carbs": 74.6,
        "Salt": 2.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, whole wheat, unenriched",
        "Protein": 15.1,
        "Calories": 0.0,
        "Fat": 2.73,
        "Fiber": 10.6,
        "Carbs": 71.2,
        "Salt": 3.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, bread, white, enriched, unbleached",
        "Protein": 14.3,
        "Calories": 0.0,
        "Fat": 1.65,
        "Fiber": 0.0,
        "Carbs": 72.8,
        "Salt": 3.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, rice, white, unenriched",
        "Protein": 6.94,
        "Calories": 0.0,
        "Fat": 1.3,
        "Fiber": 0.5,
        "Carbs": 79.8,
        "Salt": 5.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, corn, yellow, fine meal, enriched",
        "Protein": 6.2,
        "Calories": 0.0,
        "Fat": 1.74,
        "Fiber": 4.3,
        "Carbs": 80.8,
        "Salt": 0.0,
        "Sugar": 1.04
        },
        {
        "name": "Butter, stick, salted",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 82.2,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 524.0,
        "Sugar": 0.58
        },
        {
        "name": "Onions, red, raw",
        "Protein": 0.94,
        "Calories": 0.0,
        "Fat": 0.1,
        "Fiber": 2.2,
        "Carbs": 9.93,
        "Salt": 1.0,
        "Sugar": 5.76
        },
        {
        "name": "Onions, yellow, raw",
        "Protein": 0.83,
        "Calories": 0.0,
        "Fat": 0.05,
        "Fiber": 1.9,
        "Carbs": 8.61,
        "Salt": 1.0,
        "Sugar": 5.82
        },
        {
        "name": "Garlic, raw",
        "Protein": 6.62,
        "Calories": 0.0,
        "Fat": 0.38,
        "Fiber": 2.7,
        "Carbs": 28.2,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, soy, defatted",
        "Protein": 51.1,
        "Calories": 0.0,
        "Fat": 3.33,
        "Fiber": 0.0,
        "Carbs": 32.9,
        "Salt": 2.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, soy, full-fat",
        "Protein": 38.6,
        "Calories": 0.0,
        "Fat": 20.7,
        "Fiber": 0.0,
        "Carbs": 27.9,
        "Salt": 2.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, rice, brown",
        "Protein": 7.19,
        "Calories": 0.0,
        "Fat": 3.85,
        "Fiber": 0.0,
        "Carbs": 75.5,
        "Salt": 1.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, rice, glutinous",
        "Protein": 6.69,
        "Calories": 0.0,
        "Fat": 1.16,
        "Fiber": 0.0,
        "Carbs": 80.1,
        "Salt": 6.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, pastry, unenriched, unbleached",
        "Protein": 8.75,
        "Calories": 0.0,
        "Fat": 1.64,
        "Fiber": 0.0,
        "Carbs": 77.2,
        "Salt": 1.0,
        "Sugar": 0.0
        },
        {
        "name": "Onions, white, raw",
        "Protein": 0.89,
        "Calories": 0.0,
        "Fat": 0.13,
        "Fiber": 1.2,
        "Carbs": 7.68,
        "Salt": 2.0,
        "Sugar": 5.76
        },
        {
        "name": "Bananas, overripe, raw",
        "Protein": 0.73,
        "Calories": 0.0,
        "Fat": 0.22,
        "Fiber": 1.7,
        "Carbs": 20.1,
        "Salt": 0.0,
        "Sugar": 15.8
        },
        {
        "name": "Bananas, ripe and slightly ripe, raw",
        "Protein": 0.74,
        "Calories": 0.0,
        "Fat": 0.29,
        "Fiber": 1.7,
        "Carbs": 23.0,
        "Salt": 0.0,
        "Sugar": 15.8
        },
        {
        "name": "Apples, red delicious, with skin, raw",
        "Protein": 0.188,
        "Calories": 61.8,
        "Fat": 0.212,
        "Fiber": 2.04,
        "Carbs": 14.8,
        "Salt": 0.0,
        "Sugar": 12.2
        },
        {
        "name": "Apples, fuji, with skin, raw",
        "Protein": 0.148,
        "Calories": 64.7,
        "Fat": 0.162,
        "Fiber": 2.08,
        "Carbs": 15.7,
        "Salt": 1.01,
        "Sugar": 13.3
        },
        {
        "name": "Apples, gala, with skin, raw",
        "Protein": 0.133,
        "Calories": 61.0,
        "Fat": 0.15,
        "Fiber": 2.11,
        "Carbs": 14.8,
        "Salt": 0.279,
        "Sugar": 11.8
        },
        {
        "name": "Apples, granny smith, with skin, raw",
        "Protein": 0.266,
        "Calories": 58.9,
        "Fat": 0.138,
        "Fiber": 2.51,
        "Carbs": 14.1,
        "Salt": 0.0,
        "Sugar": 10.7
        },
        {
        "name": "Apples, honeycrisp, with skin, raw",
        "Protein": 0.102,
        "Calories": 60.0,
        "Fat": 0.1,
        "Fiber": 1.72,
        "Carbs": 14.7,
        "Salt": 0.138,
        "Sugar": 12.4
        },
        {
        "name": "Oil, peanut",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Oil, sunflower",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Oil, safflower",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Oil, olive, extra light",
        "Protein": 0.0,
        "Calories": 0.0,
        "Fat": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Mushroom, lion's mane",
        "Protein": 2.5,
        "Calories": 42.7,
        "Fat": 0.256,
        "Fiber": 4.38,
        "Carbs": 7.59,
        "Salt": 0.336,
        "Sugar": 0.0
        },
        {
        "name": "Mushroom, oyster",
        "Protein": 2.9,
        "Calories": 41.0,
        "Fat": 0.188,
        "Fiber": 2.85,
        "Carbs": 6.94,
        "Salt": 1.13,
        "Sugar": 0.0
        },
        {
        "name": "Mushrooms, shiitake",
        "Protein": 2.41,
        "Calories": 44.1,
        "Fat": 0.195,
        "Fiber": 4.17,
        "Carbs": 8.17,
        "Salt": 0.936,
        "Sugar": 0.0
        },
        {
        "name": "Mushrooms, white button",
        "Protein": 2.89,
        "Calories": 31.2,
        "Fat": 0.371,
        "Fiber": 1.72,
        "Carbs": 4.08,
        "Salt": 6.44,
        "Sugar": 0.0
        },
        {
        "name": "Soy milk, unsweetened, plain, shelf stable",
        "Protein": 3.55,
        "Calories": 38.5,
        "Fat": 2.12,
        "Fiber": 0.0,
        "Carbs": 1.29,
        "Salt": 34.3,
        "Sugar": 0.557
        },
        {
        "name": "Almond milk, unsweetened, plain, shelf stable",
        "Protein": 0.555,
        "Calories": 14.6,
        "Fat": 1.22,
        "Fiber": 0.0,
        "Carbs": 0.337,
        "Salt": 59.6,
        "Sugar": 0.0
        },
        {
        "name": "Spinach, baby",
        "Protein": 2.85,
        "Calories": 26.6,
        "Fat": 0.619,
        "Fiber": 1.56,
        "Carbs": 2.41,
        "Salt": 111.0,
        "Sugar": 0.0
        },
        {
        "name": "Spinach, mature",
        "Protein": 2.91,
        "Calories": 27.6,
        "Fat": 0.604,
        "Fiber": 1.59,
        "Carbs": 2.64,
        "Salt": 107.0,
        "Sugar": 0.0
        },
        {
        "name": "Tomato, roma",
        "Protein": 0.696,
        "Calories": 22.0,
        "Fat": 0.425,
        "Fiber": 0.971,
        "Carbs": 3.84,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, 00",
        "Protein": 11.4,
        "Calories": 357.0,
        "Fat": 1.52,
        "Fiber": 2.66,
        "Carbs": 74.4,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, spelt, whole grain",
        "Protein": 14.5,
        "Calories": 364.0,
        "Fat": 2.54,
        "Fiber": 9.34,
        "Carbs": 70.7,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, semolina, coarse and semi-coarse",
        "Protein": 11.7,
        "Calories": 357.0,
        "Fat": 1.6,
        "Fiber": 3.22,
        "Carbs": 73.8,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Flour, semolina, fine",
        "Protein": 13.3,
        "Calories": 358.0,
        "Fat": 1.84,
        "Fiber": 3.68,
        "Carbs": 72.0,
        "Salt": 0.426,
        "Sugar": 0.0
        },
        {
        "name": "Apple juice, with added vitamin C, from concentrate, shelf stable",
        "Protein": 0.086,
        "Calories": 48.4,
        "Fat": 0.286,
        "Fiber": 0.0,
        "Carbs": 11.4,
        "Salt": 4.87,
        "Sugar": 10.3
        },
        {
        "name": "Orange juice, no pulp, not fortified, from concentrate, refrigerated",
        "Protein": 0.734,
        "Calories": 47.2,
        "Fat": 0.325,
        "Fiber": 0.0,
        "Carbs": 10.3,
        "Salt": 5.23,
        "Sugar": 8.28
        },
        {
        "name": "Grape juice, purple, with added vitamin C, from concentrate, shelf stable",
        "Protein": 0.258,
        "Calories": 66.1,
        "Fat": 0.288,
        "Fiber": 0.0,
        "Carbs": 15.6,
        "Salt": 4.02,
        "Sugar": 14.0
        },
        {
        "name": "Grape juice, white, with added vitamin C, from concentrate, shelf stable",
        "Protein": 0.094,
        "Calories": 66.1,
        "Fat": 0.265,
        "Fiber": 0.0,
        "Carbs": 15.8,
        "Salt": 7.19,
        "Sugar": 14.4
        },
        {
        "name": "Cranberry juice, not fortified, from concentrate, shelf stable",
        "Protein": 0.0,
        "Calories": 32.1,
        "Fat": 0.338,
        "Fiber": 0.0,
        "Carbs": 7.26,
        "Salt": 6.34,
        "Sugar": 3.41
        },
        {
        "name": "Grapefruit juice, red, not fortified, not from concentrate, refrigerated",
        "Protein": 0.57,
        "Calories": 41.1,
        "Fat": 0.267,
        "Fiber": 0.0,
        "Carbs": 9.1,
        "Salt": 1.03,
        "Sugar": 7.12
        },
        {
        "name": "Tomato juice, with added ingredients, from concentrate, shelf stable",
        "Protein": 0.859,
        "Calories": 23.3,
        "Fat": 0.288,
        "Fiber": 0.0,
        "Carbs": 4.32,
        "Salt": 236.0,
        "Sugar": 2.57
        },
        {
        "name": "Orange juice, no pulp, not fortified, not from concentrate, refrigerated",
        "Protein": 0.812,
        "Calories": 46.5,
        "Fat": 0.356,
        "Fiber": 0.0,
        "Carbs": 10.0,
        "Salt": 0.075,
        "Sugar": 8.08
        },
        {
        "name": "Mushroom, portabella",
        "Protein": 2.75,
        "Calories": 32.4,
        "Fat": 0.312,
        "Fiber": 1.88,
        "Carbs": 4.66,
        "Salt": 5.31,
        "Sugar": 0.0
        },
        {
        "name": "Mushroom, king oyster",
        "Protein": 2.41,
        "Calories": 46.4,
        "Fat": 0.308,
        "Fiber": 3.01,
        "Carbs": 8.5,
        "Salt": 0.771,
        "Sugar": 0.0
        },
        {
        "name": "Mushroom, enoki",
        "Protein": 2.42,
        "Calories": 44.4,
        "Fat": 0.245,
        "Fiber": 2.94,
        "Carbs": 8.14,
        "Salt": 0.417,
        "Sugar": 0.0
        },
        {
        "name": "Mushroom, crimini",
        "Protein": 3.09,
        "Calories": 30.2,
        "Fat": 0.197,
        "Fiber": 1.78,
        "Carbs": 4.01,
        "Salt": 4.57,
        "Sugar": 0.0
        },
        {
        "name": "Mushroom, maitake",
        "Protein": 2.2,
        "Calories": 37.6,
        "Fat": 0.265,
        "Fiber": 3.07,
        "Carbs": 6.6,
        "Salt": 0.345,
        "Sugar": 0.0
        },
        {
        "name": "Mushroom, beech",
        "Protein": 2.18,
        "Calories": 39.8,
        "Fat": 0.449,
        "Fiber": 3.14,
        "Carbs": 6.76,
        "Salt": 0.891,
        "Sugar": 0.0
        },
        {
        "name": "Mushroom, pioppini",
        "Protein": 3.5,
        "Calories": 39.2,
        "Fat": 0.24,
        "Fiber": 2.75,
        "Carbs": 5.76,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Soy milk, unsweetened, plain, refrigerated",
        "Protein": 2.78,
        "Calories": 40.7,
        "Fat": 1.96,
        "Fiber": 0.0,
        "Carbs": 3.0,
        "Salt": 39.4,
        "Sugar": 0.0
        },
        {
        "name": "Almond milk, unsweetened, plain, refrigerated",
        "Protein": 0.656,
        "Calories": 19.3,
        "Fat": 1.56,
        "Fiber": 0.0,
        "Carbs": 0.671,
        "Salt": 59.2,
        "Sugar": 0.0
        },
        {
        "name": "Oat milk, unsweetened, plain, refrigerated",
        "Protein": 0.797,
        "Calories": 48.3,
        "Fat": 2.75,
        "Fiber": 0.0,
        "Carbs": 5.1,
        "Salt": 42.0,
        "Sugar": 2.32
        },
        {
        "name": "Carrots, mature, raw",
        "Protein": 0.941,
        "Calories": 48.0,
        "Fat": 0.351,
        "Fiber": 3.1,
        "Carbs": 10.3,
        "Salt": 86.6,
        "Sugar": 0.0
        },
        {
        "name": "Carrots, baby, raw",
        "Protein": 0.805,
        "Calories": 40.8,
        "Fat": 0.138,
        "Fiber": 2.69,
        "Carbs": 9.08,
        "Salt": 62.7,
        "Sugar": 0.0
        },
        {
        "name": "Peppers, bell, green, raw",
        "Protein": 0.715,
        "Calories": 22.9,
        "Fat": 0.106,
        "Fiber": 0.942,
        "Carbs": 4.78,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Peppers, bell, yellow, raw",
        "Protein": 0.819,
        "Calories": 30.8,
        "Fat": 0.121,
        "Fiber": 1.07,
        "Carbs": 6.6,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Peppers, bell, red, raw",
        "Protein": 0.896,
        "Calories": 31.3,
        "Fat": 0.126,
        "Fiber": 1.16,
        "Carbs": 6.65,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Peppers, bell, orange, raw",
        "Protein": 0.882,
        "Calories": 31.7,
        "Fat": 0.156,
        "Fiber": 0.967,
        "Carbs": 6.7,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Buttermilk, low fat",
        "Protein": 3.46,
        "Calories": 42.8,
        "Fat": 1.08,
        "Fiber": 0.0,
        "Carbs": 4.81,
        "Salt": 92.5,
        "Sugar": 0.0
        },
        {
        "name": "Yogurt, plain, whole milk",
        "Protein": 3.82,
        "Calories": 78.0,
        "Fat": 4.48,
        "Fiber": 0.0,
        "Carbs": 5.57,
        "Salt": 41.8,
        "Sugar": 4.09
        },
        {
        "name": "Yogurt, Greek, plain, whole milk",
        "Protein": 8.78,
        "Calories": 93.7,
        "Fat": 4.39,
        "Fiber": 0.0,
        "Carbs": 4.75,
        "Salt": 33.8,
        "Sugar": 3.25
        },
        {
        "name": "Cheese, parmesan, grated, refrigerated",
        "Protein": 30.1,
        "Calories": 403.0,
        "Fat": 29.5,
        "Fiber": 0.0,
        "Carbs": 4.33,
        "Salt": 1050.0,
        "Sugar": 0.638
        },
        {
        "name": "Cheese, feta, whole milk, crumbled",
        "Protein": 19.7,
        "Calories": 273.0,
        "Fat": 19.1,
        "Fiber": 0.0,
        "Carbs": 5.58,
        "Salt": 1030.0,
        "Sugar": 1.63
        },
        {
        "name": "Flour, almond",
        "Protein": 26.2,
        "Calories": 622.0,
        "Fat": 50.2,
        "Fiber": 9.27,
        "Carbs": 16.2,
        "Salt": 0.894,
        "Sugar": 0.0
        },
        {
        "name": "Flour, oat, whole grain",
        "Protein": 13.2,
        "Calories": 389.0,
        "Fat": 6.31,
        "Fiber": 10.5,
        "Carbs": 69.9,
        "Salt": 3.62,
        "Sugar": 0.0
        },
        {
        "name": "Flour, potato",
        "Protein": 8.11,
        "Calories": 361.0,
        "Fat": 0.951,
        "Fiber": 5.4,
        "Carbs": 79.9,
        "Salt": 47.7,
        "Sugar": 0.0
        },
        {
        "name": "Peanut butter, creamy",
        "Protein": 24.0,
        "Calories": 632.0,
        "Fat": 49.4,
        "Fiber": 6.32,
        "Carbs": 22.7,
        "Salt": 221.0,
        "Sugar": 0.0
        },
        {
        "name": "Sesame butter, creamy",
        "Protein": 19.7,
        "Calories": 697.0,
        "Fat": 62.4,
        "Fiber": 8.37,
        "Carbs": 14.2,
        "Salt": 63.6,
        "Sugar": 0.0
        },
        {
        "name": "Almond butter, creamy",
        "Protein": 20.8,
        "Calories": 645.0,
        "Fat": 53.0,
        "Fiber": 9.72,
        "Carbs": 21.2,
        "Salt": 0.996,
        "Sugar": 0.0
        },
        {
        "name": "Flaxseed, ground",
        "Protein": 18.0,
        "Calories": 545.0,
        "Fat": 37.3,
        "Fiber": 23.1,
        "Carbs": 34.4,
        "Salt": 36.7,
        "Sugar": 0.0
        },
        {
        "name": "Cottage cheese, full fat, large or small curd",
        "Protein": 11.6,
        "Calories": 103.0,
        "Fat": 4.22,
        "Fiber": 0.0,
        "Carbs": 4.6,
        "Salt": 350.0,
        "Sugar": 0.0
        },
        {
        "name": "Cream cheese, full fat, block",
        "Protein": 5.79,
        "Calories": 343.0,
        "Fat": 33.5,
        "Fiber": 0.0,
        "Carbs": 4.56,
        "Salt": 368.0,
        "Sugar": 0.0
        },
        {
        "name": "Cream, heavy",
        "Protein": 2.02,
        "Calories": 343.0,
        "Fat": 35.6,
        "Fiber": 0.0,
        "Carbs": 3.8,
        "Salt": 20.6,
        "Sugar": 0.0
        },
        {
        "name": "Cream, sour, full fat",
        "Protein": 3.07,
        "Calories": 196.0,
        "Fat": 18.0,
        "Fiber": 0.0,
        "Carbs": 5.56,
        "Salt": 50.0,
        "Sugar": 0.0
        },
        {
        "name": "Lettuce, iceberg, raw",
        "Protein": 0.742,
        "Calories": 17.1,
        "Fat": 0.074,
        "Fiber": 0.0,
        "Carbs": 3.37,
        "Salt": 16.1,
        "Sugar": 0.0
        },
        {
        "name": "Lettuce, romaine, green, raw",
        "Protein": 0.977,
        "Calories": 20.8,
        "Fat": 0.071,
        "Fiber": 0.0,
        "Carbs": 4.06,
        "Salt": 23.0,
        "Sugar": 0.0
        },
        {
        "name": "Lettuce, leaf, red, raw",
        "Protein": 0.883,
        "Calories": 17.5,
        "Fat": 0.106,
        "Fiber": 0.0,
        "Carbs": 3.26,
        "Salt": 24.9,
        "Sugar": 0.0
        },
        {
        "name": "Lettuce, leaf, green, raw",
        "Protein": 1.09,
        "Calories": 22.0,
        "Fat": 0.156,
        "Fiber": 0.0,
        "Carbs": 4.07,
        "Salt": 28.9,
        "Sugar": 0.0
        },
        {
        "name": "Nuts, pine nuts, raw",
        "Protein": 15.7,
        "Calories": 689.0,
        "Fat": 61.3,
        "Fiber": 3.94,
        "Carbs": 18.6,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Nuts, almonds, whole, raw",
        "Protein": 21.5,
        "Calories": 626.0,
        "Fat": 51.1,
        "Fiber": 10.8,
        "Carbs": 20.0,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Nuts, walnuts, English, halves, raw",
        "Protein": 14.6,
        "Calories": 730.0,
        "Fat": 69.7,
        "Fiber": 5.21,
        "Carbs": 10.9,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Nuts, pecans, halves, raw",
        "Protein": 9.96,
        "Calories": 750.0,
        "Fat": 73.3,
        "Fiber": 5.79,
        "Carbs": 12.7,
        "Salt": 0.0,
        "Sugar": 0.0
        },
        {
        "name": "Oats, whole grain, rolled, old fashioned",
        "Protein": 13.5,
        "Calories": 382.0,
        "Fat": 5.89,
        "Fiber": 0.0,
        "Carbs": 68.7,
        "Salt": 0.668,
        "Sugar": 0.0
        },
        {
        "name": "Oats, whole grain, steel cut",
        "Protein": 12.5,
        "Calories": 381.0,
        "Fat": 5.8,
        "Fiber": 0.0,
        "Carbs": 69.8,
        "Salt": 0.311,
        "Sugar": 0.0
        },
        {
        "name": "Pineapple, raw",
        "Protein": 0.461,
        "Calories": 60.1,
        "Fat": 0.211,
        "Fiber": 0.935,
        "Carbs": 14.1,
        "Salt": 0.0,
        "Sugar": 11.4
        },
        {
        "name": "Cherries, sweet, dark red, raw",
        "Protein": 1.04,
        "Calories": 70.5,
        "Fat": 0.192,
        "Fiber": 0.0,
        "Carbs": 16.2,
        "Salt": 0.0,
        "Sugar": 13.9
        },
        {
        "name": "Beans, snap, green, raw",
        "Protein": 1.97,
        "Calories": 40.0,
        "Fat": 0.275,
        "Fiber": 3.01,
        "Carbs": 7.41,
        "Salt": 0.0,
        "Sugar": 2.33
        },
        {
        "name": "Potatoes, russet, without skin, raw",
        "Protein": 2.27,
        "Calories": 83.4,
        "Fat": 0.36,
        "Fiber": 0.0,
        "Carbs": 17.8,
        "Salt": 2.74,
        "Sugar": 0.526
        },
        {
        "name": "Potatoes, red, without skin, raw",
        "Protein": 2.06,
        "Calories": 75.6,
        "Fat": 0.248,
        "Fiber": 0.0,
        "Carbs": 16.3,
        "Salt": 2.86,
        "Sugar": 0.664
        },
        {
        "name": "Potatoes, gold, without skin, raw",
        "Protein": 1.81,
        "Calories": 73.5,
        "Fat": 0.264,
        "Fiber": 0.0,
        "Carbs": 16.0,
        "Salt": 2.24,
        "Sugar": 0.645
        },
        {
        "name": "Sweet potatoes, orange flesh, without skin, raw",
        "Protein": 1.58,
        "Calories": 79.0,
        "Fat": 0.375,
        "Fiber": 0.0,
        "Carbs": 17.3,
        "Salt": 0.0,
        "Sugar": 6.06
        },
        {
        "name": "Celery, raw",
        "Protein": 0.492,
        "Calories": 16.7,
        "Fat": 0.162,
        "Fiber": 0.0,
        "Carbs": 3.32,
        "Salt": 97.2,
        "Sugar": 0.0
        },
        {
        "name": "Cucumber, with peel, raw",
        "Protein": 0.625,
        "Calories": 15.9,
        "Fat": 0.178,
        "Fiber": 0.0,
        "Carbs": 2.95,
        "Salt": 1.52,
        "Sugar": 0.0
        },
        {
        "name": "Cabbage, green, raw",
        "Protein": 0.961,
        "Calories": 31.4,
        "Fat": 0.228,
        "Fiber": 0.0,
        "Carbs": 6.38,
        "Salt": 16.1,
        "Sugar": 0.0
        },
        {
        "name": "Cabbage, red, raw",
        "Protein": 1.24,
        "Calories": 34.1,
        "Fat": 0.214,
        "Fiber": 0.0,
        "Carbs": 6.79,
        "Salt": 11.7,
        "Sugar": 0.0
        },
        {
        "name": "Strawberries, raw",
        "Protein": 0.641,
        "Calories": 36.4,
        "Fat": 0.22,
        "Fiber": 0.0,
        "Carbs": 7.96,
        "Salt": 0.0,
        "Sugar": 4.86
        },
        {
        "name": "Raspberries, raw",
        "Protein": 1.01,
        "Calories": 57.3,
        "Fat": 0.188,
        "Fiber": 0.0,
        "Carbs": 12.9,
        "Salt": 0.0,
        "Sugar": 2.68
        },
        {
        "name": "Blueberries, raw",
        "Protein": 0.703,
        "Calories": 63.9,
        "Fat": 0.306,
        "Fiber": 0.0,
        "Carbs": 14.6,
        "Salt": 0.0,
        "Sugar": 9.36
        },
        {
        "name": "Grapes, red, seedless, raw",
        "Protein": 0.914,
        "Calories": 85.9,
        "Fat": 0.164,
        "Fiber": 0.0,
        "Carbs": 20.2,
        "Salt": 7.0,
        "Sugar": 17.3
        },
        {
        "name": "Grapes, green, seedless, raw",
        "Protein": 0.899,
        "Calories": 80.1,
        "Fat": 0.232,
        "Fiber": 0.0,
        "Carbs": 18.6,
        "Salt": 3.17,
        "Sugar": 16.1
        },
        {
        "name": "Applesauce, unsweetened, with added vitamin C",
        "Protein": 0.273,
        "Calories": 51.6,
        "Fat": 0.162,
        "Fiber": 0.0,
        "Carbs": 12.3,
        "Salt": 0.504,
        "Sugar": 9.66
        }
        ]
