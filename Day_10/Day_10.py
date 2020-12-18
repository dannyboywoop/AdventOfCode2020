from aoc_tools import Advent_Timer


trib_001_cache = {1: 0, 2: 0, 3: 1}


def read_adapters(filename="input.txt"):
    with open(filename, "r") as input_file:
        data = [int(x) for x in input_file]
    return data


def find_jolt_distribution(adapters):
    jump_1_count = 0
    jump_3_count = 0
    for i in range(1, len(adapters)):
        diff = adapters[i]-adapters[i-1]
        jump_1_count += (diff == 1)
        jump_3_count += (diff == 3)
    return jump_1_count * jump_3_count


def tribonacci_n(n, cache):
    if n in cache:
        return cache[n]

    trib_n = tribonacci_n(n-1, cache)
    trib_n += tribonacci_n(n-2, cache)
    trib_n += tribonacci_n(n-3, cache)
    cache[n] = trib_n
    return trib_n


def count_arrangements(adapters):
    count = 1
    consequtive_1_jumps = 0
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i-1]
        if diff == 1:
            consequtive_1_jumps += 1
        elif diff == 3:
            count *= tribonacci_n(consequtive_1_jumps + 3, trib_001_cache)
            consequtive_1_jumps = 0
    return count


if __name__ == "__main__":
    timer = Advent_Timer()
    adapters = read_adapters()
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    print("Input parsed!")
    timer.checkpoint_hit()

    star_1_answer = find_jolt_distribution(adapters)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    star_2_answer = count_arrangements(adapters)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
