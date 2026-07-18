from day1 import Dial, Direction, parse_instruction, solve_part_1, solve_part_2


def test_move_right_less_than_100_marks():
    dial = Dial(5)
    dial.rotate_part_1(Direction.R, 10)
    assert dial.get_position() == 15


def test_move_right_more_than_100_marks():
    dial = Dial(5)
    dial.rotate_part_1(Direction.R, 150)
    assert dial.get_position() == 55


def test_move_left_less_than_100_marks():
    dial = Dial(5)
    dial.rotate_part_1(Direction.L, 10)
    assert dial.get_position() == 95


def test_parse_instruction():
    assert parse_instruction("R10") == (Direction.R, 10)
    assert parse_instruction("L20") == (Direction.L, 20)


def test_solve_test_input_part_1():
    lines = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    assert solve_part_1(lines) == 3


def test_solve_sample_input_part_1():
    lines = ["L10", "R10"]
    assert solve_part_1(lines) == 0


def test_solve_test_input_part_2():
    lines = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    assert solve_part_2(lines) == 6


# --------------------------------------------------------------------------
# rotate left
# --------------------------------------------------------------------------
def test_rotate_left_initial_at_zero_case_1():
    dial = Dial(0)
    dial.rotate_part_2(Direction.L, 5)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 0


def test_rotate_left_initial_at_zero_distance_100():
    dial = Dial(0)
    dial.rotate_part_2(Direction.L, 100)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_left_initial_at_zero_distance_150():
    dial = Dial(0)
    dial.rotate_part_2(Direction.L, 150)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_part2_less_than_initial():
    dial = Dial(50)
    dial.rotate_part_2(Direction.L, 10)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 0


def test_rotate_part2_same_initial():
    dial = Dial(50)
    dial.rotate_part_2(Direction.L, 50)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_more_than_initial_less_than_initial_plus_100_case_1():
    dial = Dial(50)
    dial.rotate_part_2(Direction.L, 100)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_more_than_initial_less_than_initial_plus_100_case_2():
    dial = Dial(50)
    dial.rotate_part_2(Direction.L, 75)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_more_than_initial_less_than_initial_plus_100_case_3():
    dial = Dial(50)
    dial.rotate_part_2(Direction.L, 149)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_position_after_rotation_is_0_case_1():
    dial = Dial(50)
    dial.rotate_part_2(Direction.L, 50)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_position_after_rotation_is_0_case_2():
    dial = Dial(50)
    dial.rotate_part_2(Direction.L, 150)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 2


def test_large_rotation_case_1():
    dial = Dial(50)
    dial.rotate_part_2(Direction.L, 1575)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 16


def test_large_rotation_case_2():
    dial = Dial(45)
    dial.rotate_part_2(Direction.L, 1525)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 15


# --------------------------------------------------------------------------
# rotate right
# --------------------------------------------------------------------------
def test_rotate_right_initial_at_zero_case_1():
    dial = Dial(0)
    dial.rotate_part_2(Direction.R, 5)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 0


def test_rotate_right_part2_less_than_initial():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 10)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 0


def test_rotate_right_part2_same_initial():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 50)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_right_more_than_initial_less_than_initial_plus_100_case_1():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 100)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_right_more_than_initial_less_than_initial_plus_100_case_2():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 75)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_right_more_than_initial_less_than_initial_plus_100_case_3():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 149)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_right_position_after_rotation_is_0_case_1():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 50)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1


def test_rotate_right_position_after_rotation_is_0_case_2():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 150)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 2


def test_rotate_right_large_rotation_case_1():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 1575)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 16


def test_rotate_right_large_rotation_case_2():
    dial = Dial(45)
    dial.rotate_part_2(Direction.R, 1525)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 15


def test_rotate_right_smaller_than_zero_reached():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 10)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 0


def test_rotate_left_from_zero_distance_100():
    dial = Dial(0)
    dial.rotate_part_2(Direction.L, 100)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1, (
        f"Expected 1, got {dial.get_nr_of_times_position_at_zero_is_reached()}"
    )


def test_rotate_right_from_zero_distance_100():
    dial = Dial(0)
    dial.rotate_part_2(Direction.R, 100)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 1, (
        f"Expected 1, got {dial.get_nr_of_times_position_at_zero_is_reached()}"
    )


def test_rotate_left_distance_zero():
    dial = Dial(50)
    dial.rotate_part_2(Direction.L, 0)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 0, (
        f"Expected 0, got {dial.get_nr_of_times_position_at_zero_is_reached()}"
    )


def test_rotate_right_distance_zero():
    dial = Dial(50)
    dial.rotate_part_2(Direction.R, 0)
    assert dial.get_nr_of_times_position_at_zero_is_reached() == 0, (
        f"Expected 0, got {dial.get_nr_of_times_position_at_zero_is_reached()}"
    )
