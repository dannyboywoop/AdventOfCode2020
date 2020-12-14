from aoc_tools.advent_timer import Advent_Timer


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

    timer.end_hit()
