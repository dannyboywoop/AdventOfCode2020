def read_declarations(filename="input.txt"):
    with open(filename, "r") as input_file:
        groups = input_file.read().strip().split("\n\n")
    return [[set(person) for person in group.split()] for group in groups]


if __name__ == "__main__":
    answers = read_declarations()

    star_1_answer = 0
    star_2_answer = 0
    for group in answers:
        star_1_answer += len(set.union(*group))
        star_2_answer += len(set.intersection(*group))

    print("Star 1: {}".format(star_1_answer))
    print("Star 2: {}".format(star_2_answer))
