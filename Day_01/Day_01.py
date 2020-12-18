from aoc_tools import Advent_Timer


def read_data(input_file="input.txt"):
    with open(input_file, 'r') as file:
        data = {int(line) for line in file}
    return data


def find_set_with_sum(data, set_size, total=2020, all_positive=True):
    if set_size < 1:
        raise Exception("Error: set_size must be atleast 1")

    if set_size > len(data):
        raise Exception("Error: set_size must be <= the size of the data")

    if set_size == 1:
        if total in data:
            return {total}

    else:
        remaining_data = data.copy()
        set_size -= 1
        for _ in range(len(remaining_data)-set_size):
            val = remaining_data.pop()
            if val >= total and all_positive:
                continue
            sub_set = find_set_with_sum(remaining_data, set_size, total-val)
            if sub_set is not None:
                sub_set.add(val)
                return sub_set


def get_formatted_product(int_set):
    product = 1
    for x in int_set:
        product *= x
    return "x".join(map(str, int_set)) + "={}".format(product)


if __name__ == "__main__":
    timer = Advent_Timer()
    data = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    pair = find_set_with_sum(data, 2)
    print("Star 1: "+get_formatted_product(pair))
    timer.checkpoint_hit()

    triplet = find_set_with_sum(data, 3)
    print("Star 2: "+get_formatted_product(triplet))
    timer.checkpoint_hit()

    timer.end_hit()
