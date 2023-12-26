from typing import List


class Case:
    def __init__(self) -> None:
        self.start = 0  # start is from 0-23
        self.end = 0  # end is from 1-24
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

    def add_bonus(self, amount: int) -> None:
        self.bonus = self.bonus + amount


class ScheduleGenerator:
    def __init__(self, num_cases=10, num_doctors=10) -> None:
        self.num_cases = num_cases
        self.num_doctors = num_doctors

    def generate_schedule(self) -> List[Case]:
        pass
