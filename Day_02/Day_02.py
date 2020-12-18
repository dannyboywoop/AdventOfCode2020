from aoc_tools import Advent_Timer


class Password:
    def __init__(self, input_string):
        rule_string, letter_string, self.password = input_string.split(" ")
        self.rule_val_1, self.rule_val_2 = Password._parse_rule(rule_string)
        self.required_letter = letter_string.strip(":")

    def _parse_rule(rule_string):
        return [int(val) for val in rule_string.split("-")]

    def is_valid_rule_1(self):
        count = self.password.count(self.required_letter)
        return self.rule_val_1 <= count <= self.rule_val_2

    def is_valid_rule_2(self):
        letter_in_pos_count = 0
        if self.password[self.rule_val_1-1] == self.required_letter:
            letter_in_pos_count += 1
        if self.password[self.rule_val_2-1] == self.required_letter:
            letter_in_pos_count += 1
        return letter_in_pos_count == 1


def read_passwords_from_file(filename="input.txt"):
    with open(filename, "r") as input_file:
        passwords = [Password(line.strip()) for line in input_file]
    return passwords


def count_valid_passwords_rule_1(passwords):
    return [pwd.is_valid_rule_1() for pwd in passwords].count(True)


def count_valid_passwords_rule_2(passwords):
    return [pwd.is_valid_rule_2() for pwd in passwords].count(True)


if __name__ == "__main__":
    timer = Advent_Timer()
    passwords = read_passwords_from_file()
    print("Input parsed!")
    timer.checkpoint_hit()

    valid_passwords_rule_1 = count_valid_passwords_rule_1(passwords)
    print("Star_01: {}".format(valid_passwords_rule_1))
    timer.checkpoint_hit()

    valid_passwords_rule_2 = count_valid_passwords_rule_2(passwords)
    print("Star_02: {}".format(valid_passwords_rule_2))
    timer.checkpoint_hit()

    timer.end_hit()
