from aoc_tools import Advent_Timer
from regex import fullmatch, compile


REGEX_CACHE = {}


def parse_rules(rules_str):
    rule_strings = [rule.split(":") for rule in rules_str.split("\n")]
    rules = {key: val.strip() for key, val in rule_strings}
    return rules


def get_regex(rules, rule):
    if rule in REGEX_CACHE:
        return REGEX_CACHE[rule]

    if '"' in rules[rule]:
        regex = rules[rule].strip('"')
        REGEX_CACHE[rule] = regex
        return regex

    parts = rules[rule].split()
    parsed_parts = []
    recursive = False
    for part in parts:
        if part == "|":
            parsed_parts.append("|")
        elif part == rule:
            parsed_parts.append("(?P>r{})*".format(rule))
            recursive = True
        else:
            parsed_parts.append(get_regex(rules, part))

    regex = "".join(parsed_parts)
    if recursive:
        regex = "(?P<r{}>{})".format(rule, regex)
    else:
        regex = "(?:{})".format(regex)
    REGEX_CACHE[rule] = regex
    return regex


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        rules_str, messages_str = file.read().strip().split("\n\n")
    rules = parse_rules(rules_str)
    messages = messages_str.split()
    return rules, messages


def count_matching_messages(rules, messages, rule="0"):
    regex = compile(get_regex(rules, rule))
    return sum([bool(fullmatch(regex, message)) for message in messages])


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    rules, messages = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer = count_matching_messages(rules, messages)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    rules["8"] = "42 8"
    rules["11"] = "42 31 | 42 11 31"
    REGEX_CACHE.clear()
    star_2_answer = count_matching_messages(rules, messages)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
