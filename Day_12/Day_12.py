from aoc_tools.advent_timer import Advent_Timer
from math import sin, cos, radians
from numpy import array, dot, absolute


DIRECTIONS = {
    "N": array([0, 1]),
    "S": array([0, -1]),
    "E": array([1, 0]),
    "W": array([-1, 0])
}


class Ship:
    def __init__(self):
        self.pos = array([0, 0])
        self.direction = array([1, 0])

    def follow_instruction(self, instruction):
        action, value = instruction
        if action == "L":
            self.direction = rotate_2d_vector(self.direction, value)
        elif action == "R":
            self.direction = rotate_2d_vector(self.direction, -value)
        elif action == "F":
            self.pos += value * self.direction
        else:
            self.pos += value * DIRECTIONS[action]


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        instructions = [(line[0], int(line[1:])) for line in file]
    return instructions


def rotate_2d_vector(vector, angle):
    cos_angle = int(cos(radians(angle)))
    sin_angle = int(sin(radians(angle)))
    rotation_matrix = array([[cos_angle, -sin_angle],
                             [sin_angle, cos_angle]])
    return dot(rotation_matrix, vector).astype(int)


def move_ship_along_path(ship, instructions):
    for instruction in instructions:
        ship.follow_instruction(instruction)
    return ship


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    instructions = read_input()
    timer.checkpoint_hit()

    # star 1
    ship_1 = move_ship_along_path(Ship(), instructions)
    print("Star 1: {}".format(sum(absolute(ship_1.pos))))
    timer.checkpoint_hit()

    timer.end_hit()
