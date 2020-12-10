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


def tribonacci_n(n, sequence={1: 0, 2: 0, 3: 1}):
    if n in sequence:
        return sequence[n]

    trib_n = tribonacci_n(n-1) + tribonacci_n(n-2) + tribonacci_n(n-3)
    sequence[n] = trib_n
    return trib_n


def count_arrangements(adapters):
    count = 1
    consequtive_1_jumps = 0
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i-1]
        if diff == 1:
            consequtive_1_jumps += 1
        else:
            count *= tribonacci_n(consequtive_1_jumps + 3)
            consequtive_1_jumps = 0
    return count


if __name__ == "__main__":
    adapters = read_adapters()
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)

    star_1_answer = find_jolt_distribution(adapters)
    print("Star 1: {}".format(star_1_answer))

    star_2_answer = count_arrangements(adapters)
    print("Star 2: {}".format(star_2_answer))
