class BatteryBank:
    _bank: tuple[int, ...]

    def __init__(self, bank_str: str):
        self._bank = tuple(map(int, bank_str))

    def _max_subsequence(self, k: int) -> int:
        stack = []
        n = len(self._bank)
        for i, v in enumerate(self._bank):
            while stack and stack[-1] < v and len(stack) - 1 + n - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(v)
        return int("".join(map(str, stack)))

    @property
    def highest_joltage_part_1(self) -> int:
        return self._max_subsequence(2)

    @property
    def highest_joltage_part_2(self) -> int:
        return self._max_subsequence(12)


def solve_part_1(lines: list[str]) -> int:
    return sum(BatteryBank(bank_str=line).highest_joltage_part_1 for line in lines)


def solve_part_2(lines: list[str]) -> int:
    return sum(BatteryBank(bank_str=line).highest_joltage_part_2 for line in lines)
