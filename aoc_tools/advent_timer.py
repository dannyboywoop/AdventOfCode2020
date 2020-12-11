from time import perf_counter


class Advent_Timer:
    def __init__(self):
        self.last_checkpoint = self.start_time = perf_counter()

    def checkpoint_hit(self):
        time = perf_counter()
        time_elapsed = time - self.last_checkpoint
        print("Checkpoint time: {:.4f} seconds\n".format(time_elapsed))
        self.last_checkpoint = time

    def end_hit(self):
        total_time = perf_counter() - self.start_time
        print("Total time: {:.4f} seconds".format(total_time))
