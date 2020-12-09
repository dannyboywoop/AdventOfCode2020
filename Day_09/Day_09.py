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


if __name__ == "__main__":
    data = read_data()
    star_1_answer = find_first_invalid_number(data)
    print("Star 1: {}".format(star_1_answer))
