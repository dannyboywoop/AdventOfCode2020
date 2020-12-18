from re import match, finditer
from aoc_tools import Advent_Timer


can_contain_colour_cache = {}
total_bag_count_cache = {}


class Requirement:
    def __init__(self, input_tuple):
        number, self.colour = input_tuple
        self.number = int(number)


def parse_rules(string_rules):
    rules = {}
    for string_rule in string_rules:
        key_colour = match(r"^(\S+ \S+)", string_rule).group()
        required_colours = [Requirement(x.groups())
                            for x in finditer(r"(\d) (\S+ \S+)", string_rule)]
        rules[key_colour] = required_colours
    return rules


def read_rules_from_file(filename="input.txt"):
    with open(filename, "r") as input_file:
        string_rules = input_file.readlines()
    return parse_rules(string_rules)


def can_contain_colour(rules, container, colour):
    # initialise cache for bags that can contain 'colour'
    if colour not in can_contain_colour_cache:
        can_contain_colour_cache[colour] = {}

    # check cache for container
    if container in can_contain_colour_cache[colour]:
        return can_contain_colour_cache[colour][container]

    # calculate if not cached
    result = False
    for rule in rules[container]:
        if rule.colour == colour:
            result = True
            break
        elif can_contain_colour(rules, container=rule.colour, colour=colour):
            result = True
            break

    # cache result
    can_contain_colour_cache[colour][container] = result
    return result


def find_colours_that_contain(rules, colour):
    colours = []
    for key_colour in rules:
        if can_contain_colour(rules, key_colour, colour):
            colours += [key_colour]
    return colours


def find_total_bag_count(rules, colour):
    # check cache for colour
    if colour in total_bag_count_cache:
        return total_bag_count_cache[colour]

    total = 0
    for rule in rules[colour]:
        total += rule.number
        total += rule.number * find_total_bag_count(rules, rule.colour)

    # cache total
    total_bag_count_cache[colour] = total
    return total


if __name__ == "__main__":
    timer = Advent_Timer()
    rules = read_rules_from_file()
    print("Input parsed!")
    timer.checkpoint_hit()

    star_1_answer = len(find_colours_that_contain(rules, "shiny gold"))
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    star_2_answer = find_total_bag_count(rules, "shiny gold")
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
