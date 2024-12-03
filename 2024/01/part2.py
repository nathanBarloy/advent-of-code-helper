from collections import Counter

l1 = []
l2 = []
with open(0) as f:
    for line in f:
        a, b = tuple(map(int, line.strip().split("   ")))
        l1.append(a)
        l2.append(b)

target = Counter(l2)

tot = 0
for x in l1:
    tot += target[x] * x

print(tot)