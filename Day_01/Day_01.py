def read_data(input_file="input.txt"):
    with open(input_file, 'r') as file:
        data = [int(line) for line in file]
    return data


def find_set_with_sum(data, set_size, total=2020, all_positive=True):
    if set_size < 1:
        raise Exception("Error: set_size must be atleast 1")

    if set_size > len(data):
        raise Exception("Error: set_size must be <= the size of the data")

    if set_size == 1:
        if total in data:
            return [total]

    else:
        sub_set_size = set_size - 1
        for i, val in enumerate(data[:-sub_set_size]):
            if i >= total and all_positive:
                continue
            sub_set = find_set_with_sum(data[i+1:], sub_set_size, total-val)
            if sub_set is not None:
                return sub_set+[val]


def get_formatted_product(int_list):
    product = 1
    for x in int_list:
        product *= x
    return "x".join(map(str, int_list)) + "={}".format(product)


if __name__ == "__main__":
    data = read_data()

    pair = find_set_with_sum(data, 2)
    print("Star 1: "+get_formatted_product(pair))

    triplet = find_set_with_sum(data, 3)
    print("Star 2: "+get_formatted_product(triplet))
