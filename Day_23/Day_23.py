from aoc_tools import Advent_Timer


INPUT = "315679824"


class Circular_Linked_List:
    def __init__(self, array):
        self._links = {array[i-1]: array[i] for i in range(len(array))}

    def get_next(self, value):
        return self._links[value]

    def pop(self, start, num):
        removed_items = []
        next_item = self._links[start]
        for _ in range(num):
            removed_items.append(next_item)
            next_item = self._links.pop(next_item)
        self._links[start] = next_item
        return removed_items

    def insert(self, start, array):
        final_link = self._links[start]
        previous_item = start
        for item in array:
            self._links[previous_item] = item
            previous_item = item
        self._links[previous_item] = final_link


class Cup_Game:
    def __init__(self, cups):
        self.cups = Circular_Linked_List(cups)
        self.min_cup = min(cups)
        self.max_cup = max(cups)
        self.current_cup = cups[0]

    def _make_move(self):
        # remove 3 cups
        removed = self.cups.pop(self.current_cup, 3)

        # find destination
        destination_found = False
        destination = self.current_cup - 1
        while not destination_found:
            destination_found = True
            if destination in removed:
                destination -= 1
                destination_found = False
            if destination < self.min_cup:
                destination = self.max_cup
                destination_found = False

        # insert removed cups in destination
        self.cups.insert(destination, removed)

        # increment current_cup
        self.current_cup = self.cups.get_next(self.current_cup)

    def play_turns(self, num_of_turns):
        for _ in range(num_of_turns):
            self._make_move()

    def get_labels_after_1(self):
        answer = ""
        cup = 1
        while True:
            next_cup = self.cups.get_next(cup)
            if next_cup == 1:
                break
            answer += str(next_cup)
            cup = next_cup
        return answer

    def get_next_2_cups(self, cup):
        next_cup_1 = self.cups.get_next(cup)
        next_cup_2 = self.cups.get_next(next_cup_1)
        return next_cup_1, next_cup_2


def star_1(start_order):
    cups = [int(char) for char in start_order]
    game = Cup_Game(cups)
    game.play_turns(100)
    return game.get_labels_after_1()


def star_2(start_order):
    cups = [int(char) for char in start_order]
    cups += [x for x in range(max(cups) + 1, 1000001)]
    game = Cup_Game(cups)
    game.play_turns(10000000)
    next_cup_1, next_cup_2 = game.get_next_2_cups(1)
    return next_cup_1 * next_cup_2


if __name__ == "__main__":
    timer = Advent_Timer()

    star_1_answer = star_1(INPUT)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    star_2_answer = star_2(INPUT)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
