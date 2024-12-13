

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
    """Return area and corners"""
    global to_see
    value = inp[i][j]
    neigh = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
    neigh = list(filter(lambda x: 0 <= x[0] < height and
                                  0 <= x[1] < width and
                                  inp[x[0]][x[1]] == value,
                        neigh))
    corner = 0
    area = 1
    # Count external corners
    match len(neigh):
        case 0:
            corner += 4
        case 1:
            corner += 2
        case 2:
            i1, j1 = neigh[0]
            i2, j2 = neigh[1]
            if not (i1 == i2 or j1 == j2):
                corner += 1
        case 3:
            pass
        case 4:
            pass
    
    # Count internal corners
    for i1, j1, i2, j2 in [(i+1,j,i,j-1), (i,j-1,i-1,j), (i-1,j,i,j+1), (i,j+1,i+1,j)]:
        if (i1, j1) in neigh and (i2, j2) in neigh:
            ci = i1 + i2 - i
            cj = j1 + j2 - j
            if inp[ci][cj] != value:
                corner += 1

    for ni, nj in neigh:
        if (ni, nj) in to_see:
            to_see.remove((ni, nj))
            a, c = visit(ni, nj)
            corner += c
            area += a
    return area, corner

    


tot = 0
while len(to_see) > 0:
    ii, ij = to_see.pop()
    area, corner = visit(ii, ij)
    tot += area * corner

print(tot)