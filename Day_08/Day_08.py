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
    return terminated_safely, index, accumulator


if __name__ == "__main__":
    program = read_program()
    _, _, star_1_answer = run_program(program)
    print("Star 1: {}".format(star_1_answer))
