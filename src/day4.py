from functools import cached_property
from enum import Enum, unique
from dataclasses import dataclass, field
from typing import Self
from collections import deque


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
    _paper_rolls: set[Position] = field(repr=False)

    @classmethod
    def from_lines(cls, lines: list[str]) -> Self:
        width = len(lines[0])
        height = len(lines)
        locations: dict[Position, LocationType] = {}
        paper_rolls = set()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                pos = Position(x, y, width, height)
                l_type = LocationType.from_string(char)
                locations[pos] = l_type
                if l_type == LocationType.PAPER_ROLL:
                    paper_rolls.add(pos)
        return cls(width=width, height=height, _locations=locations, _paper_rolls=paper_rolls)

    def get_type_at(self, pos: Position) -> LocationType:
        return self._locations.get(pos, LocationType.EMPTY)

    def is_accessible_by_forklift(self, pos: Position) -> bool:
        if pos not in self._paper_rolls:
            return False
            
        paper_roll_neighbours = sum(
            1 for n in pos.all_neighbours if n in self._paper_rolls
        )
        return paper_roll_neighbours < 4

    def _remove_paper_roll(self, position: Position):
        self._locations[position] = LocationType.EMPTY
        self._paper_rolls.discard(position)

    def find_all_accessible_paper_roll_positions(self) -> list[Position]:
        return [
           pos for pos in self._paper_rolls if self.is_accessible_by_forklift(pos)
        ]
    

    @property
    def forklift_access_locations(self) -> int:
        return sum(
            1 for pos in self._paper_rolls 
            if self.is_accessible_by_forklift(pos)
        )

def solve_part_2(lines: list[str]) -> int:
    pd = PrintingDepartment.from_lines(lines)

    queue = deque(pd.find_all_accessible_paper_roll_positions())

    result = 0
    while queue:
        pos = queue.popleft()
        if pos not in pd._paper_rolls:
            continue
            
        pd._remove_paper_roll(pos)
        result += 1
        
        for n in pos.all_neighbours:
            if n in pd._paper_rolls and pd.is_accessible_by_forklift(n):
                queue.append(n)

    return result