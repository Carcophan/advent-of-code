from asyncio import exceptions
from asyncio import exceptions
from asyncio import exceptions
from asyncio import exceptions
from asyncio import exceptions
from asyncio import exceptions
from enum import unique
from enum import Enum
from dataclasses import dataclass

@unique
class LocationType(Enum):
    EMPTY = 0
    PAPER_ROLL = 1

    @staticmethod
    def from_string(s: str):
        match(s):
            case '.':
                return LocationType.EMPTY
            case '@':
                return LocationType.PAPER_ROLL
            case _:
                raise ValueError(f"unknown LocationType char {s}")

@dataclass(slots=True, frozen=True)
class Position:
    x: int
    y: int

def create_position(x: int, y: int):
    return Position(x, y)

@dataclass(slots=True, frozen=True)
class Location:
    location_type: LocationType
    position: Position
    neighbouring_positions: set[Position]


def create_location(location_type: LocationType, position: Position, neighbouring_positions: set[Position]) -> Location:
    return Location(location_type=location_type, position=position, neighbouring_positions=neighbouring_positions)


@dataclass(slots=True, frozen=True)
class PrintingDepartment:
    size: tuple[int,int]
    locations: dict[Position, Location]

    @property
    def forklift_access_locations(self) -> int:
        result = 0
        for loc in self.locations.values():
            if loc.location_type==LocationType.PAPER_ROLL:
                empty_np = sum (
                    self.locations[np].location_type==LocationType.PAPER_ROLL for 
                    np in loc.neighbouring_positions
                )
                if empty_np < 4:
                    result += 1
        return result

def determine_neighbouring_positions(position: Position, dep_size: tuple[int,int]):
    x = position.x
    y = position.y

    size_x, size_y = dep_size

    np: set[Position] = set()

    if y > 0:
        np.add(create_position(x, y-1))

    if x > 0:
        np.add(create_position(x-1, y))    

    if y < size_y-1:
        np.add(create_position(x, y+1))

    if x < size_x - 1:
        np.add(create_position(x+1, y))

    if y > 0 and x > 0:  
        np.add(create_position(x-1, y-1))

    if y > 0 and x < size_x - 1:
        np.add(create_position(x+1, y-1))

    if y < size_y-1 and x < size_x -1:
        np.add(create_position(x+1, y+1))    

    if y < size_y-1 and x > 0:
        np.add(create_position(x-1, y+1))

    return np
            


def create_printing_department(lines: list[str]):
    size = (len(lines[0]), len(lines))
    locations: dict[Position, Location] = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            location_type = LocationType.from_string(char)
            position = create_position(i,j)
            neighboring_positions = determine_neighbouring_positions(position, size)
            location = create_location(position=position, location_type=location_type, neighbouring_positions=neighboring_positions)

            locations[position] = location
    return PrintingDepartment(size=size, locations=locations)

        
def solve_part_1(lines: list[str]) -> int:
    pd = create_printing_department(lines)
    return pd.forklift_access_locations