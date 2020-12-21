from aoc_tools import Advent_Timer
from numpy import array


class Tile:
    class Edge:
        def __init__(self, elements):
            self.elements = elements
            self.generate_representation()

        def generate_representation(self):
            self.rep = tuple(max([self.elements, self.elements[::-1]],
                                 key=list_to_binary))

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return False
            return self.rep == other.rep

        def __ne__(self, other):
            return not self.__eq__(other)

        def __hash__(self):
            return hash(self.rep)

    def __init__(self, tile_strings):
        self.grid = array([[1 if x == "#" else 0 for x in line]
                           for line in tile_strings])
        self.get_edges()

    def get_edges(self):
        self.edges = [Tile.Edge(self.grid[0, :]),  # top edge
                      Tile.Edge(self.grid[:, -1]),  # right edge
                      Tile.Edge(self.grid[-1, :]),  # bottom edge
                      Tile.Edge(self.grid[:, 0])]  # left edge


def list_to_binary(binary_list):
    return '0b' + ''.join('1' if x else '0' for x in binary_list)


def parse_tile(tile_string):
    tile_strings = tile_string.split("\n")
    tile_number = int(tile_strings.pop(0)[5:-1])
    tile = Tile(tile_strings)
    return (tile_number, tile)


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        tiles = file.read().strip().split("\n\n")
    tiles = dict([parse_tile(tile) for tile in tiles])
    return tiles


def star_1(tiles):
    unique_edge_count = {tile_num: 4 for tile_num in tiles}
    seen_edges = {}
    for tile_num, tile in tiles.items():
        for edge in tile.edges:
            if edge in seen_edges:
                unique_edge_count[tile_num] -= 1
                unique_edge_count[seen_edges[edge]] -= 1
            else:
                seen_edges[edge] = tile_num
    answer = 1
    for tile_num, unique_edges in unique_edge_count.items():
        if unique_edges == 2:
            answer *= tile_num
    return answer


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    tiles = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer = star_1(tiles)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    timer.checkpoint_hit()

    timer.end_hit()
