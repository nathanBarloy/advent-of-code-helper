


direc = None
pos = None
stones = set()
seen = set()
h = 0
w = 0

with open(0) as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '>':
                pos = (i,j)
                direc = (0,1)
            elif c == '<':
                pos = (i,j)
                direc = (0,-1)
            elif c == '^':
                pos = (i,j)
                direc = (-1,0)
            elif c == 'v':
                pos = (i,j)
                direc = (1,0)
            elif c == '#':
                stones.add((i,j))
    h = i+1
    w = j+1


def oob():
    global pos
    i, j = pos
    return not (0 <= i < h and 0 <= j < w)

def turn_right():
    global direc
    if direc == (0,1):
        direc = (1,0)
    elif direc == (1,0):
        direc = (0,-1)
    elif direc == (0,-1):
        direc = (-1,0)
    elif direc == (-1,0):
        direc = (0,1)


def step():
    global pos, direc
    i, j = pos
    newi = i
    newj = j
    di, dj = direc
    newi += di
    newj += dj
    if (newi, newj) in stones:
        turn_right()
        step()
    else:
        pos = (newi, newj)


while not oob():
    seen.add(pos)
    step()

print(len(seen))


