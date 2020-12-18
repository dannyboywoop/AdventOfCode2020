from aoc_tools import Advent_Timer


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [line.strip() for line in file]
    return data


def no_precedence_evaluate(simple_expression):
    terms = simple_expression.strip("()").split(" ")
    result = int(terms.pop(0))
    for i in range(0, len(terms), 2):
        if terms[i] == "+":
            result += int(terms[i+1])
        else:
            result *= int(terms[i+1])
    return result


def evaluate_expression(expression, base_evaluate_func):
    open_bracket_indices = []
    index = 0
    while index < len(expression):
        if expression[index] == "(":
            open_bracket_indices.append(index)
        elif expression[index] == ")":
            start_index = open_bracket_indices.pop()
            sub_expression = expression[start_index:index+1]
            value = str(base_evaluate_func(sub_expression))
            expression = expression.replace(sub_expression, value)
            index += len(value) - len(sub_expression)
        index += 1
    return base_evaluate_func(expression)


def sum_expressions(expressions, base_evaluate_func):
    values = [evaluate_expression(expression, base_evaluate_func)
              for expression in expressions]
    return sum(values)


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    expressions = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer = sum_expressions(expressions, no_precedence_evaluate)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    timer.end_hit()
