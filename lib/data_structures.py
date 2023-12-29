spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level", 0) > 5]

def print_spicy_foods(spicy_foods):

    for food in spicy_foods:
        # Calculate the number of chili pepper icons to print
        peppers = '🌶' * int(food.get('heat_level', 0))
        # Print the food name, cuisine, and heat level in the desired format
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        # Check if the cuisine of the current food matches the given cuisine
        if food['cuisine'] == cuisine:
            return food
    # Return None if no match is found
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food.get("heat_level", 0) > 5]

    for food in spiciest_foods:
        # Calculate the number of chili pepper icons to print
        peppers = '🌶' * int(food.get('heat_level', 0))
        # Print the food name, cuisine, and heat level in the desired format
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    
    # Calculate total heat by summing up the heat levels of all foods
    for food in spicy_foods:
        total_heat += food['heat_level']
    
    # Calculate average by dividing total heat by the number of foods
    # Convert result to integer
    average = int(total_heat / len(spicy_foods)) if spicy_foods else 0
    
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    
    # Return the updated list
    return spicy_foods
