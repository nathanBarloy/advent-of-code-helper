


init_direc = None
init_pos = None
init_stones = set()
init_seen = set()
h = 0
w = 0

with open(0) as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '>':
                init_pos = (i,j)
                init_direc = (0,1)
            elif c == '<':
                init_pos = (i,j)
                init_direc = (0,-1)
            elif c == '^':
                init_pos = (i,j)
                init_direc = (-1,0)
            elif c == 'v':
                init_pos = (i,j)
                init_direc = (1,0)
            elif c == '#':
                init_stones.add((i,j))
    h = i+1
    w = j+1


def oob(pos):
    i, j = pos
    return not (0 <= i < h and 0 <= j < w)

def turn_right(direc):
    if direc == (0,1):
        direc = (1,0)
    elif direc == (1,0):
        direc = (0,-1)
    elif direc == (0,-1):
        direc = (-1,0)
    elif direc == (-1,0):
        direc = (0,1)
    return direc


def step(pos, direc, stones):
    i, j = pos
    newi = i
    newj = j
    di, dj = direc
    newi += di
    newj += dj
    if (newi, newj) in stones:
        direc = turn_right(direc)
        return step(pos, direc, stones)
    else:
        pos = (newi, newj)
        return pos, direc

def init_simul():
    global init_seen
    pos = init_pos
    direc = init_direc
    while not (oob(pos)):
        init_seen.add(pos)
        pos, direc = step(pos, direc, init_stones)

def simul(stone):
    stones = init_stones.copy()
    stones.add(stone)
    pos = init_pos
    direc = init_direc
    seen = set()
    while not (oob(pos) or (pos, direc) in seen):
        seen.add((pos, direc))
        pos, direc = step(pos, direc, stones)
    return not oob(pos)

init_simul()
init_seen.remove(init_pos)

count = 0
for stone in init_seen:
    if simul(stone):
        count += 1
print(count)


