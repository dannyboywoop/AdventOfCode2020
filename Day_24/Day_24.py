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


class Tile_Floor:
    def __init__(self, black_tiles):
        self.black_tiles = {black_tile: self._get_neighbours(black_tile)
                            for black_tile in black_tiles}

    def _add_black_tile(self, position):
        self.black_tiles[position] = self._get_neighbours(position)

    def _get_neighbours(self, position):
        x, y = position
        neighbours = {(x + delta_x, y + delta_y)
                      for delta_x, delta_y in DIRECTIONS.values()}
        return neighbours

    def _count_black_neighbours(self):
        black_neighbour_counts = {black_tile: 0
                                  for black_tile in self.black_tiles}
        for neighbours in self.black_tiles.values():
            for neighbour in neighbours:
                if neighbour in black_neighbour_counts:
                    black_neighbour_counts[neighbour] += 1
                else:
                    black_neighbour_counts[neighbour] = 1
        return black_neighbour_counts

    def _update_black_tiles(self):
        black_neighbour_counts = self._count_black_neighbours()
        for pos, count in black_neighbour_counts.items():
            if pos in self.black_tiles:
                if not (count == 1 or count == 2):
                    self.black_tiles.pop(pos)
            else:
                if count == 2:
                    self._add_black_tile(pos)

    def evolve(self, num_of_days):
        for _ in range(num_of_days):
            self._update_black_tiles()


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


def star_2(black_tiles):
    floor = Tile_Floor(black_tiles)
    floor.evolve(num_of_days=100)
    return len(floor.black_tiles)


if __name__ == "__main__":
    timer = Advent_Timer()

    instructions_list = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    black_tiles = star_1(instructions_list)
    print("Star 1: {}".format(len(black_tiles)))
    timer.checkpoint_hit()

    star_2_answer = star_2(black_tiles)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
