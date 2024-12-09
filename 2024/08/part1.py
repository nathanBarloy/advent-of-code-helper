

def get_anti(pos1, pos2):
    i1, j1 = pos1
    i2, j2 = pos2
    di = i2 - i1
    dj = j2 - j1
    return ((i1 - di, j1 - dj), (i2 + di, j2 + dj))

def in_bounds(pos, h, w):
    i, j = pos
    return 0 <= i < h and 0 <= j < w


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
                    anti1, anti2 = get_anti((i,j), other)
                    if in_bounds(anti1, h, w):
                        antinodes.add(anti1)
                    if in_bounds(anti2, h, w):
                        antinodes.add(anti2)
                antennas[c].append((i,j))
            else:
                antennas[c] = [(i,j)]

print(len(antinodes))
