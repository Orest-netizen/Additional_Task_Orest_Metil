import sys


# Завдання A
def task_a():
    print(len(set(sys.stdin.read().split())))


# Завдання B
def task_b():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if len(lines) >= 2:
        set1 = set(lines[0].split())
        set2 = set(lines[1].split())
        print(len(set1 & set2))


# Завдання C
def task_c():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if len(lines) >= 2:
        set1 = set(map(int, lines[0].split()))
        set2 = set(map(int, lines[1].split()))
        print(*(sorted(set1 & set2)))


# Завдання D
def task_d():
    numbers = sys.stdin.read().split()
    seen = set()
    for num in numbers:
        if num in seen:
            print("YES")
        else:
            print("NO")
            seen.add(num)


# Завдання E
def task_e():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    idx = 2
    set_a = set(map(int, input_data[idx: idx + n]))
    idx += n
    set_b = set(map(int, input_data[idx: idx + m]))

    inter = sorted(set_a & set_b)
    only_a = sorted(set_a - set_b)
    only_b = sorted(set_b - set_a)

    print(len(inter))
    for x in inter:
        print(x)
    print(len(only_a))
    for x in only_a:
        print(x)
    print(len(only_b))
    for x in only_b:
        print(x)


# Завдання F
def task_f():
    print(len(set(sys.stdin.read().split())))


# Завдання G
def task_g():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return
    n = int(lines[0])
    possible = set(range(1, n + 1))
    i = 1
    while i < len(lines):
        line = lines[i]
        if line == "HELP":
            break
        query = set(map(int, line.split()))
        ans = lines[i + 1]
        if ans == "YES":
            possible &= query
        elif ans == "NO":
            possible -= query
        i += 2
    print(*(sorted(possible)))


# Завдання H
def task_h():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return
    n = int(lines[0])
    possible = set(range(1, n + 1))
    for i in range(1, len(lines)):
        line = lines[i]
        if line == "HELP":
            break
        query = set(map(int, line.split()))
        yes_set = possible & query
        no_set = possible - query
        if len(yes_set) > len(no_set):
            print("YES")
            possible = yes_set
        else:
            print("NO")
            possible = no_set
    print(*(sorted(possible)))


# Завдання I
def task_i():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return
    n = int(lines[0])
    line_idx = 1
    everyone = None
    at_least_one = set()
    for _ in range(n):
        m = int(lines[line_idx])
        line_idx += 1
        current_student = set()
        for _ in range(m):
            current_student.add(lines[line_idx])
            line_idx += 1
        if everyone is None:
            everyone = current_student
        else:
            everyone &= current_student
        at_least_one |= current_student

    print(len(everyone))
    for lang in sorted(everyone):
        print(lang)
    print(len(at_least_one))
    for lang in sorted(at_least_one):
        print(lang)


# Завдання J
def task_j():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    strikes = [False] * (n + 1)
    idx = 2
    for _ in range(k):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        for day in range(a, n + 1, b):
            if day % 7 != 6 and day % 7 != 0:
                strikes[day] = True
    print(sum(strikes))


if __name__ == "__main__":
    pass
