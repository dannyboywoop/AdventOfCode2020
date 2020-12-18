from aoc_tools import Advent_Timer
from re import compile
from itertools import chain
from copy import deepcopy


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


def get_allowed_positions(rules, valid_tickets):
    allowed_positions = {field: set() for field in rules}
    for field, allowed_range in rules.items():
        for pos in range(len(my_ticket)):
            pos_valid = True
            for ticket in valid_tickets:
                if ticket[pos] not in allowed_range:
                    pos_valid = False
                    break
            if pos_valid:
                allowed_positions[field].add(pos)
    return allowed_positions


def find_sole_bipartide_match(allowed_positions):
    remaining = deepcopy(allowed_positions)
    matches = {}
    matched_edge = None
    while len(matches) < len(allowed_positions):
        for node, edges in remaining.items():
            if len(edges) == 1:
                matched_edge = edges.pop()
                matches[node] = matched_edge
                remaining.pop(node)
                break
        for edges in remaining.values():
            edges.discard(matched_edge)
    return matches


def star_2(rules, valid_tickets, my_ticket):
    allowed_positions = get_allowed_positions(rules, valid_tickets)
    correct_positions = find_sole_bipartide_match(allowed_positions)
    answer = 1
    for field in rules:
        if not field.startswith("departure"):
            continue
        answer *= my_ticket[correct_positions[field]]
    return answer


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

    # star 2
    star_2_answer = star_2(rules, valid_tickets, my_ticket)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
