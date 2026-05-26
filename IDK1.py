import sys

# Завдання K
def task_k():
    input_data = sys.stdin.read().split()
    counts = {}
    result = []
    for word in input_data:
        result.append(str(counts.get(word, 0)))
        counts[word] = counts.get(word, 0) + 1
    print(" ".join(result))

# Завдання L
def task_l():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n = int(lines[0].strip())
    syns = {}
    for i in range(1, n + 1):
        w1, w2 = lines[i].split()
        syns[w1] = w2
        syns[w2] = w1
    search_word = lines[n + 1].strip()
    print(syns.get(search_word, ""))

# Завдання M
def task_m():
    lines = sys.stdin.read().splitlines()
    votes = {}
    for line in lines:
        if not line.strip():
            continue
        parts = line.split()
        candidate = parts[0]
        count = int(parts[1])
        votes[candidate] = votes.get(candidate, 0) + count
    for candidate in sorted(votes.keys()):
        print(f"{candidate} {votes[candidate]}")

# Завдання N
def task_n():
    words = sys.stdin.read().split()
    if not words:
        return
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    best_word = min(counts.keys(), key=lambda w: (-counts[w], w))
    print(best_word)

# Завдання P
def task_p():
    words = sys.stdin.read().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    sorted_words = sorted(counts.keys(), key=lambda w: (-counts[w], w))
    for word in sorted_words:
        print(word)

# Завдання Q
def task_q():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0].strip())
    city_to_country = {}
    line_idx = 1
    for _ in range(n):
        parts = input_data[line_idx].split()
        country = parts[0]
        cities = parts[1:]
        for city in cities:
            city_to_country[city] = country
        line_idx += 1
    m = int(input_data[line_idx].strip())
    line_idx += 1
    for _ in range(m):
        city = input_data[line_idx].strip()
        print(city_to_country.get(city, ""))
        line_idx += 1

# Завдання R
def task_r():
    lines = sys.stdin.read().splitlines()
    balances = {}
    for line in lines:
        parts = line.split()
        if not parts:
            continue
        command = parts[0]
        if command == "Exit":
            break
        if command == "DEPOSIT":
            name, sum_val = parts[1], int(parts[2])
            balances[name] = balances.get(name, 0) + sum_val
        elif command == "WITHDRAW":
            name, sum_val = parts[1], int(parts[2])
            balances[name] = balances.get(name, 0) - sum_val
        elif command == "BALANCE":
            name = parts[1]
            if name in balances:
                print(balances[name])
            else:
                print("ERROR")
        elif command == "TRANSFER":
            name1, name2, sum_val = parts[1], parts[2], int(parts[3])
            balances[name1] = balances.get(name1, 0) - sum_val
            balances[name2] = balances.get(name2, 0) + sum_val
        elif command == "INCOME":
            p = int(parts[1])
            for name in balances:
                if balances[name] > 0:
                    balances[name] += balances[name] * p // 100

# Завдання S
def task_s():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0].strip())
    dict_words = {}
    for i in range(1, n + 1):
        w = input_data[i].strip()
        w_low = w.lower()
        if w_low not in dict_words:
            dict_words[w_low] = set()
        dict_words[w_low].add(w)
    text_line = input_data[n + 1] if len(input_data) > n + 1 else ""
    petro_words = text_line.split()
    errors = 0
    for word in petro_words:
        upper_count = sum(1 for c in word if c.isupper())
        if upper_count != 1:
            errors += 1
        else:
            w_low = word.lower()
            if w_low in dict_words:
                if word not in dict_words[w_low]:
                    errors += 1
    print(errors)

# Завдання T
def task_t():
    lines = sys.stdin.read().splitlines()
    sales = {}
    for line in lines:
        if not line.strip():
            continue
        buyer, item, count = line.split()
        count = int(count)
        if buyer not in sales:
            sales[buyer] = {}
        sales[buyer][item] = sales[buyer].get(item, 0) + count
    for buyer in sorted(sales.keys()):
        print(f"{buyer}:")
        for item in sorted(sales[buyer].keys()):
            print(f"{item} {sales[buyer][item]}")

# Завдання V
def task_v():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n = int(lines[0].strip())
    electors = {}
    for i in range(1, n + 1):
        state, num = lines[i].split()
        electors[state] = int(num)
    state_votes = {}
    all_candidates = set()
    for i in range(n + 1, len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        state, candidate = line.split()
        all_candidates.add(candidate)
        if state not in state_votes:
            state_votes[state] = {}
        state_votes[state][candidate] = state_votes[state].get(candidate, 0) + 1
    global_electors = {cand: 0 for cand in all_candidates}
    for state, votes in state_votes.items():
        if state in electors:
            winner = min(votes.keys(), key=lambda c: (-votes[c], c))
            global_electors[winner] += electors[state]
    sorted_candidates = sorted(global_electors.keys(), key=lambda c: (-global_electors[c], c))
    for cand in sorted_candidates:
        print(f"{cand} {global_electors[cand]}")

# Завдання O
def task_o():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0].strip())
    file_ops = {}
    line_idx = 1
    for _ in range(n):
        parts = input_data[line_idx].split()
        filename = parts[0]
        ops = set(parts[1:])
        file_ops[filename] = ops
        line_idx += 1
    m = int(input_data[line_idx].strip())
    line_idx += 1
    op_map = {'read': 'R', 'write': 'W', 'execute': 'X'}
    for _ in range(m):
        if line_idx >= len(input_data):
            break
        line = input_data[line_idx].strip()
        if not line:
            line_idx += 1
            continue
        op, filename = line.split()
        required_op = op_map[op]
        if filename in file_ops and required_op in file_ops[filename]:
            print("OK")
        else:
            print("Access denied")
        line_idx += 1

if __name__ == "__main__":
    pass