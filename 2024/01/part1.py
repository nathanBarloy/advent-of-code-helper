l1 = []
l2 = []
with open(0) as f:
    for line in f:
        a, b = tuple(map(int, line.strip().split("   ")))
        l1.append(a)
        l2.append(b)

l1.sort()
l2.sort()

tot = 0
for i in range(len(l1)):
    tot += abs(l1[i] - l2[i])

print(tot)