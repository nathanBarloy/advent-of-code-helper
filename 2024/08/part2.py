from math import gcd

def in_bounds(pos, h, w):
    i, j = pos
    return 0 <= i < h and 0 <= j < w


def get_anti(pos1, pos2, h, w):
    i1, j1 = pos1
    i2, j2 = pos2
    di = i2 - i1
    dj = j2 - j1
    gcd_ = gcd(di, dj)
    di //= gcd_
    dj //= gcd_

    res = []
    i = i1
    j = j1
    while in_bounds((i,j), h, w):
        res.append((i,j))
        i += di
        j += dj
    i = i1 - di
    j = j1 - dj
    while in_bounds((i,j), h, w):
        res.append((i,j))
        i -= di
        j -= dj
    return res


lines = []
with open(0) as f:
    for line in f:
        lines.append(line.strip())

antennas = {}
antinodes = set()
h = len(lines)
w = len(lines[0])
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != '.':
            if c in antennas:
                for other in antennas[c]:
                    for anti in get_anti((i,j), other, h, w):
                        antinodes.add(anti)
                antennas[c].append((i,j))
            else:
                antennas[c] = [(i,j)]

print(len(antinodes))
