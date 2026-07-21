from day4 import Position
from day4 import PrintingDepartment
from day4 import LocationType
from day4 import solve_part_2

lines = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@."
]


def test_location_type_from_string():
    assert LocationType.from_string(".") == LocationType.EMPTY
    assert LocationType.from_string("@") == LocationType.PAPER_ROLL


def test_create_printing_department():
    pd = PrintingDepartment.from_lines(lines)
    assert pd.width == 10
    assert pd.height == 10
    assert len(pd._locations) == 100


def test_solve_part_2():
    assert solve_part_2(lines) == 43


def test_printing_department_str():
    pd = PrintingDepartment.from_lines(lines)
    print(f"\n{pd}")


def test_determine_neighbouring_positions():
    pos_list = Position(0,0,5,5).all_neighbours
    assert len(pos_list) == 3

    pos_list = Position(1,0,5,5).all_neighbours
    assert len(pos_list) == 5

    pos_list = Position(3,0,5,5).all_neighbours
    assert len(pos_list) == 5

    pos_list = Position(4,0,5,5).all_neighbours
    assert len(pos_list) == 3

    pos_list = Position(3,3,5,5).all_neighbours
    assert len(pos_list) == 8

    pos_list = Position(4,4,5,5).all_neighbours
    assert len(pos_list) == 3

    pos_list = Position(3,4,5,5).all_neighbours
    assert len(pos_list) == 5

    pos_list = Position(0,4,5,5).all_neighbours
    assert len(pos_list) == 3

    pos_list = Position(3,1,5,5).all_neighbours
    assert len(pos_list) == 8

    pos_list = Position(1,1,5,5).all_neighbours
    assert len(pos_list) == 8

    pos_list = Position(0,1,5,5).all_neighbours
    assert len(pos_list) == 5


def test_count_forklift_access_locations():
    pd = PrintingDepartment.from_lines(lines)
    assert pd.forklift_access_locations == 13


def test_find_all_accessible_paper_roll_positions():
    pd = PrintingDepartment.from_lines(lines)
    assert len(pd.find_all_accessible_paper_roll_positions()) == 13