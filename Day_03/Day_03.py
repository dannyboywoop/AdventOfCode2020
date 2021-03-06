from aoc_tools import Advent_Timer


class Forest_Map:
    TREE_CHAR = '#'

    def __init__(self, map_array):
        self.map_array = map_array
        self.height = len(map_array)
        self.width = len(map_array[0])

    def _get_indices(self, x_pos, y_pos):
        return (x_pos % self.width, y_pos)

    def is_in_forest(self, x_pos, y_pos):
        return 0 <= y_pos < self.height and x_pos >= 0

    def is_tree(self, x_pos, y_pos):
        x_index, y_index = self._get_indices(x_pos, y_pos)
        return self.map_array[y_index][x_index] == Forest_Map.TREE_CHAR


def read_map_from_file(filename="input.txt"):
    with open(filename, 'r') as map_file:
        map_array = [line.strip() for line in map_file]
    return Forest_Map(map_array)


def count_trees_in_trajectory(forest_map, x_vel, y_vel):
    tree_count = 0
    x_pos = y_pos = 0
    while forest_map.is_in_forest(x_pos, y_pos):
        tree_count += forest_map.is_tree(x_pos, y_pos)
        x_pos += x_vel
        y_pos += y_vel
    return tree_count


if __name__ == "__main__":
    timer = Advent_Timer()
    forest_map = read_map_from_file()
    print("Input parsed!")
    timer.checkpoint_hit()

    star_1_answer = count_trees_in_trajectory(forest_map, 3, 1)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    star_2_inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    star_2_answer = 1
    for x_vel, y_vel in star_2_inputs:
        star_2_answer *= count_trees_in_trajectory(forest_map, x_vel, y_vel)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
