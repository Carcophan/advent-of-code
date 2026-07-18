from day3 import BatteryBank, solve_part_1


def test_highest_joltage():
    assert BatteryBank("987654321111111").highest_joltage == 98
    assert BatteryBank("811111111111119").highest_joltage == 89
    assert BatteryBank("234234234234278").highest_joltage == 78
    assert BatteryBank("818181911112111").highest_joltage == 92


def test_solve_1():
    assert (
        solve_part_1(
            ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
        )
        == 357
    )
