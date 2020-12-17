from aoc_tools.advent_timer import Advent_Timer
from itertools import product


class Pocket_Dimension:
    def __init__(self, cube_array, dimensions):
        self.dimensions = dimensions
        self.active_cubes = {}
        self.neighbour_deltas = [deltas for deltas in
                                 product([-1, 0, 1], repeat=self.dimensions)
                                 if any(deltas)]
        self._initialise_active_cubes(cube_array)

    def _initialise_active_cubes(self, cube_array):
        padding = tuple([0]*(self.dimensions-2))
        for i, row in enumerate(cube_array):
            for j, val in enumerate(cube_array[i]):
                if val == ".":
                    continue
                self._add_active_cube((j, i)+padding)

    def _add_active_cube(self, position):
        self.active_cubes[position] = self._get_neighbours(position)

    def _get_neighbours(self, position):
        neighbours = set()
        for deltas in self.neighbour_deltas:
            neighbour_pos = tuple(map(sum, zip(position, deltas)))
            neighbours.add(neighbour_pos)
        return neighbours

    def _count_active_neighbours(self):
        active_neighbour_counts = {active_cube: 0
                                   for active_cube in self.active_cubes}
        for neighbours in self.active_cubes.values():
            for neighbour in neighbours:
                if neighbour in active_neighbour_counts:
                    active_neighbour_counts[neighbour] += 1
                else:
                    active_neighbour_counts[neighbour] = 1
        return active_neighbour_counts

    def _update_active_cubes(self):
        active_neighbour_counts = self._count_active_neighbours()
        for pos, count in active_neighbour_counts.items():
            if pos in self.active_cubes:
                if not (count == 2 or count == 3):
                    self.active_cubes.pop(pos)
            else:
                if count == 3:
                    self._add_active_cube(pos)

    def perform_boot_process(self):
        for _ in range(6):
            self._update_active_cubes()


def read_cube_array(filename="input.txt"):
    with open(filename, "r") as file:
        cube_array = [line.strip() for line in file]
    return cube_array


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    cube_array = read_cube_array()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    pocket_dimension_3d = Pocket_Dimension(cube_array, dimensions=3)
    pocket_dimension_3d.perform_boot_process()
    star_1_answer = len(pocket_dimension_3d.active_cubes)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    pocket_dimension_4d = Pocket_Dimension(cube_array, dimensions=4)
    pocket_dimension_4d.perform_boot_process()
    star_2_answer = len(pocket_dimension_4d.active_cubes)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
