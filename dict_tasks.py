text = input()
wordss = text.split()
a = {}
for i in wordss:
    print(a.get(i,0), end=' ')
    a[i] = a.get(i,0) + 1


