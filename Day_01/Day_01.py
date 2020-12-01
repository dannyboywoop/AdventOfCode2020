def read_data(input_file="input.txt"):
    with open(input_file, 'r') as file:
        data = [int(line) for line in file]
    return data


def find_pair_with_sum(data, total=2020):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]+data[j] == total:
                return (data[i], data[j])


if __name__ == "__main__":
    data = read_data()
    pair = find_pair_with_sum(data)
    print("Star 1: {}x{}={}".format(pair[0],
                                    pair[1],
                                    pair[0]*pair[1]))
