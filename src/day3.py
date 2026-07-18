from dataclasses import dataclass


@dataclass
class BatteryBank:
    _bank: tuple[int]

    def __init__(self, bank_str: str):
        self._bank = tuple(map(int, bank_str))

    @property
    def highest_joltage(self) -> int:
        sorted_ = sort_desc(self._bank)

        battery_a = sorted_[0]
        battery_a_index = self._bank.index(battery_a)

        first_digit = 0
        second_digit = 0

        if battery_a_index == len(self._bank) - 1:
            first_digit = sorted_[1]
            second_digit = battery_a
        else:
            first_digit = battery_a
            second_digit = sort_desc(self._bank[self._bank.index(first_digit) + 1 :])[0]

        return int(f"{first_digit}{second_digit}")


def sort_desc(input_: list[int]) -> list[int]:
    return sorted(input_, reverse=True)


def solve_part_1(lines: list[str]) -> int:
    return sum(BatteryBank(bank_str=line).highest_joltage for line in lines)
