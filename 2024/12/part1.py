

to_see = set()
inp = []
with open(0) as f:
    for i, line in enumerate(f):
        line = line.strip()
        inp.append(line)
        for j in range(len(line)):
            to_see.add((i,j))
height = len(inp)
width = len(inp[0])


def visit(i,j) -> (int, int):
    """Return area and perimeter"""
    global to_see
    neigh = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
    neigh = list(filter(lambda x: 0 <= x[0] < height and
                                  0 <= x[1] < width and
                                  inp[x[0]][x[1]] == inp[i][j],
                        neigh))
    perim = 4 - len(neigh)
    area = 1
    #neigh = list(filter(lambda x: x in to_see, neigh))
    for ni, nj in neigh:
        if (ni, nj) in to_see:
            to_see.remove((ni, nj))
            a, p = visit(ni, nj)
            perim += p
            area += a
    return area, perim

    


tot = 0
while len(to_see) > 0:
    ii, ij = to_see.pop()
    area, perim = visit(ii, ij)
    tot += area * perim

print(tot)