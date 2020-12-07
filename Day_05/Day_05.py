class Boarding_Pass:
    def __init__(self, pass_string):
        self.row = Boarding_Pass._parse_row(pass_string)
        self.col = Boarding_Pass._parse_col(pass_string)
        self.seat_id = self.row * 8 + self.col

    def _parse_row(pass_string):
        return Boarding_Pass._string_to_binary(pass_string[0:7], "F", "B")

    def _parse_col(pass_string):
        return Boarding_Pass._string_to_binary(pass_string[7:10], "L", "R")

    def _string_to_binary(string, zero_char, one_char):
        binary_string = ""
        for char in string:
            if char == zero_char:
                binary_string += "0"
            elif char == one_char:
                binary_string += "1"
        return int(binary_string, 2)


def read_passes_from_file(filename="input.txt"):
    with open(filename, 'r') as input_file:
        passes = [Boarding_Pass(line.strip()) for line in input_file]
    return passes


def find_highest_seat_id(passes):
    seat_ids = [boarding_pass.seat_id for boarding_pass in passes]
    return max(seat_ids)


def find_my_seat_id(passes):
    seat_ids = [boarding_pass.seat_id for boarding_pass in passes]
    seat_ids.sort()

    for i in range(len(seat_ids)-1):
        if seat_ids[i] + 1 != seat_ids[i+1]:
            return seat_ids[i] + 1


if __name__ == "__main__":
    passes = read_passes_from_file()
    highest_seat_id = find_highest_seat_id(passes)
    print("Star 1: {}".format(highest_seat_id))

    my_seat_id = find_my_seat_id(passes)
    print("Star 2: {}".format(my_seat_id))
