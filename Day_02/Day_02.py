class Password:
    def __init__(self, input_list):
        self.allowed_range = Password._parse_range(input_list[0])
        self.required_letter = input_list[1][0]
        self.password = input_list[2]

    def _parse_range(range_string):
        minimum, inclusive_max = map(int, range_string.split("-"))
        return range(minimum, inclusive_max+1)

    def is_valid(self):
        count = 0
        for letter in self.password:
            if letter == self.required_letter:
                count += 1
        return count in self.allowed_range


def read_passwords_from_file(filename="input.txt"):
    with open(filename, "r") as input_file:
        passwords = [Password(line.strip().split(" ")) for line in input_file]
    return passwords


def count_valid_passwords(passwords):
    valid_passwords = [pwd for pwd in passwords if pwd.is_valid()]
    return len(valid_passwords)


if __name__ == "__main__":
    passwords = read_passwords_from_file()
    valid_passwords = count_valid_passwords(passwords)
    print("Star_01: {}".format(valid_passwords))
