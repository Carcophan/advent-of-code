

from day3 import BatteryBank, solve_part_1, solve_part_2


def test_highest_joltage_part_1():
    assert BatteryBank("987654321111111").highest_joltage_part_1 == 98
    assert BatteryBank("811111111111119").highest_joltage_part_1 == 89
    assert BatteryBank("234234234234278").highest_joltage_part_1 == 78
    assert BatteryBank("818181911112111").highest_joltage_part_1 == 92


def test_solve_1():
    assert (
        solve_part_1(
            ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
        )
        == 357
    )
#----------------------------------------------------------------------

def test_highest_joltage_part_2():
    assert BatteryBank("987654321111111").highest_joltage_part_2 == 987654321111
    assert BatteryBank("811111111111119").highest_joltage_part_2 == 811111111119
    assert BatteryBank("234234234234278").highest_joltage_part_2 == 434234234278
    assert BatteryBank("818181911112111").highest_joltage_part_2 == 888911112111


def test_solve_2():
    assert (
        solve_part_2(
            ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
        )
        == 3121910778619
    )


