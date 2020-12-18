from aoc_tools import Advent_Timer


def read_data(filename="input.txt"):
    with open(filename, "r") as input_file:
        data = [int(x) for x in input_file]
    return data


def pair_of_numbers_sum_to_val(numbers, val):
    for number in numbers:
        if val - number in numbers:
            return True


def find_first_invalid_number(data):
    previous_25 = set(data[:25])

    for i in range(25, len(data)):
        val = data[i]
        if not pair_of_numbers_sum_to_val(previous_25, val):
            return val
        oldest_number = data[i-25]
        previous_25.remove(oldest_number)
        previous_25.add(val)


def find_min_plus_max_of_contigous_set(data, val):
    for i in range(len(data)):
        total = 0
        for j in range(i, len(data)):
            total += data[j]
            if total == val:
                return min(data[i:j+1]) + max(data[i:j+1])
            if total > val:
                break


if __name__ == "__main__":
    timer = Advent_Timer()
    data = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    star_1_answer = find_first_invalid_number(data)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    star_2_answer = find_min_plus_max_of_contigous_set(data, star_1_answer)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
