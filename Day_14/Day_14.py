from aoc_tools import Advent_Timer


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [line.strip().split(" = ") for line in file]
    return data


def apply_mask_1(mask, val):
    val_binary = "{:036b}".format(val)
    ans_binary = ""
    for i, char in enumerate(mask):
        if char == "X":
            ans_binary += val_binary[i]
        else:
            ans_binary += char
    return int(ans_binary, 2)


def star_1(data):
    mask = ""
    memory = {}
    for key, val in data:
        if key == "mask":
            mask = val
            continue
        index = int(key[4:-1])
        memory[index] = apply_mask_1(mask, int(val))
    return sum(memory.values())


def apply_mask_2(mask, val):
    val_binary = "{:036b}".format(val)
    ans_binaries = [""]
    for i, char in enumerate(mask):
        if char == "0":
            ans_binaries = [curr + val_binary[i] for curr in ans_binaries]
        elif char == "1":
            ans_binaries = [curr + "1" for curr in ans_binaries]
        else:
            zero_options = [curr + "0" for curr in ans_binaries]
            one_options = [curr + "1" for curr in ans_binaries]
            ans_binaries = zero_options + one_options
    return [int(ans, 2) for ans in ans_binaries]


def star_2(data):
    mask = ""
    memory = {}
    for key, val in data:
        if key == "mask":
            mask = val
            continue
        indices = apply_mask_2(mask, int(key[4:-1]))
        for index in indices:
            memory[index] = int(val)
    return sum(memory.values())


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer = star_1(data)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    star_2_answer = star_2(data)
    print("Star 1: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
