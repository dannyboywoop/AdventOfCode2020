from aoc_tools.advent_timer import Advent_Timer
from itertools import product


class Cube:
    def __init__(self, pos):
        self.dimensions = len(pos)
        self._find_neighbours(pos)

    def _find_neighbours(self, pos):
        self.neighbours = set()
        for deltas in product([-1, 0, 1], repeat=self.dimensions):
            if any(deltas):
                neighbour_pos = tuple(map(sum, zip(pos, deltas)))
                self.neighbours.add(neighbour_pos)


def parse_cubes(cube_array, dimensions):
    active_cubes = {}
    padding = tuple([0]*(dimensions-2))
    for i, row in enumerate(cube_array):
        for j, val in enumerate(cube_array[i]):
            if val == ".":
                continue
            active_cubes[(j, i)+padding] = Cube((j, i)+padding)
    return active_cubes


def read_active_cubes(dimensions, filename="input.txt"):
    with open(filename, "r") as file:
        cube_array = [line.strip() for line in file]
    return parse_cubes(cube_array, dimensions)


def count_active_neighbours(active_cubes):
    active_neighbour_count = {active_cube: 0 for active_cube in active_cubes}
    for active_cube in active_cubes.values():
        for neighbour_pos in active_cube.neighbours:
            if neighbour_pos in active_neighbour_count:
                active_neighbour_count[neighbour_pos] += 1
            else:
                active_neighbour_count[neighbour_pos] = 1
    return active_neighbour_count


def update_active_cubes(active_cubes):
    active_neighbour_count = count_active_neighbours(active_cubes)
    for pos, count in active_neighbour_count.items():
        if pos in active_cubes:
            if not (count == 2 or count == 3):
                active_cubes.pop(pos)
        else:
            if count == 3:
                active_cubes[pos] = Cube(pos)


def perform_boot_process(active_cubes):
    for _ in range(6):
        update_active_cubes(active_cubes)
    return len(active_cubes)


if __name__ == "__main__":
    timer = Advent_Timer()

    # star 1
    active_cubes = read_active_cubes(dimensions=3)
    star_1_answer = perform_boot_process(active_cubes)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    timer.end_hit()
