#A:
a = [1, 2, 3, 4, 5]
print(a[::2])

#B:
a = [1, 2, 2, 3, 3, 3, 4]
print(*[x for x in a if x % 2 == 0])

#C:
a = [1, 5, 2, 4, 3]
print(*[a[i] for i in range(1, len(a)) if a[i] > a[i-1]])

#D:
a = [-1, 0, 1]
i = 0
while a[i] <= 0:
    i += 1
print(i)

#E:
a = [-1, 0, 1]
i = 0
while i < len(a) and a[i] <= 0:
    i += 1
print(i if i < len(a) else -1)

#F:
a = [1, 2, 3, 2, 1]
val = max(a)
print(val, a.index(val))

#G:
a = [1, 0, 1, 0, 1]
count = sum(1 for i in range(1, len(a)-1) if a[i-1] < a[i] > a[i+1])
print(count)

#H:
a = [5, -4, 3, -2, 1]
print(min(x for x in a if x > 0))

#I:
a = [6, 5, 4, 2, 1]
x = 4
print(min(a, key=lambda val: abs(val - x)))

#J:
a = [165, 163, 160, 160, 157, 157, 155, 154]
x = 162
i = 0
while i < len(a) and a[i] >= x:
    i += 1
print(i + 1)

#K:
a = [1, 2, 2, 3, 3, 3]
print(len(set(a)))

#L:
a = [0, 1, 2, 3, 4]
odds = [x for x in a if x % 2 != 0]
print(min(odds) if odds else 0)

#M:
a = [1, 2, 3, 4, 5]
n = len(a)
for i in range(n // 2):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]
print(*a)

#N:
a = [1, 2, 3, 4, 5]
for i in range(0, len(a) - 1, 2):
    a[i], a[i+1] = a[i+1], a[i]
print(*a)

#O:
a = [3, 4, 5, 2, 1]
i_min, i_max = a.index(min(a)), a.index(max(a))
a[i_min], a[i_max] = a[i_max], a[i_min]
print(*a)

#R:
a = [1, 2, 3, 2, 3]
pairs = sum(1 for i in range(len(a)) for j in range(i+1, len(a)) if a[i] == a[j])
print(pairs)

#T:
a = [3, 2, 1, 2, 3]
count = 0
for i in range(len(a)):
    is_new = True
    for j in range(i):
        if a[i] == a[j]:
            is_new = False
    if is_new:
        count += 1
print(count)

#V:
a = [1, 2, 2, 3, 3, 3]
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count == 1:
        print(a[i], end=' ')
