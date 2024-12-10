def file_as_line(file):
    with open(file, encoding="utf-8") as f:
        return f.readline().strip()

def get_floor(line):
    floor = 0
    for i, c in enumerate(line):
        if c == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i + 1

def solve():
    line = file_as_line("input")

    up = line.count("(")
    down = line.count(")")

    print(f"P1: {up - down}")
    print(f"P2: {get_floor(line)}")

solve()