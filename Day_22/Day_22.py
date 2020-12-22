from aoc_tools import Advent_Timer
from re import findall
from copy import deepcopy


def parse_hand(hand_string):
    start_pos = hand_string.find(":")
    hand = list(map(int, findall("\d+", hand_string[start_pos:])))
    return hand


def read_data(filename="input.txt"):
    with open(filename, 'r') as input_file:
        hands = input_file.read().strip().split("\n\n")
    return [parse_hand(hand) for hand in hands]


def play_combat(hands):
    while len(hands[0]) > 0 and len(hands[1]) > 0:
        cards = [hand.pop(0) for hand in hands]
        winner = cards[1] > cards[0]
        hands[winner] += sorted(cards, reverse=True)
    return max(hands, key=len)


def get_winning_score(winning_hand):
    answer = 0
    for i, card in enumerate(reversed(winning_hand)):
        answer += (i + 1) * card
    return answer


def star_1(hands):
    hands = deepcopy(hands)
    winning_hand = play_combat(hands)
    return get_winning_score(winning_hand)


if __name__ == "__main__":
    timer = Advent_Timer()

    hands = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    star_1_answer = star_1(hands)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    timer.end_hit()
