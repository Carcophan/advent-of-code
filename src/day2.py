def solve_part_2(lines: list[str]) -> int:
    return sum(
        i
        for p in lines[0].split(",")
        for s, e in [p.split("-")]
        for i in range(int(s), int(e) + 1)
        if len(si := str(i)) >= 2 and si in (si + si)[1:-1]
    )