from functools import cache


topo = []
with open(0) as f:
    for line in f:
        topo.append(list(map(int, line.strip())))
height = len(topo)
width = len(topo[0])

@cache
def count_hike(init_i, init_j):
    num = topo[init_i][init_j]
    # stop case
    if num == 9:
        res = set()
        res.add((init_i, init_j))
        return res
    
    # get neigbours
    neigh = [(init_i+1, init_j), (init_i-1, init_j), (init_i, init_j+1), (init_i, init_j-1)]
    
    tot = set()
    for i, j in neigh:
        if 0<=i<height and 0<=j<width:
            if topo[i][j] == num+1:
                tot = tot.union(count_hike(i,j))
    return tot

res = 0
for i in range(height):
    for j in range(width):
        if topo[i][j] == 0:
            #print(count_hike(i,j))
            res += len(count_hike(i,j))
print(res)