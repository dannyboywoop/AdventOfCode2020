from aoc_tools.advent_timer import Advent_Timer


def play_game(turn_count, starting_numbers=[1, 0, 18, 10, 19, 6]):
    # populate previously spoken with all but the last starting number
    previously_spoken = {num: i for i, num in enumerate(starting_numbers[:-1])}

    # current_number is the number most recently spoken
    current_number = starting_numbers[-1]

    # for each subsequent turn in the game
    for turn in range(len(starting_numbers), turn_count):
        if current_number in previously_spoken:
            # gap is between the previous turn and the last time it was spoken
            new_number = (turn - 1) - previously_spoken[current_number]
        else:
            new_number = 0
        # current_number was last spoken on the previous turn
        previously_spoken[current_number] = turn - 1
        current_number = new_number
    return current_number


if __name__ == "__main__":
    timer = Advent_Timer()

    # star 1
    star_1_answer = play_game(2020)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    star_2_answer = play_game(30000000)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
