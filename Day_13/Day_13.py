from aoc_tools.advent_timer import Advent_Timer


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


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    start_time, buses = read_input("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    depart_time, bus_id = earliest_departure(start_time, buses)
    print("Star 1: {}".format((depart_time-start_time) * bus_id))
    timer.checkpoint_hit()

    timer.end_hit()
