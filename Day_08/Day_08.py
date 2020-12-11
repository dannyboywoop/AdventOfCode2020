from aoc_tools.advent_timer import Advent_Timer


def read_program(filename="input.txt"):
    with open(filename, "r") as input_file:
        code = [line.strip() for line in input_file]
    return [(op, int(arg)) for op, arg in [line.split() for line in code]]


def perform_operation(program, index, accumulator):
    op, arg = program[index]
    if op == "nop":
        return index + 1, accumulator
    if op == "acc":
        return index + 1, accumulator + arg
    if op == "jmp":
        return index + arg, accumulator
    return index, accumulator


def run_program(program):
    accumulator = 0
    index = 0
    visited_indices = {0}
    while index in range(len(program)):
        index, accumulator = perform_operation(program, index, accumulator)
        if index in visited_indices:
            break
        visited_indices.add(index)
    terminated_safely = (index == len(program))
    return terminated_safely, index, accumulator, visited_indices


def fix_infinite_loop(program, visited):
    indices_to_check = {}
    for index, instruction in enumerate(program):
        # only check instructions that are actually hit
        if index not in visited:
            continue

        # store potential fix
        op, arg = instruction
        if op == "nop":
            indices_to_check[index] = ("jmp", arg)
        elif op == "jmp":
            indices_to_check[index] = ("nop", arg)

    for index, new_instruction in indices_to_check.items():
        fix_program = program.copy()
        fix_program[index] = new_instruction
        terminated_safely, _, accumulator, _ = run_program(fix_program)
        if terminated_safely:
            return accumulator


if __name__ == "__main__":
    timer = Advent_Timer()
    program = read_program()
    print("Input parsed!")
    timer.checkpoint_hit()

    _, _, star_1_answer, visited = run_program(program)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    star_2_answer = fix_infinite_loop(program, visited)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
