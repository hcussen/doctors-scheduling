from typing import List
import numpy as np


class Case:
    def __init__(self) -> None:
        self.start = 0  # start is from 0-23
        self.end = 1  # end is from 1-24
        self.difficulty = 0  # between 1 and 10
        self.location = ""
        self.base_compensation = 0
        self.bonus = 0

    def get_start(self) -> int:
        return self.start

    def get_end(self) -> int:
        return self.end

    def get_length(self) -> int:
        return self.end - self.start

    def get_difficulty(self) -> int:
        return self.difficulty

    def get_comp(self) -> int:
        return self.base_compensation + self.bonus

    def set_start(self, start: int) -> None:
        assert start < self.end, "start time is not less than end time"
        assert start in list(
            range(0, 24)
        ), "start time is not within range 0, 23 inclusive"
        self.start = start

    def set_end(self, end: int) -> None:
        assert end > self.start, "end time is not greater than start time"
        assert end in list(range(1, 25)), "end time is not within range 1, 24 inclusive"
        self.end = end

    def set_difficulty(self, difficulty) -> None:
        assert difficulty in list(
            range(1, 11)
        ), f"difficulty is {difficulty} is not an integer between 1 and 10"
        self.difficulty = difficulty

    def add_bonus(self, amount: int) -> None:
        self.bonus = self.bonus + amount


class ScheduleGenerator:
    def __init__(self, num_cases=10, num_doctors=10) -> None:
        self.num_cases = num_cases
        self.num_doctors = num_doctors
        self.compensation_scheme = "regular"
        # regular compensation is 100 dollars an hour
        self.hourly_rate = 100
        self.schedule = []

    def generate_schedule(self) -> List[Case]:
        # Create a random number generator instance
        rng = np.random.default_rng()

        cases_difficulty = rng.integers(
            low=1, high=10, endpoint=True, size=(self.num_cases)
        )
        cases_starts = rng.integers(
            low=1, high=23, endpoint=True, size=(self.num_cases)
        )
        cases_ends = cases_starts + cases_difficulty
        cases_ends = np.where(cases_ends > 24, 24, cases_ends)
        arrays = [cases_difficulty, cases_starts, cases_ends]
        data = np.stack(arrays, axis=0)
        print(data)
        cases = []
        for i in range(self.num_cases):
            print(data[:, i])
            difficulty, start, end = data[:, i]
            c = Case()
            c.set_difficulty(difficulty)
            c.set_end(end)
            c.set_start(start)
        self.schedule = cases

    def get_schedule(self):
        return self.schedule

    def print_schedule(self):
        pass


def main():
    s = ScheduleGenerator()
    s.generate_schedule()


if __name__ == "__main__":
    main()
