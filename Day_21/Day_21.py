from aoc_tools import Advent_Timer
from re import findall
from copy import deepcopy


def parse_food(food_string):
    open_bracket_pos = food_string.find("(")
    ingredients = set(findall(r"\w+", food_string[:open_bracket_pos]))
    allergens = set(findall(r"(\w+)[,\)]", food_string[open_bracket_pos:]))
    return (ingredients, allergens)


def read_data(filename="input.txt"):
    with open(filename, "r") as input_file:
        foods = [parse_food(line.strip()) for line in input_file]
    return foods


def get_risky_ingredients(foods):
    all_allergens = set.union(*[allergens for _, allergens in foods])
    risky_ingredients = {}
    for allergen in all_allergens:
        potential_risks = None
        for ingredients, allergens in foods:
            if allergen in allergens:
                if potential_risks is None:
                    potential_risks = ingredients
                    continue
                potential_risks = potential_risks.intersection(ingredients)
        risky_ingredients[allergen] = potential_risks
    return risky_ingredients


def star_1(foods):
    risky_ingredients = get_risky_ingredients(foods)

    # get sets containing all ingredients and all risky_ingredients
    all_ingredients = set.union(*[ingredients for ingredients, _ in foods])
    all_risky_ingredients = set.union(*risky_ingredients.values())

    # safe_ingredients should not exist in the risky_ingredients
    safe_ingredients = all_ingredients.difference(all_risky_ingredients)

    count = 0
    for safe_ingredient in safe_ingredients:
        for ingredients, _ in foods:
            if safe_ingredient in ingredients:
                count += 1
    return count


if __name__ == "__main__":
    timer = Advent_Timer()

    foods = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    star_1_answer = star_1(foods)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()
    timer.checkpoint_hit()

    timer.end_hit()
