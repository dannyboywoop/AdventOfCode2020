from aoc_tools import Advent_Timer


def transform_subject_number(sn, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= sn
        value %= 20201227
    return value


def find_loop_size(public_key):
    val = public_key
    steps = 0
    while val != 1:
        if val % 7 == 0:
            val //= 7
            steps += 1
        else:
            val += 20201227
    return steps


def find_encryption_key(public_keys):
    door_key, card_key = public_keys
    door_loop_size = find_loop_size(door_key)
    return transform_subject_number(card_key, door_loop_size)


if __name__ == "__main__":
    timer = Advent_Timer()
    public_keys = [12232269, 19452773]

    encryption_key = find_encryption_key(public_keys)
    print("Star 1: {}".format(encryption_key))
    timer.checkpoint_hit()

    timer.end_hit()
