from functools import cached_property
from enum import Enum, unique
from dataclasses import dataclass
from typing import Self


@unique
class LocationType(Enum):
    EMPTY = 0
    PAPER_ROLL = 1

    @classmethod
    def from_string(cls, char: str) -> Self:
        if char == '.': return cls.EMPTY
        if char == '@': return cls.PAPER_ROLL
        raise ValueError(f"Unknown LocationType char: {char}")
        

@dataclass(frozen=True)
class Position:
    x: int
    y: int
    board_size_width: int
    board_size_height: int

    @cached_property
    def all_neighbours(self) -> set['Position']:
        """Calculates valid neighbours based on grid boundaries."""
        neighbours = set()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < self.board_size_width and 0 <= ny < self.board_size_height:
                    neighbours.add(Position(nx, ny, self.board_size_width, self.board_size_height))
        return neighbours


@dataclass(slots=True, frozen=True)
class PrintingDepartment:
    width: int
    height: int
    _locations: dict[Position, LocationType]

    @classmethod
    def from_lines(cls, lines: list[str]) -> Self:
        width = len(lines[0])
        height = len(lines)
        locations: dict[Position, LocationType] = {}
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                locations[Position(x, y, width, height)] = LocationType.from_string(char)
        return cls(width=width, height=height, _locations=locations)

    def get_type_at(self, pos: Position) -> LocationType:
        return self._locations.get(pos, LocationType.EMPTY)

    def is_accessible_by_forklift(self, pos: Position) -> bool:
        if self.get_type_at(pos) != LocationType.PAPER_ROLL:
            return False
            
        neighbours = pos.all_neighbours
        paper_roll_neighbours = sum(
            1 for n in neighbours if self.get_type_at(n) == LocationType.PAPER_ROLL
        )
        return paper_roll_neighbours < 4

    def _remove_paper_roll(self, position: Position):
        self._locations[position]=LocationType.EMPTY

    def find_all_accessible_paper_roll_positions(self) -> list[Position]:
        return [
           pos for pos, l_type in self._locations.items() if self.is_accessible_by_forklift(pos)
        ]
    

    @property
    def forklift_access_locations(self) -> int:
        return sum(
            1 for pos in self._locations 
            if self.is_accessible_by_forklift(pos)
        )

def solve_part_2(lines: list[str]) -> int:
    pd = PrintingDepartment.from_lines(lines)

    paper_roll_pos_list = pd.find_all_accessible_paper_roll_positions()

    result = 0
    while len(paper_roll_pos_list) > 0:
        for pos in paper_roll_pos_list:
            pd._remove_paper_roll(pos)
            result += 1
        paper_roll_pos_list = pd.find_all_accessible_paper_roll_positions()

    return result