class Password:
    def __init__(self, input_list):
        self.rule_vals = Password._parse_rule(input_list[0])
        self.required_letter = input_list[1][0]
        self.password = input_list[2]

    def _parse_rule(range_string):
        return [int(val) for val in range_string.split("-")]

    def is_valid_rule_1(self):
        count = 0
        for letter in self.password:
            if letter == self.required_letter:
                count += 1
        return self.rule_vals[0] <= count <= self.rule_vals[1]

    def is_valid_rule_2(self):
        letter_in_pos_count = 0
        if self.password[self.rule_vals[0]-1] == self.required_letter:
            letter_in_pos_count += 1
        if self.password[self.rule_vals[1]-1] == self.required_letter:
            letter_in_pos_count += 1
        return letter_in_pos_count == 1


def read_passwords_from_file(filename="input.txt"):
    with open(filename, "r") as input_file:
        passwords = [Password(line.strip().split(" ")) for line in input_file]
    return passwords


def count_valid_passwords_rule_1(passwords):
    valid_passwords = [pwd for pwd in passwords if pwd.is_valid_rule_1()]
    return len(valid_passwords)


def count_valid_passwords_rule_2(passwords):
    valid_passwords = [pwd for pwd in passwords if pwd.is_valid_rule_2()]
    return len(valid_passwords)


if __name__ == "__main__":
    passwords = read_passwords_from_file()

    valid_passwords_rule_1 = count_valid_passwords_rule_1(passwords)
    print("Star_01: {}".format(valid_passwords_rule_1))

    valid_passwords_rule_2 = count_valid_passwords_rule_2(passwords)
    print("Star_02: {}".format(valid_passwords_rule_2))
