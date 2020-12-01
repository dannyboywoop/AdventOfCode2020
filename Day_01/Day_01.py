def read_data(input_file="input.txt"):
    with open(input_file, 'r') as file:
        data = [int(line) for line in file]
    return data


def find_pair_with_sum(data, total=2020):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]+data[j] == total:
                return (data[i], data[j])


def find_triplet_with_sum(data, total=2020):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            for k in range(j+1, len(data)):
                if data[i]+data[j]+data[k] == total:
                    return (data[i], data[j], data[k])


if __name__ == "__main__":
    data = read_data()
    pair = find_pair_with_sum(data)
    print("Star 1: {}x{}={}".format(pair[0],
                                    pair[1],
                                    pair[0]*pair[1]))

    triplet = find_triplet_with_sum(data)
    product = triplet[0]*triplet[1]*triplet[2]
    print("Star 2: {}x{}x{}={}".format(triplet[0],
                                       triplet[1],
                                       triplet[2],
                                       product))
