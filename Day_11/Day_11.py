from operator import add
from copy import deepcopy


class Seat:
    def __init__(self, position, occupied):
        self.occupied = occupied
        self.neighbours = []
        self.adjacencies = 0


def parse_seats(seating_array):
    seats = {}
    for i, row in enumerate(seating_array):
        for j, val in enumerate(seating_array[i]):
            if val == ".":
                continue
            seats[(i, j)] = Seat((i, j), val == "#")
    return seats


def read_seats(filename="input.txt"):
    with open(filename, "r") as file:
        seating_array = [line.strip() for line in file]
    return parse_seats(seating_array)


def populate_neighbours(seats, neighbour_eval_func):
    for position, seat in seats.items():
        for neighbour_pos in neighbour_eval_func(seats, position):
            seat.neighbours += [neighbour_pos]
            seats[neighbour_pos].neighbours += [position]


def adjacent_neighbours(seats, position):
    adjacent_neighbours = []

    # check 3 above and 1 directly left
    for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1)]:
        test_position = tuple(map(add, position, direction))
        if test_position in seats:
            adjacent_neighbours += [test_position]
    return adjacent_neighbours


def get_changes(seats, max_neighbours):
    changes = {}
    for position, seat in seats.items():
        if seat.occupied and seat.adjacencies >= max_neighbours:
            changes[position] = False
        elif not seat.occupied and seat.adjacencies == 0:
            changes[position] = True
    return changes


def update_seats(seats, changes):
    for position, now_occupied in changes.items():
        seats[position].occupied = now_occupied
        for neighbour in seats[position].neighbours:
            if now_occupied:
                seats[neighbour].adjacencies += 1
            else:
                seats[neighbour].adjacencies -= 1


def find_steady_state(seats, neighbour_eval_func, max_neighbours):
    current_seats = deepcopy(seats)
    populate_neighbours(current_seats, neighbour_eval_func)
    while True:
        changes = get_changes(current_seats, max_neighbours)
        if len(changes) == 0:
            break
        update_seats(current_seats, changes)
    return current_seats


if __name__ == "__main__":
    seats = read_seats()

    steady_state_1 = find_steady_state(seats, adjacent_neighbours, 4)
    star_1_answer = sum(seat.occupied for seat in steady_state_1.values())
    print("Star 1: {}".format(star_1_answer))
