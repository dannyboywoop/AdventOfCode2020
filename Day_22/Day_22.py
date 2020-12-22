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


def state_representation(hands):
    return tuple(tuple(hand) for hand in hands)


def play_recursive_combat(hands):
    state_cache = set()
    while len(hands[0]) > 0 and len(hands[1]) > 0:
        # check for reoccuring game state
        state_rep = state_representation(hands)
        if state_rep in state_cache:
            # end game with player 1 victory
            return 0
        state_cache.add(state_rep)

        # play cards
        cards = [hand.pop(0) for hand in hands]

        # check if players have too few cards for recursion
        if cards[0] > len(hands[0]) or cards[1] > len(hands[1]):
            winner = cards[1] > cards[0]
            hands[winner] += sorted(cards, reverse=True)
            continue

        # recurse game
        sub_hands = [hands[0][:cards[0]], hands[1][:cards[1]]]
        sub_winner = play_recursive_combat(sub_hands)
        hands[sub_winner] += [cards[sub_winner], cards[sub_winner - 1]]

    # return winning hand index
    return len(hands[0]) == 0


def get_winning_score(winning_hand):
    answer = 0
    for i, card in enumerate(reversed(winning_hand)):
        answer += (i + 1) * card
    return answer


def star_1(hands):
    hands = deepcopy(hands)
    winning_hand = play_combat(hands)
    return get_winning_score(winning_hand)


def star_2(hands):
    hands = deepcopy(hands)
    winner = play_recursive_combat(hands)
    return get_winning_score(hands[winner])


if __name__ == "__main__":
    timer = Advent_Timer()

    hands = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    star_1_answer = star_1(hands)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    star_2_answer = star_2(hands)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
