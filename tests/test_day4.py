from day4 import determine_neighbouring_positions
from day4 import create_position
from day4 import create_printing_department
from day4 import LocationType
from day4 import solve_part_1

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
    pd = create_printing_department(lines)
    assert pd.size == (10,10)
    assert len(pd.locations) == 10


def test_solve_part_1():
    solve_part_1(lines)


def test_printing_department_str():
    pd = solve_part_1(lines)
    print(f"\n{pd}")


def test_determine_neighbouring_positions():
    pos_list = determine_neighbouring_positions(create_position(0,0),(5,5))
    assert len(pos_list) == 3

    pos_list = determine_neighbouring_positions(create_position(1,0),(5,5))
    assert len(pos_list) == 5

    pos_list = determine_neighbouring_positions(create_position(3,0),(5,5))
    assert len(pos_list) == 5

    pos_list = determine_neighbouring_positions(create_position(4,0),(5,5))
    assert len(pos_list) == 3

    pos_list = determine_neighbouring_positions(create_position(3,3),(5,5))
    assert len(pos_list) == 8

    pos_list = determine_neighbouring_positions(create_position(4,4),(5,5))
    assert len(pos_list) == 3

    pos_list = determine_neighbouring_positions(create_position(3,4),(5,5))
    assert len(pos_list) == 5

    pos_list = determine_neighbouring_positions(create_position(0,4),(5,5))
    assert len(pos_list) == 3

    pos_list = determine_neighbouring_positions(create_position(3,1),(5,5))
    assert len(pos_list) == 8

    pos_list = determine_neighbouring_positions(create_position(1,1),(5,5))
    assert len(pos_list) == 8

    pos_list = determine_neighbouring_positions(create_position(0,1),(5,5))
    assert len(pos_list) == 5


def test_count_forklift_access_locations():
    pd = create_printing_department(lines)

    assert pd.forklift_access_locations == 13