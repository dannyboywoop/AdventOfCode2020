from aoc_tools import Advent_Timer
from re import findall, compile


INSTRUCTION_REGEX = compile(r"(?:e|w|(?:se)|(?:sw)|(?:ne)|(?:nw))")
DIRECTIONS = {
    "e": (2, 0),
    "w": (-2, 0),
    "ne": (1, 1),
    "nw": (-1, 1),
    "se": (1, -1),
    "sw": (-1, -1)
}


def parse_instructions(instructions):
    return list(findall(INSTRUCTION_REGEX, instructions))


def read_data(filename="input.txt"):
    with open(filename, 'r') as input_file:
        instructions_list = [parse_instructions(line) for line in input_file]
    return instructions_list


def follow_instructions(instructions, start_pos = (0, 0)):
    x, y = start_pos
    for instruction in instructions:
        delta_x, delta_y = DIRECTIONS[instruction]
        x += delta_x
        y += delta_y
    return (x, y)


def star_1(instructions_list):
    black_tiles = set()
    for instructions in instructions_list:
        position = follow_instructions(instructions)
        if position in black_tiles:
            black_tiles.remove(position)
        else:
            black_tiles.add(position)
    return black_tiles


if __name__ == "__main__":
    timer = Advent_Timer()

    instructions_list = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    black_tiles = star_1(instructions_list)
    print("Star 1: {}".format(len(black_tiles)))
    timer.checkpoint_hit()

    timer.end_hit()
