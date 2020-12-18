from aoc_tools import Advent_Timer
from numpy import lcm, int64


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        start_time, buses_string = [line.strip() for line in file]
    buses = [(int(bus), i)
             for i, bus in enumerate(buses_string.split(","))
             if bus != "x"]
    return int(start_time), buses


def earliest_departure(start_time, buses):
    time = start_time
    while True:
        for bus_id, _ in buses:
            if time % bus_id == 0:
                return time, bus_id
        time += 1


def deltas_correct(time, buses):
    for bus_id, delta in buses:
        if (time + delta) % bus_id > 0:
            return False
    return True


def prize_time(buses):
    time = 1
    interval = 1
    for i in range(len(buses)):
        bus_ids_to_check = [bus_id for bus_id, _ in buses[:i+1]]
        while True:
            if deltas_correct(time, buses[:i+1]):
                break
            time += interval
        interval = int(lcm.reduce(bus_ids_to_check, dtype=int64))
    return time


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    start_time, buses = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    depart_time, bus_id = earliest_departure(start_time, buses)
    print("Star 1: {}".format((depart_time-start_time) * bus_id))
    timer.checkpoint_hit()

    # star 2
    star_2_answer = prize_time(buses)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
