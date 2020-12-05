class Boarding_Pass:
    def __init__(self, pass_string):
        self.row = Boarding_Pass._parse_row(pass_string)
        self.col = Boarding_Pass._parse_col(pass_string)
        self.seat_id = self.row * 8 + self.col

    def _parse_row(pass_string):
        binary = pass_string[0:7].replace("F", "0").replace("B", "1")
        return int(binary, 2)

    def _parse_col(pass_string):
        binary = pass_string[7:10].replace("L", "0").replace("R", "1")
        return int(binary, 2)


def read_passes_from_file(filename="input.txt"):
    with open(filename, 'r') as input_file:
        passes = [Boarding_Pass(line.strip()) for line in input_file]
    return passes


def find_highest_seat_id(passes):
    seat_ids = [boarding_pass.seat_id for boarding_pass in passes]
    return max(seat_ids)


if __name__ == "__main__":
    passes = read_passes_from_file()
    highest_seat_id = find_highest_seat_id(passes)
    print("Star 1: {}".format(highest_seat_id))
