from aoc_tools import Advent_Timer
from numpy import array, sqrt, rot90, transpose, concatenate
from copy import deepcopy


SEA_MONSTER = array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
])


class Tile:
    class Edge:
        def __init__(self, elements):
            self.elements = elements
            self._generate_representation()

        def _generate_representation(self):
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
        self._get_edges()
        self._sides = {
            "LEFT": 0,
            "TOP": 1,
            "RIGHT": 2,
            "BOTTOM": 3
        }

    def _get_edges(self):
        self.edges = [Tile.Edge(self.grid[::-1, 0]),  # left edge
                      Tile.Edge(self.grid[0, :]),  # top edge
                      Tile.Edge(self.grid[:, -1]),  # right edge
                      Tile.Edge(self.grid[-1, ::-1])]  # bottom edge

    def __getitem__(self, side):
        return self.edges[self._sides[side]]

    def _rotate90(self):
        self.grid = rot90(self.grid)
        temp = self._sides["LEFT"]
        self._sides["LEFT"] = self._sides["TOP"]
        self._sides["TOP"] = self._sides["RIGHT"]
        self._sides["RIGHT"] = self._sides["BOTTOM"]
        self._sides["BOTTOM"] = temp

    def _swap_sides(self, side1, side2):
        temp = self._sides[side1]
        self._sides[side1] = self._sides[side2]
        self._sides[side2] = temp

    def _transpose(self):
        self.grid = transpose(self.grid)
        self._swap_sides("LEFT", "TOP")
        self._swap_sides("RIGHT", "BOTTOM")

    def edges_are_adjacent(self, edge1, edge2):
        edges = {edge1, edge2}
        for i in range(len(self.edges)):
            if self.edges[i] in edges and self.edges[i-1] in edges:
                return True
        return False

    def match_edges(self, left_edge, top_edge):
        edges_to_match = {left_edge, top_edge}
        while (self["LEFT"] not in edges_to_match or
               self["TOP"] not in edges_to_match):
            self._rotate90()
        if self["LEFT"] != left_edge:
            self._transpose()


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
    # get paired and unpaired edges
    paired_edges = {}
    unpaired_edges = {}
    for tile_num, tile in tiles.items():
        for edge in tile.edges:
            if edge in unpaired_edges:
                paired_edges[edge] = {tile_num, unpaired_edges.pop(edge)}
            else:
                unpaired_edges[edge] = tile_num

    # count tiles with 2 unpaired edges
    answer = 1
    corner_tiles = []
    for tile_num, tile in tiles.items():
        unpaired_edges_count = 0
        for edge in tile.edges:
            if edge in unpaired_edges:
                unpaired_edges_count += 1
        if unpaired_edges_count == 2:
            answer *= tile_num
            corner_tiles.append(tile_num)
    return answer, corner_tiles, paired_edges


def get_picture_order(tiles, corner_tile_num, paired_edges, grid_size):
    unmatched_tiles = set(tiles.keys())
    picture_order = {}

    for i in range(grid_size):
        for j in range(grid_size):
            # define known constraints
            left_edge = top_edge = None
            if j > 0:
                left_edge = tiles[picture_order[(i, j-1)]]["RIGHT"]
            if i > 0:
                top_edge = tiles[picture_order[(i-1, j)]]["BOTTOM"]

            # handle top-left corner
            if not left_edge and not top_edge:
                tile_num = corner_tile_num
                left_edge, top_edge = [edge for edge in tiles[tile_num].edges
                                       if edge not in paired_edges]

            # handle left column and top row
            elif not left_edge or not top_edge:
                if not left_edge:
                    known_edge = top_edge
                else:
                    known_edge = left_edge

                # get tile_num
                matching_tiles = paired_edges[known_edge]
                for tile_num in matching_tiles:
                    if tile_num in unmatched_tiles:
                        break

                # get adjacent edge that isn't paired
                unpaired_edges = [edge for edge in tiles[tile_num].edges
                                  if edge not in paired_edges]
                for edge in unpaired_edges:
                    if tiles[tile_num].edges_are_adjacent(known_edge, edge):
                        other_edge = edge
                        break

                # define missing constraint
                if not left_edge:
                    left_edge = other_edge
                else:
                    top_edge = other_edge

            # handle other cases
            else:
                tile_num = set.intersection(paired_edges[left_edge],
                                            paired_edges[top_edge]).pop()

            tiles[tile_num].match_edges(left_edge, top_edge)
            unmatched_tiles.remove(tile_num)
            picture_order[(i, j)] = tile_num

    return picture_order


def build_picture(tiles, picture_order, grid_size):
    picture = None
    for i in range(grid_size):
        row = tiles[picture_order[(i, 0)]].grid[1:-1, 1:-1]
        for j in range(1, grid_size):
            tile_image = tiles[picture_order[(i, j)]].grid[1:-1, 1:-1]
            row = concatenate((row, tile_image), axis=1)
        if picture is None:
            picture = row
            continue
        picture = concatenate((picture, row), axis=0)
    return picture


def count_sea_monsters(picture):
    height, length = SEA_MONSTER.shape
    sea_monster_checks = [(i, j)
                          for i in range(height)
                          for j in range(length)
                          if SEA_MONSTER[i, j]]
    # check before and after transposing imaging
    for transpose_image in [False, True]:
        if transpose_image:
            test_picture = transpose(picture)
        else:
            test_picture = picture

        # check each 90 degree rotation
        for rotation_num in range(4):
            test_picure = rot90(test_picture, rotation_num)
            count = 0
            for i in range(len(test_picture) - height + 1):
                for j in range(len(test_picture[i]) - length + 1):
                    sea_monster_found = True
                    for delta_i, delta_j in sea_monster_checks:
                        if not test_picture[i + delta_i, j + delta_j]:
                            sea_monster_found = False
                            break
                    if sea_monster_found:
                        count += 1
            if count > 0:
                return count
    return 0


def star_2(tiles, corner_tile_num, paired_edges):
    grid_size = int(sqrt(len(tiles)))
    picture_order = get_picture_order(tiles,
                                      corner_tile_num,
                                      paired_edges,
                                      grid_size)
    picture = build_picture(tiles, picture_order, grid_size)
    number_of_ones = sum(picture.flatten())
    num_of_sea_monsters = count_sea_monsters(picture)
    return number_of_ones - (sum(SEA_MONSTER.flatten()) * num_of_sea_monsters)


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    tiles = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer, corner_tiles, paired_edges = star_1(tiles)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    star_2_answer = star_2(tiles, corner_tiles[0], paired_edges)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
