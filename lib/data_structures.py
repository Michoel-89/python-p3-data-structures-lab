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
    spicy_names = [f['name'] for f in spicy_foods]
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [f for f in spicy_foods if f['heat_level'] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        spiciness = food['heat_level'] * '🌶' 
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {spiciness}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    specific_cuisine = [c for c in spicy_foods if c['cuisine'] == cuisine]
    return specific_cuisine[0]


def print_spiciest_foods(spicy_foods):
    filtered_spicy_foods = get_spiciest_foods(spicy_foods)
    for food in filtered_spicy_foods:
        spiciness = food['heat_level'] * '🌶' 
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {spiciness}")

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food['heat_level']
    return total / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
