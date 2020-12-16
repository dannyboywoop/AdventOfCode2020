from aoc_tools.advent_timer import Advent_Timer
from re import compile
from itertools import chain


RULE_REGEX = compile(r"^(\w+(?: \w+)?): (?:(\d+)-(\d+)) or (?:(\d+)-(\d+))$")


def parse_ticket(ticket_string):
    return [int(x) for x in ticket_string.split(",")]


def parse_rules(rule_strings):
    rules = {}
    for rule_string in rule_strings:
        field, min1, max1, min2, max2 = RULE_REGEX.match(rule_string).groups()
        rules[field] = set(chain(range(int(min1), int(max1)+1),
                                 range(int(min2), int(max2)+1)))
    return rules


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [[line for line in section.strip().split("\n")]
                for section in file.read().split("\n\n")]
    rules = parse_rules(data[0])
    my_ticket = parse_ticket(data[1][1])
    other_tickets = [parse_ticket(ticket) for ticket in data[2][1:]]
    return rules, my_ticket, other_tickets


def star_1(rules, other_tickets):
    possible_values = set.union(*rules.values())
    scanning_error_rate = 0
    valid_tickets = []
    for ticket in other_tickets:
        valid = True
        for value in ticket:
            if value not in possible_values:
                valid = False
                scanning_error_rate += value
        if valid:
            valid_tickets.append(ticket)
    return scanning_error_rate, valid_tickets


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    rules, my_ticket, other_tickets = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer, valid_tickets = star_1(rules, other_tickets)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    timer.end_hit()
