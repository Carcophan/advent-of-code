from day4 import solve_part_2
import time
from pathlib import Path



def read_lines(filepath: str | Path) -> list[str]:
    """Reads a text file and returns its lines as a list of strings.

    Trailing newlines (\r\n or \n) are stripped.
    """
    path = Path(filepath)
    with path.open("r", encoding="utf-8") as f:
        return [line.rstrip("\r\n") for line in f]


if __name__ == "__main__":
    input_file = Path(__file__).parent / "day4-input.txt"
    lines = read_lines(input_file)

    start_time = time.perf_counter()
    result = solve_part_2(lines)
    execution_time = time.perf_counter() - start_time
    print(f"Result: {result}")
    print(f"Execution time: {execution_time:.6f} seconds")
