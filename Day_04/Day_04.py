REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def list_to_dict(some_list):
    array = [field.split(":") for field in some_list]
    dictionary = {key: val for key, val in array}
    return dictionary


def read_passports(filename="input.txt"):
    with open(filename, "r") as passport_file:
        all_text = passport_file.read().strip()
    passport_array = [string.split() for string in all_text.split("\n\n")]
    passports = [list_to_dict(passport) for passport in passport_array]
    return passports


def passport_has_all_fields(passport):
    for field in REQUIRED_FIELDS:
        if field not in passport.keys():
            return False
    return True


def count_passports_with_all_fields(passports):
    count = 0
    for passport in passports:
        count += passport_has_all_fields(passport)
    return count


if __name__ == "__main__":
    passports = read_passports()
    passports_with_all_fields = count_passports_with_all_fields(passports)
    print("Star 1: {}".format(passports_with_all_fields))
