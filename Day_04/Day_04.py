from aoc_tools import Advent_Timer
from re import match


REQUIRED_FIELDS = {"byr": r"^(19[2-9]\d|200[0-2])$",
                   "iyr": r"^20(1\d|20)$",
                   "eyr": r"^20(2\d|30)$",
                   "hgt": r"^((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)$",
                   "hcl": r"^#[a-f\d]{6}$",
                   "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
                   "pid": r"^\d{9}$"}


def list_to_dict(some_list):
    array = [field.split(":") for field in some_list]
    dictionary = {key: val for key, val in array}
    return dictionary


def read_passports(filename="input.txt"):
    with open(filename, "r") as passport_file:
        all_text = passport_file.read()
    passport_array = [string.split() for string in all_text.split("\n\n")]
    passports = [list_to_dict(passport) for passport in passport_array]
    return passports


def passport_has_all_fields(passport):
    for field in REQUIRED_FIELDS.keys():
        if field not in passport.keys():
            return False
    return True


def count_passports_with_all_fields(passports):
    count = 0
    for passport in passports:
        count += passport_has_all_fields(passport)
    return count


def passport_is_valid(passport):
    if not passport_has_all_fields(passport):
        return False
    for field, regex in REQUIRED_FIELDS.items():
        if not bool(match(regex, passport[field])):
            return False
    return True


def count_valid_passports(passports):
    count = 0
    for passport in passports:
        count += passport_is_valid(passport)
    return count


if __name__ == "__main__":
    timer = Advent_Timer()
    passports = read_passports()
    print("Input parsed!")
    timer.checkpoint_hit()

    passports_with_all_fields = count_passports_with_all_fields(passports)
    print("Star 1: {}".format(passports_with_all_fields))
    timer.checkpoint_hit()

    valid_passports = count_valid_passports(passports)
    print("Star 2: {}".format(valid_passports))
    timer.checkpoint_hit()

    timer.end_hit()
