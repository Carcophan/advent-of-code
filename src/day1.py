import math
from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    L = "L"
    R = "R"

    @classmethod
    def from_char(cls, char: str) -> "Direction":
        return cls(char)


@dataclass
class Dial:
    position: int
    nr_of_marks: int = 100
    nr_of_times_position_at_zero_is_reached: int = 0

    def _rotate(self, direction, distance):
        if direction == Direction.L:
            self.position = (self.position - distance) % self.nr_of_marks
        elif direction == Direction.R:
            self.position = (self.position + distance) % self.nr_of_marks

    def rotate_part_1(self, direction: Direction, distance: int):
        self._rotate(direction, distance)

        if self.position % self.nr_of_marks == 0:
            self.nr_of_times_position_at_zero_is_reached += 1

    def rotate_part_2(self, direction: Direction, distance: int):
        match direction:
            case Direction.L:
                self.nr_of_times_position_at_zero_is_reached += (
                    ((self.position - 1) // self.nr_of_marks) - ((self.position - distance - 1) // self.nr_of_marks)
                )
            case Direction.R:
                self.nr_of_times_position_at_zero_is_reached += (
                    (self.position + distance) // self.nr_of_marks
                )
        self._rotate(direction, distance)

    def __str__(self) -> str:
        return f"Position: {self.position}, Nr of times position at zero is reached: {self.nr_of_times_position_at_zero_is_reached}"

    def get_position(self) -> int:
        return self.position

    def get_nr_of_times_position_at_zero_is_reached(self) -> int:
        return self.nr_of_times_position_at_zero_is_reached


def parse_instruction(instruction: str) -> tuple[Direction, int]:
    direction = Direction.from_char(instruction[0])
    distance = int(instruction[1:])
    return direction, distance


def solve_part_1(lines: list[str]) -> int:
    dial = Dial(position=50)
    for line in lines:
        direction, distance = parse_instruction(line)
        dial.rotate_part_1(direction, distance)
    return dial.get_nr_of_times_position_at_zero_is_reached()


def solve_part_2(lines: list[str]) -> int:
    dial = Dial(position=50)
    print(f"initial state: {dial}")
    for line in lines:
        direction, distance = parse_instruction(line)
        dial.rotate_part_2(direction, distance)
        print(f"after instruction {line}: {dial}")
    return dial.get_nr_of_times_position_at_zero_is_reached()
